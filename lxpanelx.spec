%define int_name lxpanel

Summary:	Lightweight X11 desktop panel based on fbpanel
Name:	  	lxpanelx
Version:	0.5.6
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%int_name-%version.tar.gz
Source1:	volume_icon.tar.gz
Patch0:		lxpanel-0.5.0-customization.patch
Patch3:		batt_status.patch
Patch4:		configure_desktop_number.patch
Patch8:		missing_glades.patch
Patch9:		redefine-alarm-variable.patch
Patch10:	lxpanel-icons.patch
Patch11:	lxpanel-0.5.6-volumeicon.patch
Patch12:	lxpanel-0.5.6-clock.patch

URL:		http://code.google.com/p/lxpanelx/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+2-devel libalsa-devel intltool
BuildRequires:	menu-cache-devel >= 0.2.1
BuildRequires:	docbook-to-man libwnck-1-devel docbook-dtd412-xml
Requires:	desktop-common-data obconf
Suggests:	pcmanfm
Conflicts:	lxpanel

%description
LXPanelx is a fork lightweight X11 desktop panel. It's consist more flexible 
taskbar plugin configurations and other  many improvements, not in original lxpanel.

%package devel
Summary: Development files for lxpanel
Group: Graphical desktop/Other

%description devel
This package contains development files needed for building lxde plugins.

%prep
%setup -q -n %int_name-%version -a1
%patch0 -p0
%patch3 -p1
%patch4 -p1
%patch8 -p1
#patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
./autogen.sh
%configure2_5x \
  --with-plugins="volumealsa cpu deskno batt kbled xkb thermal"
  
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{int_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{int_name}.lang
%defattr(-, root, root)
%{_bindir}/%{int_name}
%{_bindir}/lxpanelctl
%dir %{_libdir}/%int_name
%dir %{_libdir}/%{int_name}/plugins
%{_libdir}/%{int_name}/plugins/batt.so
%{_libdir}/%{int_name}/plugins/cpu.so
#{_libdir}/%{int_name}/plugins/cpufreq.so
%{_libdir}/%{int_name}/plugins/deskno.so
%{_libdir}/%{int_name}/plugins/kbled.so
%{_libdir}/%{int_name}/plugins/volumealsa.so
%{_libdir}/%{int_name}/plugins/xkb.so
%{_libdir}/%{int_name}/plugins/thermal.so
%{_datadir}/%int_name
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/lxpanel
%{_libdir}/pkgconfig/lxpanel.pc
