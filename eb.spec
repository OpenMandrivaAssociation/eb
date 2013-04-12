%define major	13
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Library for reading EB/EPWING files
Name:		eb
Version:	4.4.2
Release:	4
Group:		System/Internationalization
License:	BSD-like
Url:		http://www.sra.co.jp/people/m-kasahr/eb/
Source0:	ftp://ftp.sra.co.jp/pub/misc/eb/%{name}-%{version}.tar.bz2
BuildRequires:	locales-en
BuildRequires:	pkgconfig(zlib)

%description
Eb is a library for reading EB/EPWING files.

%package -n	%{libname}
Summary:	Eb library
Group:		System/Internationalization

%description -n	%{libname}
Eb library.

%package -n	%{devname}
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
Eb development package: static libraries, header files, and the like.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

%find_lang ebutils 

cat ebutils.lang >> %{name}.lang

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/eb.conf
%{_bindir}/eb*
%{_datadir}/eb

%files -n %{libname}
%{_libdir}/libeb.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/aclocal/eb4.m4
%{_libdir}/libeb.so
%{_includedir}/eb

