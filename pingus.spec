Summary:	Pingus, a lemmings style game with penguins
Summary(pl):	Gra typu lemmingi z pingwinami w roli g³ównej
Name:		pingus
Version:	0.6.0
Release:	0.5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://pingus.seul.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	9cd678272b97dbdb53f42324be31eacd
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
URL:		http://pingus.seul.org/
BuildRequires:	ClanLib-devel >= 0.6.5
BuildRequires:	ClanLib-devel < 0.7.0
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
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cool lemmings game with penguins instead of lemmings!

%description -l pl
Wspania³a gra typu lemmingi z tym, ¿e sterujesz pingwinami!

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/X11R6/include"
%configure \
	--with-clanGL
#	LDFLAGS="-L/usr/X11R6/lib %{rpmldflags}"
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
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/%{name}.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/%{name}.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%lang(sr) %{_datadir}/locale/sr/LC_MESSAGES/%{name}.mo
%lang(tr) %{_datadir}/locale/tr/LC_MESSAGES/%{name}.mo
