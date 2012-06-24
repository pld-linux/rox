%define		_name ROX-Filer
%define		_platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	File manager
Summary(pl):	Zarz�dca plik�w
Name:		rox
Version:	2.1.0
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/rox/%{name}-%{version}.tgz
# Source0-md5:	b48089ea846036a1fc6107e0da876f62
Source1:	%{name}.desktop
Patch0:		%{name}-help.patch
URL:		http://rox.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel >= 2.0.1
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 2.0.3
Requires:	gtk+2 >= 2.0.1
Requires:	libxml2 >= 2.0.0
Requires:	shared-mime-info >= 0.11
Conflicts:	rox-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-Filer is a small, fast and powerful file manager for Linux and
Unix systems.

%description -l pl
ROX-Filer jest ma�ym, szybkim programem do zarz�dzania plikami o
du�ych mo�liwo�ciach przeznaczonym dla Linuksa i innych system�w
uniksowych.

%prep
%setup -q
%patch0 -p1

%build
cd ROX-Filer/src
%{__autoconf}
%configure \
	--enable-rox \
	--with-platform="`uname -s`-`echo \"\`uname -m\`\"|sed s/i.86/ix86/`"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appsdir}/%{_name},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_pixmapsdir}/rox,%{_desktopdir}} \
	$RPM_BUILD_ROOT%{_datadir}/{mime/packages,Choices}

ln -sf %{_appsdir}/%{_name}/.DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox.png
ln -s %{_appsdir}/%{_name}/ROX/MIME $RPM_BUILD_ROOT%{_pixmapsdir}/rox

cp -R ROX-Filer/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}
cp -R Choices/* $RPM_BUILD_ROOT%{_datadir}/Choices

install ROX-Filer/.DirIcon $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install rox.xml $RPM_BUILD_ROOT%{_datadir}/mime/packages
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

# start-up script
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
CHOICESPATH=~/Choices:%{_datadir}/Choices; export CHOICESPATH
exec %{_appsdir}/%{_name}/AppRun "\$@"
EOF

echo ".so rox.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ROX-Filer.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_pixmapsdir}/rox/MIME-icons || rm -rf %{_pixmapsdir}/rox/MIME-icons

%post
%{_bindir}/update-mime-database %{_datadir}/mime

%postun
%{_bindir}/update-mime-database %{_datadir}/mime

%files
%defattr(644,root,root,755)
%doc ROX-Filer/Help/{Changes,README,README-es,TODO}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
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
%{_appsdir}/%{_name}/ROX
%dir %{_datadir}/Choices
%dir %{_datadir}/Choices/MIME-types
%attr(755,root,root) %{_datadir}/Choices/MIME-types/*
%{_desktopdir}/rox.desktop
%{_pixmapsdir}/*
%{_datadir}/mime/*
