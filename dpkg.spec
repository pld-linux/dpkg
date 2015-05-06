%include	/usr/lib/rpm/macros.perl
Summary:	Package maintenance system for Debian Linux
Summary(pl.UTF-8):	Program do obsługi pakietów Debiana
Name:		dpkg
Version:	1.17.25
Release:	1
License:	GPL v2+
Group:		Applications/File
Source0:	ftp://ftp.debian.org/debian/pool/main/d/dpkg/%{name}_%{version}.tar.xz
# Source0-md5:	e48fcfdb2162e77d72c2a83432d537ca
Patch0:		%{name}-md5.patch
URL:		http://packages.debian.org/search?keywords=dpkg
BuildRequires:	bzip2-devel
BuildRequires:	gettext-tools >= 0.18.2
BuildRequires:	libselinux-devel
BuildRequires:	perl-tools-pod
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.654
BuildRequires:	rpm-perlprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# blacklist false positives
%define		_noautoreq_perl		extra file in Tie::ExtraHash

%description
This package contains the programs to handle deb packages known from
Debian.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do obsługi pakietów deb znanych z
Debiana.

%package -n libdpkg-devel
Summary:	dpkg library and header files
Summary(pl.UTF-8):	Biblioteka i pliki nagłówkowe dpkg
Group:		Development/Libraries
Requires:	bzip2-devel
Requires:	xz-devel
Requires:	zlib-devel

%description -n libdpkg-devel
dpkg library and header files.

%description -n libdpkg-devel -l pl.UTF-8
Biblioteka i pliki nagłówkowe dpkg.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	PO4A="true" \
	--disable-dselect \
	--disable-silent-rules \
	--disable-start-stop-daemon \
	--with-admindir=/var/lib/%{name}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/alternatives/README

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdpkg.la

# dpkg for main part, dpkg-dev for perl-based build script
# don't use --all-name to avoid e.g. dselect inclusion
%find_lang dpkg
%find_lang dpkg-dev
cat dpkg-dev.lang >>dpkg.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f dpkg.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/dpkg*
%attr(755,root,root) %{_bindir}/update-alternatives
%dir %{_sysconfdir}/alternatives
%dir %{_sysconfdir}/dpkg
%dir %{_sysconfdir}/dpkg/dpkg.cfg.d

%dir %{_libdir}/dpkg
%dir %{_libdir}/dpkg/parsechangelog
%attr(755,root,root) %{_libdir}/dpkg/parsechangelog/debian
%dir %{_datadir}/dpkg
%{_datadir}/dpkg/abitable
%{_datadir}/dpkg/cputable
%{_datadir}/dpkg/ostable
%{_datadir}/dpkg/triplettable
%{_datadir}/dpkg/*.mk

%{perl_vendorlib}/Dpkg.pm
%{perl_vendorlib}/Dpkg

%dir /var/lib/dpkg
%dir /var/lib/dpkg/alternatives
%dir /var/lib/dpkg/info
%dir /var/lib/dpkg/parts
%dir /var/lib/dpkg/updates

%{_mandir}/man1/dpkg*.1*
%{_mandir}/man3/Dpkg.3*
%{_mandir}/man3/Dpkg::*.3*
%{_mandir}/man5/deb*.5*
%{_mandir}/man5/dpkg.cfg.5*
%{_mandir}/man8/dpkg-*.8*
%{_mandir}/man8/update-alternatives.8*
%lang(de) %{_mandir}/de/man1/dpkg*.1*
%lang(de) %{_mandir}/de/man5/deb*.5*
%lang(de) %{_mandir}/de/man5/dpkg.cfg.5*
%lang(de) %{_mandir}/de/man8/dpkg-*.8*
%lang(de) %{_mandir}/de/man8/update-alternatives.8*
%lang(es) %{_mandir}/es/man1/dpkg*.1*
%lang(es) %{_mandir}/es/man5/deb*.5*
%lang(es) %{_mandir}/es/man5/dpkg.cfg.5*
%lang(es) %{_mandir}/es/man8/dpkg-*.8*
%lang(es) %{_mandir}/es/man8/update-alternatives.8*
%lang(fr) %{_mandir}/fr/man1/dpkg*.1*
%lang(fr) %{_mandir}/fr/man5/deb*.5*
%lang(fr) %{_mandir}/fr/man5/dpkg.cfg.5*
%lang(fr) %{_mandir}/fr/man8/dpkg-*.8*
%lang(fr) %{_mandir}/fr/man8/update-alternatives.8*
%lang(hu) %{_mandir}/hu/man5/dpkg.cfg.5*
%lang(it) %{_mandir}/it/man1/dpkg*.1*
%lang(it) %{_mandir}/it/man5/deb*.5*
%lang(it) %{_mandir}/it/man5/dpkg.cfg.5*
%lang(it) %{_mandir}/it/man8/dpkg-*.8*
%lang(it) %{_mandir}/it/man8/update-alternatives.8*
%lang(ja) %{_mandir}/ja/man1/dpkg*.1*
%lang(ja) %{_mandir}/ja/man5/deb*.5*
%lang(ja) %{_mandir}/ja/man5/dpkg.cfg.5*
%lang(ja) %{_mandir}/ja/man8/dpkg*.8*
%lang(ja) %{_mandir}/ja/man8/update-alternatives.8*
%lang(pl) %{_mandir}/pl/man1/dpkg*.1*
%lang(pl) %{_mandir}/pl/man5/deb*.5*
%lang(pl) %{_mandir}/pl/man5/dpkg.cfg.5*
%lang(pl) %{_mandir}/pl/man8/dpkg-*.8*
%lang(pl) %{_mandir}/pl/man8/update-alternatives.8*
%lang(sv) %{_mandir}/sv/man1/dpkg*.1*
%lang(sv) %{_mandir}/sv/man5/deb*.5*
%lang(sv) %{_mandir}/sv/man5/dpkg.cfg.5*
%lang(sv) %{_mandir}/sv/man8/dpkg-*.8*
%lang(sv) %{_mandir}/sv/man8/update-alternatives.8*

%files -n libdpkg-devel
%defattr(644,root,root,755)
%{_libdir}/libdpkg.a
%{_includedir}/dpkg
%{_pkgconfigdir}/libdpkg.pc
