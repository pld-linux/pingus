Summary:	Pingus, a lemmings style game with penguins
Summary(pl):	Gra typu lemmingi z pingwinami w roli g��wnej
Name:		pingus
Version:	0.5.0pre2
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dark.x.dtu.dk/~grumbel/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
URL:		http://pingus.seul.org/
BuildRequires:	ClanLib-devel >= 0.5.0
BuildRequires:	Hermes-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_mixer-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel > 1.2.1
BuildRequires:	glib-devel
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

%build
./autogen.sh || :
install -d  data/images/buttons/
touch data/images/buttons/Makefile.in
%configure \
	CPPFLAGS="-I%{_includedir}" \
	LDFLAGS="-L%{_libdir} %{rpmldflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

mv $RPM_BUILD_ROOT/%{_datadir}/games/pingus $RPM_BUILD_ROOT/%{_datadir}/pingus

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/%{name}
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.desktop

gzip -9nf AUTHORS BUGS ChangeLog CREDITS FAQ NEWS TODO THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
