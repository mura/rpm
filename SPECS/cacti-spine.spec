Name:           cacti-spine
Version:        0.8.7a
Release:        2%{?dist}
Summary:        Threaded poller for Cacti written in C

Group:          Application/System
License:        GPL
URL:            http://www.cacti.net/spine_info.php
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  mysql-devel, net-snmp-devel
Requires:       mysql, net-snmp

%define __global_cflags -O2 -g -pipe -Wall -fexceptions -fstack-protector --param=ssp-buffer-size=4

%description
Spine, formally Cactid, is a poller for Cacti that primarily strives to be as fast as possible.

%prep
%setup -q

%build
%{__aclocal}
%{__libtoolize} --copy --force
%{__autoconf}
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS
%doc LICENSE LICENSE.LGPL README README-WINDOWS
%config %{_sysconfdir}/spine.conf
%{_bindir}/*


%changelog
* Tue Jan 13 2009 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7a-2
- Rebuild for Fedora 10

* Mon Nov 26 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7a-1
- Upgrade to 0.8.7a

* Tue Nov 13 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7-1
- Initial Package
