Summary:	File-manager
Summary(pl):	Menad¿er plików
Name:		rox
Version:	1.1.4
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{name}-%{version}.tgz
URL:		http://rox.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ROX-Filer is a small, fast and powerful filer for Linux and Unix
systems.

%description -l pl
ROX-Filer jest ma³ym, szybkim menad¿erem plików o du¿ych mo¿liwo¶ciach
dla Linuksa i innych uniksów.

%prep
%setup -q

%build
./ROX-Filer/AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_datadir}/ROX-Filer,%{_mandir}/man1}

cp -R ROX-Filer/* $RPM_BUILD_ROOT%{_datadir}/ROX-Filer
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
#ln -s %{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/ROX-Filer.1

# start-up script
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
export CHOICESPATH=%{_datadir}/Choices
exec %{_datadir}/ROX-Filer/Linux-ix86/ROX-Filer
EOF

gzip -9nf ROX-Filer/Help/Changes ROX-Filer/Help/README \
	ROX-Filer/Help/TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%doc ROX-Filer/Help/*.ps ROX-Filer/Help/*.gz
