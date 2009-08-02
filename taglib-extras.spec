Summary:        Taglib support for other formats 
Name:           taglib-extras
Version:        0.1.6
Release:        %mkrel 1
Group:          Sound 
License:        LGPLv2
URL:            http://websvn.kde.org/trunk/kdesupport/taglib-extras/
Source0:        http://www.jefferai.com/taglib-extras/taglib-extras-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

BuildRequires:  taglib-devel
BuildRequires:  kdelibs4-devel

%description
Taglib-extras delivers support for reading and editing the meta-data of 
audio formats not supported by taglib, including: asf, mp4v2, rmff, wav.

%files
%defattr(-,root,root,-)
%doc COPYING.LGPL
%{_libdir}/libtag-extras.so.0*

#--------------------------------------------------------------------

%package     devel
Summary:     Development files for %{name}
Group:       Development/C++ 
Requires:    %{name} = %{version}-%{release}
Requires:    pkgconfig
Requires:    taglib-devel
%description devel
%{summary}.

%files devel
%defattr(-,root,root,-)
%{_bindir}/taglib-extras-config
%{_includedir}/taglib-extras/
%{_libdir}/libtag-extras.so
%{_libdir}/pkgconfig/taglib-extras.pc

#--------------------------------------------------------------------

%prep
%setup -q

%build
%{cmake_kde4} -DWITH_KDE=1 ..

%make 

%install
make -C build DESTDIR=%buildroot install

%clean
rm -rf %{buildroot} 
