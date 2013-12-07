Summary:        Taglib support for other formats 
Name:           taglib-extras
Version:        1.0.1
Release:        11
Group:          Sound 
License:        LGPLv2
URL:            http://websvn.kde.org/trunk/kdesupport/taglib-extras/
Source0:        http://www.jefferai.com/taglib-extras/taglib-extras-%{version}.tar.gz 
Source100:	taglib-extras.rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

BuildRequires:  taglib-devel
BuildRequires:  kdelibs4-devel

%description
Taglib-extras delivers support for reading and editing the meta-data of 
audio formats not supported by taglib, including: asf, mp4v2, rmff, wav.

%files
%defattr(-,root,root,-)
%doc COPYING.LGPL
%{_libdir}/libtag-extras.so.1*

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


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdv2011.0
+ Revision: 670660
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdv2011.0
+ Revision: 607963
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2010.1
+ Revision: 524140
- rebuilt for 2010.1

* Tue Sep 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.1-1mdv2010.0
+ Revision: 447139
- Update to version 1.0.1

* Thu Sep 17 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-1mdv2010.0
+ Revision: 444165
- Fix file list
- Update to version 1.0.0

* Thu Sep 10 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.7-1mdv2010.0
+ Revision: 437207
- Update to version 0.1.7

* Sun Aug 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.6-1mdv2010.0
+ Revision: 407661
- Update to version 0.1.6

* Fri Jul 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.5-1mdv2010.0
+ Revision: 399534
- Fix spec file
- Update to version 1.5

* Sun May 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.3-1mdv2010.0
+ Revision: 370969
- Update to 0.1.3 ( Fix crashes with mp4)

* Sun Apr 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.1.2-1mdv2009.1
+ Revision: 366509
- import taglib-extras


