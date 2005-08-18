Summary:	File manager
Summary(pl):	Zarz±dca plików
Name:		rox
Version:	2.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{name}-%{version}.tgz
# Source0-md5:	5cca7bc58af875b88dd9956fda4249f3
Source1:	%{name}.desktop
Patch0:		%{name}-help.patch
URL:		http://rox.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel >= 1:2.0.1
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 2.0.3
Requires:	gtk+2 >= 2.0.1
Requires:	libxml2 >= 2.0.0
Requires:	shared-mime-info >= 0.16
Conflicts:	rox-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
%define		_roxdir %{_libdir}/rox

%description
ROX-Filer is a small, fast and powerful file manager for Linux and
Unix systems.

%description -l pl
ROX-Filer jest ma³ym, szybkim programem do zarz±dzania plikami o
du¿ych mo¿liwo¶ciach przeznaczonym dla Linuksa i innych systemów
uniksowych.

%prep
%setup -q
%patch0 -p1

%build
cd ROX-Filer/src
%{__autoconf}

cd -

mkdir ROX-Filer/build
cd ROX-Filer/build
../src/%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_datadir}/mime/packages \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_iconsdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_roxdir}/ROX-Filer/{Help,Messages} \
	$RPM_BUILD_ROOT/etc/xdg/rox.sourceforge.net

cat >> $RPM_BUILD_ROOT%{_bindir}/rox << 'EOF'
#!/bin/sh
exec %{_roxdir}/ROX-Filer/AppRun "$@"
EOF

install rox.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages

install rox.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install ROX-Filer/.DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox.png

install ROX-Filer/Help/Manual*.html $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer/Help

install ROX-Filer/Messages/*.gmo $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer/Messages

cp -r ROX-Filer/ROX $RPM_BUILD_ROOT%{_iconsdir}

cp -r ROX-Filer/images $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer

install ROX-Filer/AppRun $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer
install ROX-Filer/ROX-Filer $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer

install ROX-Filer/*.{css,xml} $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer

install ROX-Filer/.DirIcon $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer

cp -r Choices/* $RPM_BUILD_ROOT/etc/xdg/rox.sourceforge.net

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/update-mime-database %{_datadir}/mime ||:

%postun
/usr/bin/update-mime-database %{_datadir}/mime

%files
%defattr(644,root,root,755)
%doc ROX-Filer/Help/{Changes,README,TODO}
%lang(es) %doc ROX-Filer/Help/README-es
%attr(755,root,root) %{_bindir}/rox
%dir %{_roxdir}
%dir %{_roxdir}/ROX-Filer
%dir %{_roxdir}/ROX-Filer/Help
%{_roxdir}/ROX-Filer/Help/Manual.html
%lang(fr) %{_roxdir}/ROX-Filer/Help/Manual-fr.html
%lang(it) %{_roxdir}/ROX-Filer/Help/Manual-it.html
%dir %{_roxdir}/ROX-Filer/Messages
%lang(cs) %{_roxdir}/ROX-Filer/Messages/cs.gmo
%lang(da) %{_roxdir}/ROX-Filer/Messages/da.gmo
%lang(de) %{_roxdir}/ROX-Filer/Messages/de.gmo
%lang(es) %{_roxdir}/ROX-Filer/Messages/es.gmo
%lang(et) %{_roxdir}/ROX-Filer/Messages/et_EE.gmo
%lang(eu) %{_roxdir}/ROX-Filer/Messages/eu.gmo
%lang(fi) %{_roxdir}/ROX-Filer/Messages/fi.gmo
%lang(fr) %{_roxdir}/ROX-Filer/Messages/fr.gmo
%lang(hu) %{_roxdir}/ROX-Filer/Messages/hu.gmo
%lang(it) %{_roxdir}/ROX-Filer/Messages/it.gmo
%lang(ja) %{_roxdir}/ROX-Filer/Messages/ja.gmo
%lang(nl) %{_roxdir}/ROX-Filer/Messages/nl.gmo
%lang(no) %{_roxdir}/ROX-Filer/Messages/no.gmo
%lang(pl) %{_roxdir}/ROX-Filer/Messages/pl.gmo
%lang(pt_BR) %{_roxdir}/ROX-Filer/Messages/pt_BR.gmo
%lang(ro) %{_roxdir}/ROX-Filer/Messages/ro.gmo
%lang(ru) %{_roxdir}/ROX-Filer/Messages/ru.gmo
%lang(sv) %{_roxdir}/ROX-Filer/Messages/sv.gmo
%lang(zh_CN) %{_roxdir}/ROX-Filer/Messages/zh_CN.gmo
%lang(zh_TW) %{_roxdir}/ROX-Filer/Messages/zh_TW.gmo
%{_roxdir}/ROX-Filer/images
%attr(755,root,root) %{_roxdir}/ROX-Filer/AppRun
%attr(755,root,root) %{_roxdir}/ROX-Filer/ROX-Filer
%{_roxdir}/ROX-Filer/*.xml
%{_roxdir}/ROX-Filer/*.css
%{_roxdir}/ROX-Filer/.DirIcon
%dir /etc/xdg/rox.sourceforge.net
%dir /etc/xdg/rox.sourceforge.net/MIME-types
%attr(755,root,root) /etc/xdg/rox.sourceforge.net/MIME-types/*
%{_datadir}/mime/packages/rox.xml
%{_desktopdir}/rox.desktop
%{_iconsdir}/ROX
%{_pixmapsdir}/rox.png
%{_mandir}/man1/*
