%define uplddir /var/www/uploader

Summary: File upload application works as Apache module
Name: mod_uploader
Version: 3.1.0
Release: 2%{?dist}
Epoch: 1
Group: System Environment/Daemons
URL: http://acapulco.dyndns.org/mod_uploader
Source: %{name}-%{version}.tgz
License: The zlib/libpng License
BuildRoot: %{_tmppath}/%{name}-%{release}-root
BuildPrereq: httpd-devel >= 2.0, ImageMagick-c++-devel >= 6.0, libtool >= 1.5, make >= 3.8, gcc >= 3.3
Requires: httpd >= 2.0, ImageMagick-c++ >= 6.0

%description
mod_uploader is a file upload application works as Apache module. The following features are provided:
- It works faster than the thing made with Perl or PHP or Ruby, because it is made with C++ and works as Apache module. 
- It includes simple template engine, so you can change page layouts without re-compilation. 
- it can show progress report when uploading. 

%prep
%setup -q

%build
#export CFLAGS="$RPM_OPT_FLAGS"
%configure --enable-thumbnail --with-apctl=%{_sbindir}/apachectl
%{__make} %{?_smp_mflags} apache-module

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/httpd/modules
mkdir -p $RPM_BUILD_ROOT%{uplddir}/conf
mkdir -p $RPM_BUILD_ROOT%{uplddir}/img
mkdir -p $RPM_BUILD_ROOT%{uplddir}/css
mkdir -p $RPM_BUILD_ROOT%{uplddir}/js
mkdir -p $RPM_BUILD_ROOT%{uplddir}/swf
mkdir -p $RPM_BUILD_ROOT%{uplddir}/tmpl
mkdir -p $RPM_BUILD_ROOT%{uplddir}/tmpl/en
mkdir -p $RPM_BUILD_ROOT%{uplddir}/upld/data
mkdir -p $RPM_BUILD_ROOT%{uplddir}/upld/file
mkdir -p $RPM_BUILD_ROOT%{uplddir}/upld/thumb
mkdir -p $RPM_BUILD_ROOT%{uplddir}/upld/temp

install -m755 %{name}.so $RPM_BUILD_ROOT%{_libdir}/httpd/modules

install -m644 img/* $RPM_BUILD_ROOT%{uplddir}/img
install -m644 css/* $RPM_BUILD_ROOT%{uplddir}/css
install -m644 js/* $RPM_BUILD_ROOT%{uplddir}/js
install -m644 swf/* $RPM_BUILD_ROOT%{uplddir}/swf

install -m644 tmpl/*.htm $RPM_BUILD_ROOT%{uplddir}/tmpl
install -m644 tmpl/en/*.htm $RPM_BUILD_ROOT%{uplddir}/tmpl/en

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog MEMO doc
%{_libdir}/httpd/modules/*.so
#%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%attr(-, root, root) %{uplddir}/img/*
%attr(-, root, root) %{uplddir}/css/*
%attr(-, root, root) %{uplddir}/js/*
%attr(-, root, root) %{uplddir}/swf/*
%attr(-, root, root) %{uplddir}/tmpl/*.htm
%attr(-, root, root) %{uplddir}/tmpl/en/*.htm
%attr(-, apache, apache) %dir %{uplddir}/upld/data
%attr(-, apache, apache) %dir %{uplddir}/upld/file
%attr(-, apache, apache) %dir %{uplddir}/upld/thumb
%attr(-, apache, apache) %dir %{uplddir}/upld/temp


%changelog
* Tue Jan 13 2009 Yohei Murayama <muracchi@users.sourceforge.jp> 3.1.0-2
- Rebuild for Fedora 10

* Sun Sep 28 2008 Yohei Murayama <muracchi@users.sourceforge.jp> 3.1.0-1
- Update to 3.1.0

* Wed Apr  2 2008 Yohei Murayama <muracchi@users.sourceforge.jp> 3.0.6-1
- Update to 3.0.6

* Mon Feb 11 2008 Yohei Murayama <muracchi@users.sourceforge.jp> 3.0.3-1
- Update to 3.0.3

* Fri Dec 14 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 2.6.5-1
- Update to 2.5.8

* Fri Nov  9 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 2.5.8-2
- Add swf file

* Fri Nov  9 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 2.5.8-1
- Update to 2.5.8

* Wed Aug 29 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 2.5.4-1
- Update to 2.5.4

* Tue Aug 21 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 2.5.3-1
- Update to 2.5.3

* Thu Aug  9 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 2.5.2-1
- Update to 2.5.2

* Thu Jul 12 2007 Yohei Murayama <muracchi@users.sourceforge.jp> 2.4.9-1
- initial package
