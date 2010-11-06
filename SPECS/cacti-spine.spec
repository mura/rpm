Name:           cacti-spine
Version:        0.8.7g
Release:        1%{?dist}
Summary:        Threaded poller for Cacti written in C

Group:          Application/System
License:        GPL
URL:            http://www.cacti.net/spine_info.php
Source0:        %{name}-%{version}.tar.gz
Patch1:         %{name}-unified_issues.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  mysql-devel, net-snmp-devel
Requires:       mysql, net-snmp

#define __global_cflags -O2 -g -pipe -Wall -fexceptions -fstack-protector --param=ssp-buffer-size=4

%description
Spine, formally Cactid, is a poller for Cacti that primarily strives to be as fast as possible.

%prep
%setup -q
%patch1 -p1

%build
./bootstrap
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
%{_sysconfdir}/spine.conf.dist
%{_bindir}/*


%changelog
* Sat Nov  6 2010 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7g-1
- Upgrade to 0.8.7g

* Sun Jan 24 2010 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7e-2
- add official patch

* Thu Jan 21 2010 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7e-1
- Upgrade to 0.8.7e

* Tue Jan 13 2009 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7a-2
- Rebuild for Fedora 10

* Mon Nov 26 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7a-1
- Upgrade to 0.8.7a

* Tue Nov 13 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 0.8.7-1
- Initial Package
