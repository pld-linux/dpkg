#
# Conditional build:
%bcond_with	alternatives	# build alternatives package

Summary:	Package maintenance system for Debian Linux
Summary(pl.UTF-8):	Program do obsługi pakietów Debiana
Name:		dpkg
Version:	1.22.11
Release:	1
License:	GPL v2+
Group:		Applications/File
Source0:	http://ftp.debian.org/debian/pool/main/d/dpkg/%{name}_%{version}.tar.xz
# Source0-md5:	20fd4de234d9192a941ae58b616677ec
URL:		https://packages.debian.org/search?keywords=dpkg
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	libmd-devel
BuildRequires:	libselinux-devel >= 2.3
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	ncurses-devel >= 5
BuildRequires:	perl-base >= 1:5.32.1
BuildRequires:	perl-tools-pod >= 1:5.32.1
BuildRequires:	pkgconfig
BuildRequires:	po4a >= 0.59
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.754
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRequires:	zstd-devel
Requires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# blacklist false positives
%define		_noautoreq_perl		at extra file

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

%package alternatives
Summary:	Maintain symbolic links determining default commands
Summary(pl.UTF-8):	Utrzymywanie dowiązań symbolicznych określających domyślne polecenia
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description alternatives
alternatives creates, removes, maintains and displays information
about the symbolic links comprising the alternatives system. The
alternatives system is a reimplementation of the Debian alternatives
system.

%description alternatives -l pl.UTF-8
alternatives tworzy, usuwa, utrzymuje i wyświetla informacje o
dowiązaniach symbolicznych obejmujących system alternatyw. System
alternatyw to reimplementacja systemu alternatyw ("alternatives") z
Debiana.

%package -n zsh-completion-dpkg
Summary:        ZSH completion for dpkg command
Summary(pl.UTF-8):      Dopełnianianie parametrów w ZSH dla polecenia dpkg
Group:          Applications/Shells
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
BuildArch:      noarch

%description -n zsh-completion-dpkg
ZSH completion for dpkg command.

%description -n zsh-completion-dpkg -l pl.UTF-8
Dopełnianianie parametrów w ZSH dla polecenia dpkg.

%prep
%setup -q

%build
# dpkg expects <md5.h> from FreeBSD-compatible libmd (not libmd5)
CPPFLAGS="%{rpmcppflags} -I/usr/include/libmd"
%configure \
	PO4A="true" \
	--disable-devel-docs \
	--disable-dselect \
	--disable-silent-rules \
	--disable-start-stop-daemon \
	%{!?with_alternatives:--disable-update-alternatives} \
	--with-admindir=/var/lib/%{name} \
	--with-zshcompletionsdir=%{zsh_compdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with alternatives}
%{__rm} $RPM_BUILD_ROOT%{_sysconfdir}/alternatives/README
%endif

# packaged as doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/dpkg

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
%attr(755,root,root) %{_sbindir}/dpkg-fsys-usrunmess
%dir %{_sysconfdir}/dpkg
%dir %{_sysconfdir}/dpkg/dpkg.cfg.d

%dir %{_datadir}/dpkg
%{_datadir}/dpkg/abitable
%{_datadir}/dpkg/cputable
%{_datadir}/dpkg/ostable
%{_datadir}/dpkg/tupletable
%{_datadir}/dpkg/*.mk
%{_datadir}/dpkg/*.specs

%dir %{_datadir}/dpkg/sh
%{_datadir}/dpkg/sh/dpkg-error.sh

%dir %{_libexecdir}/dpkg
%attr(755,root,root) %{_libexecdir}/dpkg/dpkg-db-backup
%attr(755,root,root) %{_libexecdir}/dpkg/dpkg-db-keeper

%{perl_vendorlib}/Dpkg.pm
%{perl_vendorlib}/Dpkg

%dir /var/lib/dpkg
%dir /var/lib/dpkg/info
%dir /var/lib/dpkg/parts
%dir /var/lib/dpkg/updates

%{_mandir}/man1/dpkg*.1*
%{_mandir}/man3/Dpkg.3*
%{_mandir}/man3/Dpkg::*.3*
%{_mandir}/man5/deb*.5*
%{_mandir}/man5/dpkg.cfg.5*
%{_mandir}/man5/dsc.5*
%{_mandir}/man7/deb-version.7*
%{_mandir}/man7/dpkg-build-api.7*
%{_mandir}/man8/dpkg-fsys-usrunmess.8.*
%lang(de) %{_mandir}/de/man1/dpkg*.1*
%lang(de) %{_mandir}/de/man5/deb*.5*
%lang(de) %{_mandir}/de/man5/dpkg.cfg.5*
%lang(de) %{_mandir}/de/man5/dsc.5*
%lang(de) %{_mandir}/de/man7/deb-version.7*
%lang(de) %{_mandir}/de/man7/dpkg-build-api.7*
%lang(de) %{_mandir}/de/man8/dpkg-fsys-usrunmess.8.*
%lang(es) %{_mandir}/es/man1/dpkg*.1*
%lang(es) %{_mandir}/es/man5/deb*.5*
%lang(es) %{_mandir}/es/man5/dpkg.cfg.5*
%lang(fr) %{_mandir}/fr/man1/dpkg*.1*
%lang(fr) %{_mandir}/fr/man5/deb*.5*
%lang(fr) %{_mandir}/fr/man5/dpkg.cfg.5*
%lang(fr) %{_mandir}/fr/man5/dsc.5*
%lang(fr) %{_mandir}/fr/man7/deb-version.7*
%lang(fr) %{_mandir}/fr/man8/dpkg-fsys-usrunmess.8.*
%lang(it) %{_mandir}/it/man1/dpkg*.1*
%lang(it) %{_mandir}/it/man5/deb*.5*
%lang(it) %{_mandir}/it/man5/dpkg.cfg.5*
%lang(ja) %{_mandir}/ja/man1/dpkg*.1*
%lang(ja) %{_mandir}/ja/man5/deb*.5*
%lang(ja) %{_mandir}/ja/man5/dpkg.cfg.5*
%lang(nl) %{_mandir}/nl/man1/dpkg*.1*
%lang(nl) %{_mandir}/nl/man5/deb*.5*
%lang(nl) %{_mandir}/nl/man5/dpkg.cfg.5*
%lang(nl) %{_mandir}/nl/man5/dsc.5*
%lang(nl) %{_mandir}/nl/man7/deb-version.7*
%lang(nl) %{_mandir}/nl/man7/dpkg-build-api.7*
%lang(nl) %{_mandir}/nl/man8/dpkg-fsys-usrunmess.8.*
%lang(pl) %{_mandir}/pl/man1/dpkg*.1*
%lang(pl) %{_mandir}/pl/man5/deb*.5*
%lang(pl) %{_mandir}/pl/man5/dpkg.cfg.5*
%lang(pt) %{_mandir}/pt/man1/dpkg*.1*
%lang(pt) %{_mandir}/pt/man5/deb*.5*
%lang(pt) %{_mandir}/pt/man5/dpkg.cfg.5*
%lang(pt) %{_mandir}/pt/man5/dsc.5*
%lang(pt) %{_mandir}/pt/man7/deb-version.7*
%lang(pt) %{_mandir}/pt/man7/dpkg-build-api.7*
%lang(pt) %{_mandir}/pt/man8/dpkg-fsys-usrunmess.8.*
%lang(sv) %{_mandir}/sv/man1/dpkg*.1*
%lang(sv) %{_mandir}/sv/man5/deb*.5*
%lang(sv) %{_mandir}/sv/man5/dpkg.cfg.5*
%lang(sv) %{_mandir}/sv/man5/dsc.5*
%lang(sv) %{_mandir}/sv/man7/deb-version.7*
%lang(sv) %{_mandir}/sv/man7/dpkg-build-api.7*
%lang(sv) %{_mandir}/sv/man8/dpkg-fsys-usrunmess.8.*

%files -n libdpkg-devel
%defattr(644,root,root,755)
%doc doc/README.* doc/*.txt
%{_libdir}/libdpkg.a
%{_includedir}/dpkg
%{_aclocaldir}/dpkg*.m4
%{_pkgconfigdir}/libdpkg.pc
%{_mandir}/man7/libdpkg.7*

%if %{with alternatives}
%files alternatives
%defattr(644,root,root,755)
%dir %{_sysconfdir}/alternatives
%attr(755,root,root) %{_bindir}/update-alternatives
%{_mandir}/man1/update-alternatives.1*
%lang(de) %{_mandir}/de/man1/update-alternatives.1*
%lang(es) %{_mandir}/es/man1/update-alternatives.1*
%lang(fr) %{_mandir}/fr/man1/update-alternatives.1*
%lang(it) %{_mandir}/it/man1/update-alternatives.1*
%lang(ja) %{_mandir}/ja/man1/update-alternatives.1*
%lang(pl) %{_mandir}/pl/man1/update-alternatives.1*
%lang(sv) %{_mandir}/sv/man1/update-alternatives.1*
%dir /var/lib/dpkg/alternatives
%endif

%files -n zsh-completion-dpkg
%defattr(644,root,root,755)
%{zsh_compdir}/_dpkg-parsechangelog
