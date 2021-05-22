%define	snap	20140324
Summary:	VA-API implementation for Intel G45 chipsets with H264 support
Summary(pl.UTF-8):	Implementacja VA-API dla układów Intela z rodziny G45 z obsługą H264
Name:		libva-driver-intel-g45
Version:	1.3.0
Release:	0.%{snap}.1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/g45h264/intel-driver-g45-h264-%{snap}.tar.gz
# Source0-md5:	3cc264b84dbbfd7b604f0cfa716dcd68
URL:		http://www.freedesktop.org/wiki/Software/vaapi
BuildRequires:	EGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	libdrm-devel >= 2.4.45
BuildRequires:	libtool
BuildRequires:	libva-devel >= 1.2.0
BuildRequires:	libva-drm-devel >= 1.2.0
BuildRequires:	libva-wayland-devel >= 1.2.0
BuildRequires:	libva-x11-devel >= 1.2.0
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(egl)
# API version, not just package version
BuildRequires:	pkgconfig(libva) >= 0.34.0
# wayland-client
BuildRequires:	wayland-devel
Requires:	libdrm >= 2.4.45
Requires:	libva >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VA-API implementation for Intel G45 chipsets with H264 support.

%description -l pl.UTF-8
Implementacja VA-API dla układów Intela z rodziny G45 z obsługą H264.

%prep
%setup -q -n intel-driver-g45-h264

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libva/dri/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README
%attr(755,root,root) %{_libdir}/libva/dri/i965_drv_video.so
