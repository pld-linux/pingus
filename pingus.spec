Summary:	Pingus, a lemmings style game with penguins
Summary(pl.UTF-8):	Gra typu lemmingi z pingwinami w roli głównej
Summary(pt_BR.UTF-8):	Um clone de lemmings com pingüins
Name:		pingus
Version:	0.7.6
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://pingus.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	561798686f34d3fa4e69135d655f47ac
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-opt.patch
Patch1:		%{name}-gcc4.patch
URL:		http://pingus.seul.org/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	boost-devel >= 1.36.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.385
BuildRequires:	scons
BuildRequires:	xorg-lib-libXi-devel
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
#%%patch1 -p1

# note: it loads *.po files directly, no need to use msgfmt
mv -f data/po/sr{,@latin}.po
rm -f data/po/pingus.pot

%build
export CXXFLAGS="%{rpmcxxflags} -std=c++0x" 
%scons with_xinput=true

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install	%{name} $RPM_BUILD_ROOT%{_bindir}
cp -r data $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/pingus
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
