Summary:	Pingus, a lemmings style game with penguins
Summary(pl.UTF-8):   Gra typu lemmingi z pingwinami w roli głównej
Summary(pt_BR.UTF-8):   Um clone de lemmings com pingüins
Name:		pingus
Version:	0.6.0
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://pingus.seul.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	9cd678272b97dbdb53f42324be31eacd
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-assert.patch
Patch2:		%{name}-locale_names.patch
Patch3:		%{name}-types.patch
URL:		http://pingus.seul.org/
BuildRequires:	ClanLib-MikMod-devel
BuildRequires:	ClanLib-Vorbis-devel
BuildRequires:	ClanLib-devel >= 0.6.5
BuildRequires:	ClanLib-devel < 0.7.0
BuildRequires:	Hermes-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A cool lemmings game with penguins instead of lemmings!

%description -l pl.UTF-8
Wspaniała gra typu lemmingi z tym, że steruje się pingwinami!

%description -l pt_BR.UTF-8
Pingus é um clone do jogo Lemmings, com a diferença de que você guia 
pingüins.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/sr{,@Latn}.po

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/X11R6/include"
%configure \
	--with-clanGL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

mv -f $RPM_BUILD_ROOT%{_datadir}/games/pingus $RPM_BUILD_ROOT%{_datadir}/pingus

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
