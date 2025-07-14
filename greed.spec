#
Summary:	A logic game with curses-based interface
Summary(pl.UTF-8):	Gra logiczna z interfejsem typu roguelike
Name:		greed
Version:	3.4
Release:	1
License:	BSD-like
Group:		Applications/Games
Source0:	http://www.catb.org/~esr/greed/%{name}-%{version}.tar.gz
# Source0-md5:	d5d254db1e093e0bfb51ad11c35e1093
Patch0:		%{name}-makefile.patch
URL:		http://www.catb.org/~esr/greed/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The object of Greed is to erase as much of the screen as possible by
moving around in a grid of numbers. To move your cursor, simply use
your arrow keys or the the 'hjklyubn' keys or your numberic Your
location is signified by the @ symbol.

%description -l pl.UTF-8
Greed jest grą logiczną typu roguelike. Celem gry jest oczyszczenie
jak największego obszaru, poprzez poruszanie się kursorem po
planszy. Kursorem można sterować za pomocą klawiatury numerycznej
lub klawiszy strzałek. Można również posługiwać się układem
klawiszy w stylu vi. Aktualna pozycja kursora jest reprezentowana,
zgodnie z tradycją gier roguelike, przez symbol @.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} CFLAGS=-I/usr/include/ncurses

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/var/games}
install greed $RPM_BUILD_ROOT%{_bindir}
install greed.6 $RPM_BUILD_ROOT%{_mandir}/man1
touch $RPM_BUILD_ROOT/var/games/greed.scores

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc READ.ME
%attr(2755,root,games) %{_bindir}/greed
%attr(660,root,games) %config(noreplace) %verify(not md5 mtime size) /var/games/greed.scores
%{_mandir}/man1/*
