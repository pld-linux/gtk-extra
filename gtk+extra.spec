Summary:	A useful widget set complementary to GTK+
Summary(pl):	Zbiór u¿ytecznych widgetów uzupe³niaj±cy GTK+
Name:		gtk+extra
Version:	0.99.17
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://gtkextra.sourceforge.net/src/%{name}-%{version}.tar.gz
# Source0-md5:	390e622c12a5c7f7845ee144ae13ab93
Patch0:		%{name}-ac_am.patch
URL:		http://gtkextra.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	gtk+-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gtk+extra is a useful widget set complementary to GTK+ for creating
graphical interfaces for the X11 Window System. It is written in C and
requires GTK+ version 1.2.x.

%description -l pl
gtk+extra jest zbiorem po¿ytecznych widgetów uzupe³niaj±cych GTK+,
s³u¿±cych do tworzenia graficznych interfejsów w systemie X11 Window.
Zosta³ napisany w C i wymaga biblioteki GTK+ w wersji 1.2.x.

%package devel
Summary:	Header files and some docs for gtk+extra library.
Summary(pl):	Pliki nag³ówkowe i nieco dokumentacji dla biblioteki gtk+extra.
Group:		X11/Development/Libraries
Requires:	gtk+extra = %{version}

%description devel
Header files and some docs for gtk+extra library.

%description devel -l pl
Pliki nag³ówkowe i nieco dokumentacji dla biblioteki gtk+extra.

%package static
Summary:	Static gtk+extra libraries.
Summary(pl):	Biblioteki statyczne gtk+extra.
Group:		X11/Development/Libraries
Requires:	gtk+extra-devel = %{version}

%description static
Static gtk+extra libraries.

%description static -l pl
Biblioteki statyczne gtk+extra.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%doc README AUTHORS NEWS TODO docs/gtk*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_includedir}/gtkextra
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
