%define	buildno 5280

Name:           packetix
Version:        2.0.%{buildno}
Release:        2%{?dist}
Summary:        a vpn solution

Group:          Network
License:        Poroprietary
URL:            http://www.softether.com/
%ifarch x86_64
Source0:        vpnserver-%{buildno}-rtm-linux-x64.tar.gz
Source1:        vpnclient-%{buildno}-rtm-linux-x64.tar.gz
Source2:        vpnbridge-%{buildno}-rtm-linux-x64.tar.gz
%endif
%ifarch i586 i686
Source0:        vpnserver-%{buildno}-rtm-linux-x32.tar.gz
Source1:        vpnclient-%{buildno}-rtm-linux-x32.tar.gz
Source2:        vpnbridge-%{buildno}-rtm-linux-x32.tar.gz
%endif
%ifarch mips
Source0:        vpnserver-%{buildno}-rtm-linux-mips.tar.gz
Source1:        vpnclient-%{buildno}-rtm-linux-mips.tar.gz
Source2:        vpnbridge-%{buildno}-rtm-linux-mips.tar.gz
%endif
%ifarch ppc
Source0:        vpnserver-%{buildno}-rtm-linux-ppc.tar.gz
Source1:        vpnclient-%{buildno}-rtm-linux-ppc.tar.gz
Source2:        vpnbridge-%{buildno}-rtm-linux-ppc.tar.gz
%endif
%ifarch sh4
Source0:        vpnserver-%{buildno}-rtm-linux-sh4.tar.gz
Source1:        vpnclient-%{buildno}-rtm-linux-sh4.tar.gz
Source2:        vpnbridge-%{buildno}-rtm-linux-sh4.tar.gz
%endif
Source3:        vpnmanual-%{buildno}-html.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

NoSource: 0
NoSource: 1
NoSource: 2
NoSource: 3

BuildRequires: glibc-devel, readline-devel, ncurses-devel
Requires:      glibc, readline, ncurses

%description
packetix vpn solution

%package vpnserver
Summary:        a vpn server
Group:          Network
Requires:	%{name} = %{version}-%{release}

%package vpnclient
Summary:        a vpn client
Group:          Network
Requires:	%{name} = %{version}-%{release}

%package vpnbridge
Summary:        a vpn bridge
Group:          Network
Requires:	%{name} = %{version}-%{release}

%description vpnserver
packetix vpn server

%description vpnclient
packetix vpn client

%description vpnbridge
packetix vpn bridge


%prep
%setup -q -b 1 -b 2 -b 3 -c


%build
pushd vpnserver
%{__make} i_read_and_agree_the_license_agreement
popd

pushd vpnclient
%{__make} vpnclient
popd

pushd vpnbridge
%{__make} vpnbridge
popd

%{__chmod} -R go-w html manual.htm

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sbindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}

%{__install} -m644 vpnserver/hamcore.se2 $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}
%{__install} -m755 vpnserver/vpncmd $RPM_BUILD_ROOT%{_bindir}
%{__install} -m755 vpnserver/vpnserver $RPM_BUILD_ROOT%{_sbindir}
%{__install} -m755 vpnclient/vpnclient $RPM_BUILD_ROOT%{_sbindir}
%{__install} -m755 vpnbridge/vpnbridge $RPM_BUILD_ROOT%{_sbindir}

%{__ln_s} %{_sbindir}/vpnserver $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/vpnserver
%{__ln_s} %{_sbindir}/vpnclient $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/vpnclient
%{__ln_s} %{_sbindir}/vpnbridge $RPM_BUILD_ROOT%{_localstatedir}/lib/%{name}/vpnbridge

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc vpnserver/License_ReadMeFirst.txt vpnserver/License_ReadMeFirstSjis.txt vpnserver/License_ReadMeFirstUtf.txt
%doc manual.htm html
%{_localstatedir}/lib/%{name}/hamcore.se2
%{_bindir}/vpncmd

%files vpnserver
%{_sbindir}/vpnserver
%{_localstatedir}/lib/%{name}/vpnserver

%files vpnclient
%{_sbindir}/vpnclient
%{_localstatedir}/lib/%{name}/vpnclient

%files vpnbridge
%{_sbindir}/vpnbridge
%{_localstatedir}/lib/%{name}/vpnbridge

%changelog
