Summary:	Pingus, a lemmings style game with penguins
Summary(pl):	Gra typu lemmingi z pingwinami w roli g��wnej
Name:		pingus
Version:	0.5.0pre3
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dark.x.dtu.dk/~grumbel/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-Clanlib-0.6.1.patch
Patch2:		%{name}-amfix.patch
Patch3:		%{name}-acfix.patch
Patch4:		%{name}-gcc3.patch
Patch5:		%{name}-data-typos.patch
Patch6:		%{name}-info.patch
URL:		http://pingus.seul.org/
BuildRequires:	ClanLib-devel >= 0.6.1
BuildRequires:	Hermes-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel > 1.2.1
BuildRequires:	glib-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A cool lemmings game with penguins instead of lemmings!

%description -l pl
Wspania�a gra typu lemmings z tym, �e sterujesz pingwinami!

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/X11R6/include -I/usr/include/libxml2/libxml"
%configure \
	CPPFLAGS="$CPPFLAGS" \
	LDFLAGS="-L/usr/X11R6/lib %{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

mv -f $RPM_BUILD_ROOT%{_datadir}/games/pingus $RPM_BUILD_ROOT%{_datadir}/pingus

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog CREDITS FAQ NEWS TODO THANKS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_infodir}/*.info*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
