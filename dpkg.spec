Summary:	Package maintenance system for Debian Linux
Summary(pl):	Program do obs³ugi pakietów Debiana
Name:		dpkg
Version:	1.6.15
Release:	2
License:	GPL
Group:		Applications/File
Group(de):	Applikationen/Datei
Group(pl):	Aplikacje/Pliki
Source0:	ftp://ftp.debian.org/debian/dists/potato/main/source/base/%{name}_%{version}.tar.gz
Patch0:		%{name}-no-debiandoc.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-acfix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel

%description
This package contains the programs which handle the installation and
removal of packages on your system.

The primary interface for the dpkg suite is the `dselect' program; a
more low-level and less user-friendly interface is available in the
form of the `dpkg' command.

In order to unpack and build Debian source packages you will need to
install the developers' package `dpkg-dev' as well as this one.

%description -l pl
Ten pakiet zawiera narzêdzia do obs³ugi pakietów deb znanych z
Debiana.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
gettextize --copy --force
aclocal
autoconf
%configure \
	--enable-shared \
	--without-dselect \
	--with-admindir=/var/lib/%{name}

%{__make} docdir=%{_defaultdocdir}/%{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/dpkg

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/*

%find_lang dpkg

%clean
rm -rf $RPM_BUILD_ROOT

%files -f dpkg.lang
%defattr(644,root,root,755)
%doc doc/database-structure.fig doc/internals.sgml
%doc $RPM_BUILD_ROOT%{_defaultdocdir}/%{name}/*
%attr(755,root,root) %{_bindir}/822-date
%attr(755,root,root) %{_bindir}/dpkg*
%dir %{_libdir}/dpkg
%dir %{_libdir}/dpkg/methods
%dir %{_libdir}/dpkg/parsechangelog
%dir %{_libdir}/dpkg/methods/disk
%dir %{_libdir}/dpkg/methods/floppy
%{_libdir}/dpkg/controllib.pl
%attr(755,root,root) %{_libdir}/dpkg/mksplit
%dir %{_libdir}/dpkg/methods/*/desc*
%dir %{_libdir}/dpkg/methods/*/names
%attr(755,root,root) %dir %{_libdir}/dpkg/methods/*/install
%attr(755,root,root) %dir %{_libdir}/dpkg/methods/*/setup
%attr(755,root,root) %dir %{_libdir}/dpkg/methods/*/update
%attr(755,root,root) %dir %{_libdir}/dpkg/parsechangelog/debian
%attr(755,root,root) %{_sbindir}/start-stop-daemon
%attr(755,root,root) %{_sbindir}/dpkg-divert
%attr(755,root,root) %{_sbindir}/update-alternatives
%attr(755,root,root) %{_sbindir}/update-rc.d
%dir /var/lib/dpkg
/var/lib/dpkg/*
%{_mandir}/man1/822-date.1*
%{_mandir}/man1/dpkg*
%{_mandir}/man5/*
%{_mandir}/man8/dpkg*
%{_mandir}/man8/start-stop*
%{_mandir}/man8/update*
%lang(ja) %{_mandir}/ja/man1/dpkg*
%lang(ja) %{_mandir}/ja/man5/*
%lang(ja) %{_mandir}/ja/man8/dpkg*
%lang(ja) %{_mandir}/ja/man8/start-stop*
%lang(ja) %{_mandir}/ja/man8/update*
%lang(sv) %{_mandir}/sv/man5/*
