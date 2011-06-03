#define _disable_ld_no_undefined 1

# For doc,
# See http://iut-tice.ujf-grenoble.fr/cao/how_to_download_sources.txt
# bzr branch lp:~kicad-developers/kicad/doc
# 
# You can get the date by querying:
# $ bzr log -r-1 --line doc/
# 216: Andrey Fedorushkov 2011-06-02 update russian GUI

%define name kicad-doc
%define date 20110602
%define revision 216
%define version 1.2.%{date}.bzr%{revision}
%define release %mkrel 1

Name:     	%{name}
Summary:  	Documentation for kicad (creation of electronic schematic diagrams)
Version:  	%{version}
Release:  	%{release}
Source0:  	%{name}-bzr%{revision}.tar.bz2
License:  	GPL
Group:    	Sciences/Computer science
Url:      	http://www.lis.inpg.fr/realise_au_lis/kicad/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	cmake
BuildArch:	noarch

%description
Kicad is an open source (GPL) software for the creation of electronic 
schematic diagrams and printed circuit board artwork. 

Kicad-doc is the documentation for kicad.

%package locales
Summary:	Kicad locales
Requires:	kicad
BuildArch:	noarch

%description locales
Providing locales for the Kicad software.

%prep
%setup -q -n %{name}

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

%files locales
%defattr(-,root,root)
%{_datadir}/kicad
