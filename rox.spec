Summary:	File-manager
Summary(pl):	Menad�er plik�w
Name:		rox
Version:	1.2.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{name}-%{version}.tgz
Patch0:		%{name}-libxml-includes.patch
URL:		http://rox.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libxml2-devel
Requires:	rox-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ROX-Filer is a small, fast and powerful filer for Linux and Unix
systems.

%description -l pl
ROX-Filer jest ma�ym, szybkim menad�erem plik�w o du�ych mo�liwo�ciach
dla Linuksa i innych uniks�w.

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
CHOICESPATH=~/Choices:%{_datadir}/Choices; export CHOICESPATH
exec %{_datadir}/ROX-Filer/AppRun "\$@"
EOF

echo ".so rox.1" >$RPM_BUILD_ROOT%{_mandir}/man1/ROX-Filer.1

gzip -9nf ROX-Filer/Help/Changes ROX-Filer/Help/README \
	ROX-Filer/Help/README-es ROX-Filer/Help/TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ROX-Filer/Help/*.html ROX-Filer/Help/*.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/ROX-Filer/Linux-ix86/*
%attr(755,root,root) %{_datadir}/ROX-Filer/AppRun
%{_mandir}/man1/*
%dir %{_datadir}/ROX-Filer
%{_datadir}/ROX-Filer/*.png
%{_datadir}/ROX-Filer/*.xpm
%{_datadir}/ROX-Filer/*.xml
%{_datadir}/ROX-Filer/*.css
%{_datadir}/ROX-Filer/Styles
%{_datadir}/ROX-Filer/Help/*
%{_datadir}/ROX-Filer/Messages/*
%{_datadir}/ROX-Filer/pixmaps/*
