Name:           fuppes
Version:        0.640
Release:        2%{?dist}
Summary:        multiplatform UPnP A/V Media Server

Group:          System Environment/Daemons
License:        GPL
URL:            http://fuppes.ulrich-voelkel.de/
Source0:        http://sourceforge.net/projects/fuppes/files/fuppes/fuppes-%{version}.tar.gz
Source1:		init.d-fuppesd
Patch0:			fuppes-0.640-fedora.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pcre-devel, libxml2-devel, sqlite-devel, gettext-devel, ffmpeg-devel, libdlna-devel, ImageMagick-devel
Requires:       libdlna, ffmpeg-libs, ImageMagick
Requires(post): /sbin/chkconfig, /sbin/service
Requires(preun): /sbin/chkconfig, /sbin/service

%description
FUPPES is a free, multiplatform UPnP A/V Media Server.
FUPPES supports a wide range of UPnP MediaRenderers (see "features" for details) as well as on-the-fly transcoding of various audio, video and image formats.
FUPPES also includes basic DLNA support.

%package devel
Group: Development/Libraries
Summary: Files needed for building FUPPES Plugins

%description devel
The %{name}-devel package contains the files needed for building FUPPES
Plugins.

%prep
%setup -q

%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%pre
/usr/sbin/useradd -M -s /sbin/nologin -d /usr/share/fuppes -r fuppes &>/dev/null || :
/usr/sbin/usermod -s /sbin/nologin fuppes &>/dev/null || :

%post
/sbin/chkconfig --add fuppesd

%preun
/sbin/chkconfig --del fuppesd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_initrddir}
%{__install} -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/fuppesd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL README THANKS TODO
%{_initrddir}
%{_bindir}
%{_libdir}
%{_datadir}

%files devel
%defattr(-,root,root,-)
%{_includedir}

%changelog
