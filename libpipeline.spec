Summary:	A pipeline manipulation library
Name:		libpipeline
Version:	1.4.0
Release:	1
License:	GPL v3+
Group:		Development/Libraries
Source0:	http://download.savannah.gnu.org/releases/libpipeline/%{name}-%{version}.tar.gz
# Source0-md5:	660f4ac9340834a231d1516746d03d28
URL:		http://libpipeline.nongnu.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpipeline is a C library for setting up and running pipelines of
processes, without needing to involve shell command-line parsing which
is often error-prone and insecure. This alleviates programmers of the
need to laboriously construct pipelines using lower-level primitives
such as fork(2) and execve(2).

%package devel
Summary:	Header files and libraries for pipeline manipulation library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libpipeline-devel contains the header files and libraries needed to
develop programs that use libpipeline library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gnulib/m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libpipeline.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS
%attr(755,root,root) %ghost %{_libdir}/libpipeline.so.?
%attr(755,root,root) %{_libdir}/libpipeline.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libpipeline.so
%{_includedir}/*.h
%{_mandir}/man3/*
%{_pkgconfigdir}/libpipeline.pc

