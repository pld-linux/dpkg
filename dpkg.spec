Summary:	Package maintenance system for Debian Linux
Summary(pl.UTF-8):	Program do obsługi pakietów Debiana
Name:		dpkg
Version:	1.14.29
Release:	1
License:	GPL
Group:		Applications/File
Source0:	ftp://ftp.debian.org/debian/pool/main/d/dpkg/%{name}_%{version}.tar.gz
# Source0-md5:	4326172a959b5b6484b4bc126e9f628d
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	perl-tools-pod
BuildRequires:	zlib-devel
Requires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the programs which handle the installation and
removal of packages on your system.

The primary interface for the dpkg suite is the `dselect' program; a
more low-level and less user-friendly interface is available in the
form of the `dpkg' command.

In order to unpack and build Debian source packages you will need to
install the developers' package `dpkg-dev' as well as this one.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do obsługi pakietów deb znanych z
Debiana.

%prep
%setup -q

%build
%configure \
	--enable-shared \
	--without-dselect \
	--without-start-stop-daemon \
	--with-zlib \
	--with-bz2 \
	--with-selinux \
	--with-admindir=/var/lib/%{name} \
	SELINUX_LIBS=-lselinux

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_mandir}/{,*/}man5/dselect.cfg.5
rm -f $RPM_BUILD_ROOT%{_mandir}/{,*/}man1/dselect.1
rm -f $RPM_BUILD_ROOT%{_mandir}/{,*/}man8/start-stop-daemon.8
rm -f $RPM_BUILD_ROOT%{_mandir}/{,*/}man8/cleanup-info.8
rm -f $RPM_BUILD_ROOT%{_mandir}/{,*/}man8/install-info.8
rm -f $RPM_BUILD_ROOT%{_sbindir}/cleanup-info
rm -f $RPM_BUILD_ROOT%{_sbindir}/install-info
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/alternatives/README

%find_lang dpkg

%clean
rm -rf $RPM_BUILD_ROOT

%files -f dpkg.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/822-date
%attr(755,root,root) %{_bindir}/dpkg*

%attr(755,root,root) %{_sbindir}/dpkg-divert
%attr(755,root,root) %{_sbindir}/update-alternatives

%dir %{_sysconfdir}/dpkg
%dir %{_sysconfdir}/dpkg/origins
%{_sysconfdir}/dpkg/origins/debian

%dir %{_libdir}/dpkg
%dir %{_libdir}/dpkg/parsechangelog
%attr(755,root,root) %{_libdir}/dpkg/mksplit
%dir %{_libdir}/dpkg/parsechangelog
%attr(755,root,root) %{_libdir}/dpkg/parsechangelog/debian

%attr(755,root,root) %{_sbindir}/dpkg-statoverride

%dir %{_datadir}/dpkg
%{_datadir}/dpkg/cputable
%{_datadir}/dpkg/ostable
%{_datadir}/dpkg/triplettable
%{perl_vendorlib}/*.pm
%{perl_vendorlib}/Dpkg

%dir /var/lib/dpkg
/var/lib/dpkg/*

%{_mandir}/man1/822*
%{_mandir}/man5/deb*
%{_mandir}/man8/update*
%{_mandir}/man*/dpkg*
%lang(de) %{_mandir}/de/man1/822*
%lang(de) %{_mandir}/de/man5/deb*
%lang(de) %{_mandir}/de/man8/update*
%lang(de) %{_mandir}/de/man*/dpkg*
%lang(fr) %{_mandir}/fr/man1/822*
%lang(fr) %{_mandir}/fr/man5/deb*
%lang(fr) %{_mandir}/fr/man8/update*
%lang(fr) %{_mandir}/fr/man*/dpkg*
%lang(hu) %{_mandir}/hu/man*/dpkg*
%lang(ja) %{_mandir}/ja/man5/deb*
%lang(ja) %{_mandir}/ja/man8/update*
%lang(pl) %{_mandir}/pl/man1/822*
%lang(pl) %{_mandir}/pl/man5/deb*
%lang(pl) %{_mandir}/pl/man8/update*
%lang(pl) %{_mandir}/pl/man*/dpkg*
%lang(sv) %{_mandir}/sv/man1/822*
%lang(sv) %{_mandir}/sv/man5/deb*
%lang(sv) %{_mandir}/sv/man*/dpkg*
%lang(sv) %{_mandir}/sv/man8/update*
