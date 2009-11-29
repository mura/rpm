Name:           dkimproxy
Version:        1.2
Release:        1%{?dist}
Summary:        SMTP-proxy that signs and/or verifies emails

Group:          System Environment/Daemons
License:        GPL
URL:            http://dkimproxy.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dkimproxy/%{name}-%{version}.tar.gz
Source1:        init.d-dkimproxy
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires: 	perl-Mail-DKIM, perl-Error, perl-Net-Server
Requires:       perl-Mail-DKIM, perl-Error, perl-Net-Server
Requires(pre):	/usr/sbin/useradd

%description
DKIMproxy is an SMTP-proxy that implements the DKIM and DomainKeys standards,
to sign and verify email messages using digital signatures and DNS records.
It can be used to add DKIM support to nearly any existing SMTP mail server. 

%prep
%setup -q


%build
./configure --prefix=%{_localstatedir}/lib/%{name}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_initrddir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}
%{__install} -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/%{name}

%pre
/usr/sbin/useradd -c "dkimproxy" -u 103 \
	-s /sbin/nologin -r -d %{_localstatedir}/lib/%{name} dkim 2>/dev/null || :


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO smtpprox.ChangeLog smtpprox.README smtpprox.TODO
%{_initrddir}/%{name}
%{_localstatedir}/lib/%{name}/bin
%{_localstatedir}/lib/%{name}/etc
%{_localstatedir}/lib/%{name}/lib
%attr(-,dkim,dkim) %dir %{_localstatedir}/run/%{name}

%changelog
* Sun Nov 29 2009 Yohei Murayama <muracchi@users.sourceforge.jp> 1.2-1
- update version
* Sun Apr  6 2008 Yohei Murayama <muracchi@users.sourceforge.jp> 1.0.1-2
- fix pre script
* Sun Apr  6 2008 Yohei Murayama <muracchi@users.sourceforge.jp> 1.0.1-1
- initial package