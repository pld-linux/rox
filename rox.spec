%define		_name ROX-Filer
%define		_platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	File manager
Summary(pl):	Zarz±dca plików
Name:		rox
Version:	2.0.0
Release:	1
License:	GPL
Group:		X11/Applications
# Source0-md5:	895c6aa5890bb7e1f624a3cf65b457d4
Source0:	http://dl.sourceforge.net/rox/%{name}-%{version}.tgz
Source1:	%{name}.desktop
Patch0:		%{name}-fix-mime-info-path.patch
Patch1:		%{name}-help.patch
URL:		http://rox.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	gdk-pixbuf-devel
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
ROX-Filer jest ma³ym, szybkim programem do zarz±dzania plikami o
du¿ych mo¿liwo¶ciach przeznaczonym dla Linuksa i innych systemów
uniksowych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
	$RPM_BUILD_ROOT{%{_pixmapsdir}/rox,%{_applnkdir}/Utilities} \
	$RPM_BUILD_ROOT%{_datadir}/{mime-info,Choices}

ln -sf %{_appsdir}/%{_name}/.DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox.png
ln -sf %{_datadir}/Choices/MIME-icons $RPM_BUILD_ROOT%{_pixmapsdir}/rox

cp -R ROX-Filer/* $RPM_BUILD_ROOT%{_appsdir}/%{_name}
cp -R Choices/* $RPM_BUILD_ROOT%{_datadir}/Choices

install ROX-Filer/.DirIcon $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install rox.xml $RPM_BUILD_ROOT%{_datadir}/mime-info
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

# start-up script
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} << EOF
#!/bin/sh
CHOICESPATH=~/Choices:%{_datadir}/Choices; export CHOICESPATH
exec %{_appsdir}/%{_name}/AppRun "\$@"
EOF

echo ".so rox.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ROX-Filer.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities/

%clean
rm -rf $RPM_BUILD_ROOT

%pre
test -h %{_pixmapsdir}/rox/MIME-icons || rm -rf %{_pixmapsdir}/rox/MIME-icons

%post
%{_bindir}/update-mime-database %{_datadir}/mime-info

%postun
%{_bindir}/update-mime-database %{_datadir}/mime-info

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
%dir %{_datadir}/Choices
%{_datadir}/Choices/MIME-icons
%dir %{_datadir}/Choices/MIME-types
%attr(755,root,root) %{_datadir}/Choices/MIME-types/*
%{_applnkdir}/Utilities/*
%{_pixmapsdir}/*
%{_datadir}/mime-info/*
