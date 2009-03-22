%define soname 13
%define libname_orig lib%{name}
%define libname %mklibname %{name} %{soname}
%define develname %mklibname %{name} -d

Summary:	Library for reading EB/EPWING files
Name:		eb
Version:	4.4.1
Release:	%mkrel 1
Group:		System/Internationalization
License:	BSD-like
URL:		http://www.sra.co.jp/people/m-kasahr/eb/
Source0:	ftp://ftp.sra.co.jp/pub/misc/eb/eb-%{version}.tar.lzma
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

%package -n	%{develname}
Summary:	Headers of %{name} for development
Group:		Development/C
Conflicts:	eb <= 4.2.2-5mdv2009.0
Obsoletes:	libeb10-devel <= 4.2.2-5mdv2009.0
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
Eb development package: static libraries, header files, and the like.


%prep
%setup -q

%build
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
%{_datadir}/eb

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/libeb.so.%{soname}*

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING
%{_datadir}/aclocal/eb4.m4
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/libeb.so
%{_includedir}/eb
