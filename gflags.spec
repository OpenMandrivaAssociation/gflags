%define		major	2.2
%define		libname	%mklibname %{name}
%define		devel	%mklibname %{name} -d

Name:		gflags
Version:	2.2.2
Release:	1
Summary:	A C++ library that implements commandline flags processing
Group:		Development/C++
License:	BSD
URL:		https://gflags.github.io/gflags/
Source0:	https://github.com/gflags/gflags/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:		0001-Add-missing-to-cmake-file.patch
Patch50:	gflags-fix-pkg-path.patch

BuildRequires:	cmake

%description
The gflags package contains a C++ library that implements commandline flags
processing. It includes built-in support for standard types such as string
and the ability to define flags in the source file in which they are used.

%package -n	%{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n	%{libname}
Libraries for %{name}

%package -n	%{devel}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n	%{devel}
Development files for %{name}

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_gflags_LIBS:BOOL=ON \
	-DINSTALL_HEADERS:BOOL=ON
%make_build

%install
%make_install -C build

# Delete file in $HOME
%{__rm} -rf %{buildroot}/${HOME}/.cmake/packages/%{name}

%files
%doc README.md ChangeLog.txt doc/
%{_bindir}/%{name}_completions.sh

%files -n	%{devel}
%{_libdir}/libgflags.so
%{_libdir}/libgflags_nothreads.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/

%files -n	%{libname}
%{_libdir}/libgflags_nothreads.so.%{major}
%{_libdir}/libgflags_nothreads.so.%{version}
%{_libdir}/libgflags.so.%{major}
%{_libdir}/libgflags.so.%{version}
