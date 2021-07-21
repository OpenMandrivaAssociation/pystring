%define major		0.0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		pystring
Version:	1.1.3
Release:	1
Summary:	Collection of C++ functions emulating Python's string class methods
Group:		System/Libraries
License:	BSD
URL:		https://github.com/imageworks/pystring
Source0:	https://github.com/imageworks/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		0001-Add-a-CMake-configuration.patch
BuildRequires:	cmake

%description
Pystring is a collection of C++ functions which match the interface and
behavior of Python's string class methods using std::string. Implemented in
C++, it does not require or make use of a Python interpreter. It provides
convenience and familiarity for common string operations not included in the
standard C++ library. It's also useful in environments where both C++ and
Python are used.

Overlapping functionality (such as index and slice/substr) of std::string is
included to match Python interfaces.

Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

%package -n %{libname}
Summary:	Collection of C++ functions emulating Python's string class methods
Group:		System/Libraries

%description -n %{libname}
Pystring is a collection of C++ functions which match the interface and
behavior of Python's string class methods using std::string. Implemented in
C++, it does not require or make use of a Python interpreter. It provides
convenience and familiarity for common string operations not included in the
standard C++ library. It's also useful in environments where both C++ and
Python are used.

Overlapping functionality (such as index and slice/substr) of std::string is
included to match Python interfaces.

Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for %{name} library.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%license LICENSE
%doc README
%{_libdir}/libpystring.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/pystring/
%{_libdir}/libpystring.so
%{_libdir}/cmake/pystring/
