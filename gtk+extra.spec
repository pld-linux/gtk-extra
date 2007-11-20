Summary:	A useful widget set complementary to GTK+
Summary(pl.UTF-8):	Zbiór użytecznych widgetów uzupełniający GTK+
Name:		gtk+extra
Version:	2.1.1
Release:	0.9
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/scigraphica/%{name}-%{version}.tar.gz
# Source0-md5:	1a933ca1286829383a0554cc2deb9e04
URL:		http://gtkextra.sourceforge.net/
BuildRequires:	gtk+-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk+extra is a useful widget set complementary to GTK+ for creating
graphical interfaces for the X11 Window System. It is written in C and
requires GTK+ version 2.0.x.

%description -l pl.UTF-8
gtk+extra jest zbiorem pożytecznych widgetów uzupełniających GTK+,
służących do tworzenia graficznych interfejsów w systemie X11 Window.
Został napisany w C i wymaga biblioteki GTK+ w wersji 2.0.x.

%package devel
Summary:	Header files and some docs for gtk+extra library
Summary(pl.UTF-8):	Pliki nagłówkowe i nieco dokumentacji dla biblioteki gtk+extra
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and some docs for gtk+extra library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i nieco dokumentacji dla biblioteki gtk+extra.

%package static
Summary:	Static gtk+extra libraries
Summary(pl.UTF-8):	Biblioteki statyczne gtk+extra
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gtk+extra libraries.

%description static -l pl.UTF-8
Biblioteki statyczne gtk+extra.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS TODO docs/gtk*
%attr(755,root,root) %{_libdir}/libgtkextra-x11*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkextra-x11*.so
%{_libdir}/libgtkextra-x11*.la
%{_includedir}/gtkextra*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
