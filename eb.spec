%define soname 13
%define libname_orig lib%{name}
%define libname %mklibname %{name} %{soname}
%define develname %mklibname %{name} -d

Summary:	Library for reading EB/EPWING files
Name:		eb
Version:	4.4.2
Release:	%mkrel 3
Group:		System/Internationalization
License:	BSD-like
URL:		http://www.sra.co.jp/people/m-kasahr/eb/
Source0:	ftp://ftp.sra.co.jp/pub/misc/eb/%{name}-%{version}.tar.bz2
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
%{_libdir}/libeb.so
%{_includedir}/eb


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 4.4.2-3mdv2011.0
+ Revision: 664115
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 4.4.2-2mdv2011.0
+ Revision: 605092
- rebuild

* Mon Feb 22 2010 Frederik Himpe <fhimpe@mandriva.org> 4.4.2-1mdv2010.1
+ Revision: 509689
- Update to new version 4.4.2

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.4.1-2mdv2010.0
+ Revision: 424375
- rebuild

* Sun Mar 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 4.4.1-1mdv2009.1
+ Revision: 360530
- Updated to version 4.4.1
- Removed eb-linkage_fix.diff, similar change already applied.
- Add url of source tarball.
- Own /usr/share/eb directory (eb package).
- Move /usr/share/aclocal/eb4.m4 to right -devel subpackage.
- Own /usr/include/eb directory (libeb-devel package).
- Follow library policy (drop soname from -devel subpackage).

* Fri Sep 05 2008 Frederic Crozat <fcrozat@mandriva.com> 4.2.2-5mdv2009.0
+ Revision: 281122
- Fix incorrect lang tagging on .gmo file

* Wed Jul 02 2008 Oden Eriksson <oeriksson@mandriva.com> 4.2.2-4mdv2009.0
+ Revision: 230778
- added P0 to fix linkage (-lz)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 4.2.2-3mdv2008.1
+ Revision: 170806
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 4.2.2-2mdv2008.1
+ Revision: 149686
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Mar 08 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 4.2.2-1mdk
- new release

* Tue Nov 29 2005 Thierry Vignaud <tvignaud@mandriva.com> 4.2.1-1mdk
- bump major from 9 to 10 (it was wrong before)
- new release (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

* Tue Mar 08 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 4.1.3-2mdk
- add BuildRequires: locales-en zlib-devel

* Fri Feb 18 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 4.1.3-1mdk
- fix libification and overwriting config file
- first spec for Mandrakelinux (UTUMI Hirosi <utuhiro78@yahoo.co.jp>)

