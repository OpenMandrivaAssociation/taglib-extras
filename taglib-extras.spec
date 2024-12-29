Summary:		Taglib support for other formats 
Name:			taglib-extras
Version:		1.0.1
Release:		19
Group:			Sound 
License:		LGPLv2
URL:			https://websvn.kde.org/trunk/kdesupport/taglib-extras/
Source0:		http://www.jefferai.com/taglib-extras/taglib-extras-%{version}.tar.gz 
Source100:		taglib-extras.rpmlintrc
#Patch1:			taglib-1.10.patch
Patch2:     https://aur.archlinux.org/cgit/aur.git/plain/taglib-2.0.diff

BuildRequires:	cmake
BuildRequires:	pkgconfig(taglib)
BuildRequires:  pkgconfig(zlib)

%description
Taglib-extras delivers support for reading and editing the meta-data of 
audio formats not supported by taglib, including: asf, mp4v2, rmff, wav.

%files
%doc COPYING.LGPL
%{_libdir}/libtag-extras.so.1*

#--------------------------------------------------------------------

%package  devel
Summary:	Development files for %{name}
Group:		Development/C++ 
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
Requires:	pkgconfig(taglib)

%description devel
%{summary}.

%files devel
%{_bindir}/taglib-extras-config
%{_includedir}/taglib-extras/
%{_libdir}/libtag-extras.so
%{_libdir}/pkgconfig/taglib-extras.pc

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%{cmake} ..

%make_build

%install
%make_install -C build
