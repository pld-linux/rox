Summary:	File manager
Summary(pl):	Zarz±dca plików
Name:		rox
Version:	2.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{name}-%{version}.tgz
# Source0-md5:	0deefd9e7edd4e79cd0f18f423264ebb
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
Requires:	shared-mime-info >= 0.12-2
Conflicts:	rox-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)

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

%configure \
	--with-platform=%{_platform}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d \
	$RPM_BUILD_ROOT%{_bindir} \
	$RPM_BUILD_ROOT%{_datadir}/%{name} \
	$RPM_BUILD_ROOT%{_datadir}/mime/packages \
	$RPM_BUILD_ROOT%{_mandir}/man1 \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_iconsdir} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

install ROX-Filer/%{_platform}/ROX-Filer $RPM_BUILD_ROOT%{_bindir}

install ROX-Filer/*.{css,xml} $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -R ROX-Filer/{Help,Messages,images} $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -R Choices/MIME-types $RPM_BUILD_ROOT%{_datadir}/%{name}

install rox.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages

cp -R ROX-Filer/ROX $RPM_BUILD_ROOT%{_iconsdir}

install ROX-Filer/.DirIcon $RPM_BUILD_ROOT%{_datadir}/%{name}
install ROX-Filer/.DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox.png

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so rox.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ROX-Filer.1

# Preparing start-up script
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh

if [ -n "\$HOME_ETC" ]; then
	USERCHOICES=\$HOME_ETC/.%{name}
else
	USERCHOICES=~/.%{name}
fi
		
export CHOICESPATH=\$USERCHOICES:%{_datadir}/%{name}

export APP_DIR=%{_datadir}/%{name}

exec %{_bindir}/ROX-Filer "\$@"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/update-mime-database %{_datadir}/mime

%postun
%{_bindir}/update-mime-database %{_datadir}/mime

%files
%defattr(644,root,root,755)
%doc ROX-Filer/Help/{Changes,README,TODO}
%lang(es) %doc ROX-Filer/Help/README-es
%attr(755,root,root) %{_bindir}/ROX-Filer
%attr(755,root,root) %{_bindir}/rox
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/Help
%{_datadir}/%{name}/Help/Manual.html
%lang(fr) %{_datadir}/%{name}/Help/Manual-fr.html
%lang(it) %{_datadir}/%{name}/Help/Manual-it.html
%dir %{_datadir}/%{name}/Messages
%lang(cs) %{_datadir}/%{name}/Messages/cs.gmo
%lang(da) %{_datadir}/%{name}/Messages/da.gmo
%lang(de) %{_datadir}/%{name}/Messages/de.gmo
%lang(es) %{_datadir}/%{name}/Messages/es.gmo
%lang(fi) %{_datadir}/%{name}/Messages/fi.gmo
%lang(fr) %{_datadir}/%{name}/Messages/fr.gmo
%lang(hu) %{_datadir}/%{name}/Messages/hu.gmo
%lang(it) %{_datadir}/%{name}/Messages/it.gmo
%lang(ja) %{_datadir}/%{name}/Messages/ja.gmo
%lang(nl) %{_datadir}/%{name}/Messages/nl.gmo
%lang(nb) %{_datadir}/%{name}/Messages/no.gmo
%lang(pl) %{_datadir}/%{name}/Messages/pl.gmo
%lang(pt_BR) %{_datadir}/%{name}/Messages/pt_BR.gmo
%lang(ru) %{_datadir}/%{name}/Messages/ru.gmo
%lang(ro) %{_datadir}/%{name}/Messages/ro.gmo
%lang(sv) %{_datadir}/%{name}/Messages/sv.gmo
%lang(zh_CN) %{_datadir}/%{name}/Messages/zh_CN.gmo
%lang(zh_TW) %{_datadir}/%{name}/Messages/zh_TW.gmo
%{_datadir}/%{name}/images
%{_datadir}/%{name}/*.xml
%{_datadir}/%{name}/*.css
%{_datadir}/%{name}/.DirIcon
%dir %{_datadir}/%{name}/MIME-types
%attr(755,root,root) %{_datadir}/%{name}/MIME-types/*
%{_datadir}/mime/packages/rox.xml
%{_desktopdir}/rox.desktop
%{_iconsdir}/ROX
%{_pixmapsdir}/rox.png
%{_mandir}/man1/*
