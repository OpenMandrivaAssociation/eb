%define libname_orig lib%{name}
%define libname %mklibname %{name} 10

Summary:	Library for reading EB/EPWING files
Name:		eb
Version:	4.2.2
Release:	%mkrel 5
Group:		System/Internationalization
License:	BSD-like
URL:		http://www.sra.co.jp/people/m-kasahr/eb/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		eb-linkage_fix.diff
BuildRequires:	locales-en zlib-devel
Requires:	%{libname} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
Eb is a library for reading EB/EPWING files.

%package -n	%{libname}
Summary:	Eb library
Group:		System/Internationalization
Provides:	%{libname_orig} = %{version}-%{release}

%description -n	%{libname}
Eb library.

%package -n	%{libname}-devel
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}

%description -n	%{libname}-devel
Eb development package: static libraries, header files, and the like.


%prep

%setup -q
%patch0 -p0

%build
autoreconf -fis

%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%find_lang ebutils 

cat ebutils.lang >> %{name}.lang

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%config(noreplace) %{_sysconfdir}/eb.conf
%{_bindir}/eb*
%{_datadir}/aclocal/eb4.m4
%{_datadir}/eb/doc/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libeb.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/libeb.so
%{_includedir}/eb/*
