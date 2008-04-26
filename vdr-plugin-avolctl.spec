
%define plugin	avolctl
%define name	vdr-plugin-%plugin
%define version	0.3b
%define rel	8

Summary:	VDR plugin: Alsa Volume Control
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://martins-kabuff.de/avolctl.html
Source:		http://martins-kabuff.de/download/vdr-%plugin-%version.tar.bz2
Patch0:		avolctl-0.3b-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	libalsa-devel
Requires:	vdr-abi = %vdr_abi

%description
This plugin controls selectable volume controls if your soundcard depending on
the volume control of VDR. It is also possible to select controls and switches
that can be controlled within the settings menu. This is for example useful for
tone control.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


