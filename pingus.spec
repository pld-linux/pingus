Summary:	Pingus, a lemmings style game with penguins.
Summary(pl):	Gra typu lemmingi z pingwinami w roli g³ównej.
Name:		pingus
Version:	20010311
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	cvs://anonymous@dark.x.dtu.dk:/usr/local/cvsroot:Games/Pingus/Pingus-%{version}.tar.gz
URL:		http://pingus.seul.org/
BuildRequires:	gtk+-devel > 1.2.1
BuildRequires:	glib-devel
BuildRequires:	XFree86-devel
BuildRequires:	gettext-devel
BuildRequires:	SDL-devel
BuildRequires:	ClanLib-devel >= 0.5.0
BuildRequires:	libxml-devel
BuildRequires:	Hermes-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A cool lemmings game with penguins instead of lemmings! 

%description -l pl
Wspania³a gra typu lemmings z tym, ¿e sterujemy pingwinami!

%prep
%setup -q -n Pingus-%{version}

%build
./autogen.sh || :
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS BUGS ChangeLog CREDITS FAQ NEWS TODO WISHLIST

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man*/*
