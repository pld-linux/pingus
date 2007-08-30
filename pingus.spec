# TODO:
# - xorg deps
# - install po files in proper directory (needed?)
# - are we need post and postun sections?

Summary:	Pingus, a lemmings style game with penguins
Summary(pl.UTF-8):	Gra typu lemmingi z pingwinami w roli głównej
Summary(pt_BR.UTF-8):	Um clone de lemmings com pingüins
Name:		pingus
Version:	0.7.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://pingus.seul.org/files/%{name}-%{version}.tar.bz2
# Source0-md5:	d967a3c233aa094236eb2ce6a3e20dd8
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://pingus.seul.org/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	boost-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	physfs-devel
BuildRequires:	sed >= 4.0
BuildRequires:	scons
Requires:	guile
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

mv -f data/po/sr{,@Latn}.po

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install	%{name} $RPM_BUILD_ROOT%{_bindir}
cp -r data $RPM_BUILD_ROOT%{_datadir}/%{name}

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
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
