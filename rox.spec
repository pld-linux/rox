%define _appsdir /usr/X11R6/share/ROX-apps
%define _name ROX-Filer
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	File-manager
Summary(pl):	Menad¿er plików
Name:		rox
Version:	1.3.1
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/rox/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-fix-mime-info-path.patch
URL:		http://rox.sourceforge.net/
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	gtk+2 >= 2.0.0
Requires:	libxml2 >= 2.0.0
Requires:	shared-mime-info
Conflicts: rox-base
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appsdir}/%{_name},%{_mandir}/man1}
install -d $RPM_BUILD_ROOT{%{_pixmapsdir}/rox,%{_applnkdir}/Utilities}
install -d $RPM_BUILD_ROOT%{_datadir}/{mime-info,Choices}

ln -sf %{_appsdir}/%{_name}/.DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox.png
ln -sf %{_datadir}/Choices/MIME-icons $RPM_BUILD_ROOT%{_pixmapsdir}/rox
cp -R ROX-Filer/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}
cp -R Choices/* $RPM_BUILD_ROOT%{_datadir}/Choices
install ROX-Filer/.DirIcon $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install rox.mimeinfo $RPM_BUILD_ROOT%{_datadir}/mime-info
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

# start-up script
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
CHOICESPATH=~/Choices:%{_datadir}/Choices; export CHOICESPATH
exec %{_appsdir}/%{_name}/AppRun "\$@"
EOF

echo ".so rox.1" >$RPM_BUILD_ROOT%{_mandir}/man1/ROX-Filer.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities/

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_pixmapsdir}/rox/MIME-icons || rm -rf %{_pixmapsdir}/rox/MIME-icons

%files
%defattr(644,root,root,755)
%doc ROX-Filer/Help/{Changes,README,README-es,TODO}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_appsdir}/%{_name}/Linux*
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%{_mandir}/man1/*
%dir %{_appsdir}
%dir %{_appsdir}/%{_name}
%dir %{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/*.png
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/*.css
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/Help/*html
%{_appsdir}/%{_name}/Messages
%{_appsdir}/%{_name}/images
%dir %{_datadir}/Choices
%{_datadir}/Choices/MIME-icons
%dir %{_datadir}/Choices/MIME-types
%attr(755,root,root) %{_datadir}/Choices/MIME-types/*
%{_applnkdir}/Utilities/*
%{_pixmapsdir}/*
%{_datadir}/mime-info/*
