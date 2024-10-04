Name:    kf6-plasma-wayland-protocols
Version: 1.14.0
Release: 1%{?dist}
Summary: Plasma Specific Protocols for Wayland
License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-or-later AND MIT-CMU
URL:     https://invent.kde.org/libraries/%{name}
Source0:    %{name}-%{version}.tar.bz2

## upstream patches (lookaside cache)
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  qt6-qtbase-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%cmake_install


%files
%license LICENSES/* COPYING.LIB
%{_kf6_datadir}/plasma-wayland-protocols/

%files devel
%{_kf6_libdir}/cmake/PlasmaWaylandProtocols/
