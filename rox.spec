Summary:	File manager
Summary(pl.UTF-8):	Zarządca plików
Name:		rox
Version:	2.11
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/rox-filer-%{version}.tar.bz2
# Source0-md5:	0eebf05a67f7932367750ebf9faf215d
Source1:	%{name}.desktop
Patch0:		%{name}-help.patch
Patch1:		%{name}-linking.patch
URL:		http://rox.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	shared-mime-info >= 0.14
BuildRequires:	xorg-lib-libSM-devel
Requires:	glib2 >= 2.0.3
Requires:	gtk+2 >= 2:2.4.0
Requires:	libxml2 >= 2.0.0
Requires(post,postun):	shared-mime-info >= 0.14
Conflicts:	rox-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
%define		_roxdir %{_libdir}/rox

%description
ROX-Filer is a small, fast and powerful file manager for Linux and
Unix systems.

%description -l pl.UTF-8
ROX-Filer jest małym, szybkim programem do zarządzania plikami o
dużych możliwościach przeznaczonym dla Linuksa i innych systemów
uniksowych.

%prep
%setup -q -n rox-filer-%{version}
%patch -P0 -p1
%patch -P1 -p1

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
	$RPM_BUILD_ROOT%{_localedir} \
	$RPM_BUILD_ROOT%{_datadir}/mime/packages \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_iconsdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir} \
	$RPM_BUILD_ROOT%{_roxdir}/ROX-Filer/Help \
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

cp -r ROX-Filer/ROX $RPM_BUILD_ROOT%{_iconsdir}

cp -r ROX-Filer/images $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer

install ROX-Filer/AppRun $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer
install ROX-Filer/ROX-Filer $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer

install ROX-Filer/*.{css,xml} $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer

install ROX-Filer/.DirIcon $RPM_BUILD_ROOT%{_roxdir}/ROX-Filer
cp -r ROX-Filer/Messages/* $RPM_BUILD_ROOT%{_localedir}

%{__rm} $RPM_BUILD_ROOT%{_localedir}/README
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{et_EE,no,pt_PT}


%find_lang ROX-Filer

cp -r Choices/* $RPM_BUILD_ROOT/etc/xdg/rox.sourceforge.net

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files -f ROX-Filer.lang
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
