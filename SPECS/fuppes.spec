Name:           fuppes
Version:        0.660
Release:        6%{?dist}
Summary:        multiplatform UPnP A/V Media Server

Group:          System Environment/Daemons
License:        GPL
URL:            http://fuppes.ulrich-voelkel.de/
Source0:        http://sourceforge.net/projects/fuppes/files/fuppes/fuppes-%{version}.tar.gz
Source1:		init.d-fuppesd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pcre-devel, libxml2-devel, sqlite-devel, gettext-devel, ffmpeg-devel, libdlna-devel, ImageMagick-devel, mysql-devel, flac-devel, libmp4v2-devel, twolame-devel
Requires:       libuuid, libxml2, pcre, sqlite
Requires(post): /sbin/chkconfig, /sbin/service
Requires(preun): /sbin/chkconfig, /sbin/service

%description
FUPPES is a free, multiplatform UPnP A/V Media Server.
FUPPES supports a wide range of UPnP MediaRenderers (see "features" for 
details) as well as on-the-fly transcoding of various audio, video and image formats.
FUPPES also includes basic DLNA support.

%package devel
Group: Development/Libraries
Summary: Files needed for building FUPPES Plugins

%description devel
The %{name}-devel package contains the files needed for building FUPPES
Plugins.

%package decoder-flac
Group: System Environment/Libraries
Summary: FUPPES flac decorder plugin

%description decoder-flac
The %{name}-decoder-flac package contains flac decoder plugin for fuppes.

%package decoder-musepack
Group: System Environment/Libraries
Summary: FUPPES musepack decorder plugin

%description decoder-musepack
The %{name}-decoder-musepack package contains musepack decoder plugin for fuppes.

%package decoder-vorbis
Group: System Environment/Libraries
Summary: FUPPES vorbis decorder plugin

%description decoder-vorbis
The %{name}-decoder-vorbis package contains vorbis decoder plugin for fuppes.

%package encoder-pcm
Group: System Environment/Libraries
Summary: FUPPES pcm encoder plugin

%description encoder-pcm
The %{name}-encoder-pcm package contains pcm encoder plugin for fuppes.

%package encoder-wav
Group: System Environment/Libraries
Summary: FUPPES wav encoder plugin

%description encoder-wav
The %{name}-encoder-wav package contains wav encoder plugin for fuppes.

%package metadata-dlnaprofiles
Group: System Environment/Libraries
Summary: FUPPES dlna profiles metadata plugin

%description metadata-dlnaprofiles
The %{name}-metadata-dlnaprofiles package contains dlna profiles metadata plugin for fuppes.

%package metadata-exiv2
Group: System Environment/Libraries
Summary: FUPPES exiv2 metadata plugin

%description metadata-exiv2
The %{name}-metadata-exiv2 package contains exiv2 metadata plugin for fuppes.

%package metadata-libavformat
Group: System Environment/Libraries
Summary: FUPPES libavformat metadata plugin

%description metadata-libavformat
The %{name}-metadata-libavformat package contains libavformat metadata plugin for fuppes.

%package metadata-libmp4v2
Group: System Environment/Libraries
Summary: FUPPES libmp4v2 metadata plugin

%description metadata-libmp4v2
The %{name}-metadata-libmp4v2 package contains libmp4v2 metadata plugin for fuppes.

%package metadata-magickwand
Group: System Environment/Libraries
Summary: FUPPES magickwand metadata plugin

%description metadata-magickwand
The %{name}-metadata-magickwand package contains magickwand metadata plugin for fuppes.

%package metadata-taglib
Group: System Environment/Libraries
Summary: FUPPES taglib metadata plugin

%description metadata-taglib
The %{name}-metadata-taglib package contains taglib metadata plugin for fuppes.

%package transcoder-ffmpeg
Group: System Environment/Libraries
Summary: FUPPES ffmpeg transcoder plugin

%description transcoder-ffmpeg
The %{name}-transcoder-ffmpeg package contains ffmpeg transcoder plugin for fuppes.

%package transcoder-magickwand
Group: System Environment/Libraries
Summary: FUPPES magickwand transcoder plugin

%description transcoder-magickwand
The %{name}-transcoder-magickwand package contains magickwand transcoder plugin for fuppes.

%package database-mysql
Group: System Environment/Libraries
Summary: FUPPES mysql database plugin

%description database-mysql
The %{name}-database-mysql package contains mysql database plugin for fuppes.

%prep
%setup -q

%build
CPPFLAGS="-I%{_includedir}/ffmpeg -I%{_includedir}/taglib" ; export CPPFLAGS
CFLAGS="$RPM_OPT_FLAGS $CPPFLAGS" ; export CFLAGS
CXXFLAGS="$RPM_OPT_FLAGS $CPPFLAGS" ; export CXXFLAGS
TAGLIB_CONFIG='taglib-config' ; export TAGLIB_CONFIG
echo 'echo "-I/usr/include/"' > mpeg4ip-config
chmod +x mpeg4ip-config
MPEG4IP_CONFIG="./mpeg4ip-config" ; export MPEG4IP_CONFIG
UUID_LIBS="-lossp-uuid"
%configure --enable-transcoder-ffmpeg --enable-lame --enable-twolame --enable-flac --enable-mad --enable-faad --enable-twolime
%{__make} %{?_smp_mflags}

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
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/fuppes
%{__mkdir_p} $RPM_BUILD_ROOT%{_initrddir}
%{__install} -m755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/fuppesd
find $RPM_BUILD_ROOT%{_libdir} -name '*.la' -delete

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog INSTALL README THANKS TODO
%dir %attr(0755, fuppes, fuppes) %{_sysconfdir}/fuppes
%{_initrddir}
%{_bindir}
%{_libdir}/libfuppes.so*
%{_libdir}/fuppes/libdatabase_sqlite3.so*
%{_datadir}

%files devel
%defattr(-,root,root,-)
%{_includedir}

%files decoder-flac
%defattr(-,root,root,-)
%{_libdir}/fuppes/libdecoder_flac.so*

%files decoder-musepack
%defattr(-,root,root,-)
%{_libdir}/fuppes/libdecoder_musepack.so*

%files decoder-vorbis
%defattr(-,root,root,-)
%{_libdir}/fuppes/libdecoder_vorbis.so*

%files encoder-pcm
%defattr(-,root,root,-)
%{_libdir}/fuppes/libencoder_pcm.so*

%files encoder-wav
%defattr(-,root,root,-)
%{_libdir}/fuppes/libencoder_wav.so*

%files metadata-dlnaprofiles
%defattr(-,root,root,-)
%{_libdir}/fuppes/libmetadata_dlna_profiles.so*

%files metadata-exiv2
%defattr(-,root,root,-)
%{_libdir}/fuppes/libmetadata_exiv2.so*

%files metadata-libavformat
%defattr(-,root,root,-)
%{_libdir}/fuppes/libmetadata_libavformat.so*

%files metadata-libmp4v2
%defattr(-,root,root,-)
%{_libdir}/fuppes/libmetadata_libmp4v2.so*

%files metadata-magickwand
%defattr(-,root,root,-)
%{_libdir}/fuppes/libmetadata_magickwand.so*

%files metadata-taglib
%defattr(-,root,root,-)
%{_libdir}/fuppes/libmetadata_taglib.so*

%files transcoder-ffmpeg
%defattr(-,root,root,-)
%{_libdir}/fuppes/libtranscoder_ffmpeg.so*

%files transcoder-magickwand
%defattr(-,root,root,-)
%{_libdir}/fuppes/libtranscoder_magickwand.so*

%files database-mysql
%defattr(-,root,root,-)
%{_libdir}/fuppes/libdatabase_mysql.so*

%changelog
