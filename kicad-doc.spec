%define debug_package %{nil}
%define cxxstd 20
################################################################################
#	NOTE	Update this package at same time as the kicad and kicad-packages3d
#	NOTE	The KiCad packages are split this way to accommodate the build farm.
################################################################################

Name:		kicad-doc
Version:	9.0.0
Release:	4
Summary:	Documentation for KiCad
License:	GPL-3.0-or-later
Group:		Sciences/Computer science
URL:		https://www.kicad.org
Source0:	https://gitlab.com/kicad/services/kicad-doc/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	po4a
BuildRequires:	a2x
BuildRequires:	asciidoctor

Requires:	kicad = %{version}-%{release}

%description
Documentation for KiCad.

KiCad is EDA software to design electronic schematic diagrams and printed
circuit board artwork of up to 32 layers.


%prep
%autosetup
#autopatch -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -v -Wl,--verbose --warn-backrefs"

# Documentation (HTML only)
%cmake \
	-G Ninja \
	-DCMAKE_CXX_STANDARD=%{cxxstd} \
	-DKICAD_DOC_PATH=%{_docdir}/kicad/help \
	-DPDF_GENERATOR=none \
	-DBUILD_FORMATS=html
%ninja_build

%install
%ninja_install -C build

%files
%{_docdir}/kicad/help/
%license LICENSE*
