%define contentdir /var/www

Summary: advanced protection system for PHP
Name: php-suhosin
Version: 0.9.27
Release: 1%{?dist}
License: The PHP License v3.01
Group: Development/Languages
URL: http://www.hardened-php.net/suhosin/

Source0: http://www.hardened-php.net/suhosin/_media/suhosin-%{version}.tgz

BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: php-devel >= 5.2.0
Requires: php-common >= 5.2.0

%description
The php-suhosin package contains a dynamic shared object that will add
support advanced protection.

%prep
%setup -q -n suhosin-%{version}
phpize

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign"
export CFLAGS

# Install extension modules in %{_libdir}/php/modules.
EXTENSION_DIR=%{_libdir}/php/modules; export EXTENSION_DIR

# Set PEAR_INSTALLDIR to ensure that the hard-coded include_path
# includes the PEAR directory even though pear is packaged
# separately.
PEAR_INSTALLDIR=%{_datadir}/pear; export PEAR_INSTALLDIR

%configure
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# Install everything from the CGI SAPI build
make install INSTALL_ROOT=$RPM_BUILD_ROOT 

install -m 755 -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d
install -m 755 -d $RPM_BUILD_ROOT%{php_extdir}

#mv $RPM_BUILD_ROOT/usr/lib/php/modules/suhosin.so $RPM_BUILD_ROOT%{php_extdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/suhosin.ini <<EOF
; Enable suhosin extension module
extension=suhosin.so
EOF

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{php_extdir}/suhosin.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.d/suhosin.ini

%changelog
* Sun Sep 28 2008 Yohei Murayama <muracchi@users.sourceforge.jp> 0.9.27-1
- catch up version 0.9.27

* Mon Feb 11 2008 Yohei Murayama <muracchi@users.sourceforge.jp> 0.9.23-1
- catch up version 0.9.23

* Wed Dec 19 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 0.9.22-1
- catch up version 0.9.22

* Thu Jun 28 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 0.9.20
- Initial Package
