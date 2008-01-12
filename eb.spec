%define version	4.2.2
%define release	%mkrel 2

%define libname_orig lib%{name}
%define libname %mklibname %{name} 10

Name:		eb
Summary:	Eb is a library for reading EB/EPWING files
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	BSD-like
URL:		http://www.sra.co.jp/people/m-kasahr/eb/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:		locales-en zlib-devel
Requires:		%{libname} = %{version}

%description
Eb is a library for reading EB/EPWING files.


%package -n %{libname}
Summary:	Eb library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
Eb library.

%package -n %{libname}-devel
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:		%{libname} = %{version}
Provides:		%{name}-devel = %{version}-%{release}
Provides:		%{libname_orig}-devel = %{version}-%{release}

%description -n %{libname}-devel
Eb development package: static libraries, header files, and the like.


%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%config(noreplace) %{_sysconfdir}/eb.conf
%{_bindir}/eb*
%{_datadir}/aclocal/eb4.m4
%{_datadir}/eb/doc/*
%{_datadir}/locale/*/LC_MESSAGES/ebutils.mo

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


