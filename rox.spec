Summary:	File-manager
Summary(pl):	Menad¿er plików
Name:		rox
Version:	1.1.12
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{name}-%{version}.tgz
Patch0: %{name}-configfix.patch
URL:		http://rox.sourceforge.net/
BuildRequires: gtk+-devel
BuildRequires: gdk-pixbuf-devel
BuildRequires: libxml-devel
Requires: rox-base
Requires: gtk+ >= 1.2.0
Requires: gdk-pixbuf
Requires: libxml
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
%patch0 -p1

%build
./ROX-Filer/AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_datadir}/ROX-Filer,%{_mandir}/man1}

cp -R ROX-Filer/* $RPM_BUILD_ROOT%{_datadir}/ROX-Filer
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

# start-up script
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
export CHOICESPATH=%{_datadir}/Choices
exec %{_datadir}/ROX-Filer/AppRun "\$@"
EOF

gzip -9nf ROX-Filer/Help/Changes ROX-Filer/Help/README \
	ROX-Filer/Help/README-es ROX-Filer/Help/TODO 

%post
ln -s %{_mandir}/man1/%{name}.1.gz %{_mandir}/man1/ROX-Filer.1.gz

%postun
rm -f %{_mandir}/man1/ROX-Filer.1.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/ROX-Filer/Linux-ix86/*
%attr(755,root,root) %{_datadir}/ROX-Filer/AppRun
%{_mandir}/man1/*
%{_datadir}/ROX-Filer/*.png
%{_datadir}/ROX-Filer/*.xpm
%{_datadir}/ROX-Filer/*.xml
%{_datadir}/ROX-Filer/*.css
%{_datadir}/ROX-Filer/Styles
%{_datadir}/ROX-Filer/Help/*
%{_datadir}/ROX-Filer/Messages/*
%{_datadir}/ROX-Filer/pixmaps/*
%doc ROX-Filer/Help/*.html ROX-Filer/Help/*.gz
