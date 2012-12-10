#define _disable_ld_no_undefined 1

%define name kicad-doc
%define version 1.1
%define release %mkrel 3

Summary:  Documentation for kicad (creation of electronic schematic diagrams)
Name:     %{name}
Version:  %{version}
Release:  %{release}
Source0:  %{name}-%{version}.tar.bz2
License:  GPL
Group:    Sciences/Computer science
Url:      http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: cmake

%description
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-doc is the documentation for kicad.

%prep
%setup -q -n kicad

%build
export LC_ALL=C
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%make

%install
rm -rf %{buildroot}
make -C build DESTDIR=%buildroot install

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%endif

%if %mdkversion < 200900
%postun
%endif

%files
%defattr(-,root,root)
%doc %{_datadir}/doc/kicad


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-3mdv2011.0
+ Revision: 619965
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2010.0
+ Revision: 429686
- rebuild

* Thu Aug 21 2008 trem <trem@mandriva.org> 1.1-1mdv2009.0
+ Revision: 274949
- import kicad-doc


