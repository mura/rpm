%define contentdir /var/www
%define apiver 20041225
%define zendver 20050922
%define pdover 20060409
%define ext ZendOptimizer

%ifarch x86_64
%define pkgname ZendOptimizer-%{version}-linux-glibc23-x86_64
%endif
%ifarch i386
%define pkgname ZendOptimizer-%{version}-linux-glibc21-i386
%endif

Summary: PHP code optimizer
Name: php-%{ext}
Version: 3.3.0a
Release: 1
License: The PHP License v3.01
Group: Development/Languages

URL: http://www.zend.com/products/zend_optimizer
Source0: %{pkgname}.tar.gz

Requires: php >= 4.2.0
%ifarch x86_64
Requires: glibc >= 2.3
%endif
%ifarch i386
Requires: glibc >= 2.1
%endif

NoSource: 0

BuildRoot: %{_tmppath}/%{name}-root


%description
The Zend Optimizer is a free application that runs the files encoded by the Zend Guard,
while enhancing the performance of PHP applications.

%prep
%setup -q -n %{pkgname}

%build

%check

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
install -m 755 -d $RPM_BUILD_ROOT%{_bindir}
for phpvar in 4.2.0 4.2.x 4.3.x 4.4.x 5.0.x 5.1.x 5.2.x
do
  install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer-%{version}/php-${phpvar}
  install -m 755 -d $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer_TS-%{version}/php-${phpvar}
done

## Single Thread
install -m 755 data/4_2_0_comp/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer-%{version}/php-4.2.0
install -m 755 data/4_2_x_comp/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer-%{version}/php-4.2.x
install -m 755 data/4_3_x_comp/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer-%{version}/php-4.3.x
install -m 755 data/4_4_x_comp/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer-%{version}/php-4.4.x
install -m 755 data/5_0_x_comp/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer-%{version}/php-5.0.x
install -m 755 data/5_1_x_comp/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer-%{version}/php-5.1.x
install -m 755 data/5_2_x_comp/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer-%{version}/php-5.2.x

## Thread Safe
install -m 755 data/4_2_x_comp/TS/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer_TS-%{version}/php-4.2.x
install -m 755 data/4_3_x_comp/TS/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer_TS-%{version}/php-4.3.x
install -m 755 data/4_4_x_comp/TS/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer_TS-%{version}/php-4.4.x
install -m 755 data/5_0_x_comp/TS/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer_TS-%{version}/php-5.0.x
install -m 755 data/5_1_x_comp/TS/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer_TS-%{version}/php-5.1.x
install -m 755 data/5_2_x_comp/TS/%{ext}.so $RPM_BUILD_ROOT%{_libdir}/php/modules/Optimizer_TS-%{version}/php-5.2.x

install -m 755 data/ZendExtensionManager.so $RPM_BUILD_ROOT%{_libdir}/php/modules
install -m 755 data/ZendExtensionManager_TS.so $RPM_BUILD_ROOT%{_libdir}/php/modules

install -m 644 data/poweredbyoptimizer.gif $RPM_BUILD_ROOT%{_sysconfdir}

install -m 644 data/zendid $RPM_BUILD_ROOT%{_bindir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/%{ext}.ini <<EOF
; Enable %{ext} extension module
zend_extension_manager.optimizer=%{_libdir}/php/modules/Optimizer-%{version}
zend_extension_manager.optimizer_ts=%{_libdir}/php/modules/Optimizer_TS-%{version}
zend_extension=%{_libdir}/php/modules/ZendExtensionManager.so
zend_extension_ts=%{_libdir}/php/modules/ZendExtensionManager_TS.so
zend_optimizer.enable_loader=0
zend_optimizer.disable_licensing=1
EOF

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%doc EULA-ZendOptimizer LICENSE README-ZendOptimizer
%attr(755,root,root) %{_libdir}/php/modules/Optimizer-%{version}/php-4.2.0/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer-%{version}/php-4.2.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer-%{version}/php-4.3.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer-%{version}/php-4.4.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer-%{version}/php-5.0.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer-%{version}/php-5.1.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer-%{version}/php-5.2.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer_TS-%{version}/php-4.2.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer_TS-%{version}/php-4.3.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer_TS-%{version}/php-4.4.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer_TS-%{version}/php-5.0.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer_TS-%{version}/php-5.1.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/Optimizer_TS-%{version}/php-5.2.x/%{ext}.so
%attr(755,root,root) %{_libdir}/php/modules/ZendExtensionManager.so
%attr(755,root,root) %{_libdir}/php/modules/ZendExtensionManager_TS.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.d/%{ext}.ini
%attr(755,root,root) %{_sysconfdir}/poweredbyoptimizer.gif
%attr(755,root,root) %{_bindir}/zendid

%changelog
* Wed Dec 19 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 3.3.0a-1
- catch up version 3.3.0a

* Thu Aug  9 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 3.3.0-1
- catch up version 3.3.0

* Thu Jul 02 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 3.2.6-1
- Initial Package
