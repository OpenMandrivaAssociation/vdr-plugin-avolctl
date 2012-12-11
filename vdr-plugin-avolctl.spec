
%define plugin	avolctl
%define name	vdr-plugin-%plugin
%define version	0.3b
%define rel	11

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




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.3b-11mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.3b-10mdv2009.1
+ Revision: 359287
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.3b-9mdv2009.0
+ Revision: 197902
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.3b-8mdv2009.0
+ Revision: 197633
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.3b-7mdv2008.1
+ Revision: 145039
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.3b-6mdv2008.1
+ Revision: 144987
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.3b-5mdv2008.1
+ Revision: 103065
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.3b-4mdv2008.0
+ Revision: 49971
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.3b-3mdv2008.0
+ Revision: 42058
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.3b-2mdv2008.0
+ Revision: 22709
- rebuild for new vdr


* Sun Jan 21 2007 Anssi Hannula <anssi@mandriva.org> 0.3b-1mdv2007.0
+ Revision: 111489
- 0.3b

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.3a-8mdv2007.1
+ Revision: 90893
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.3a-7mdv2007.1
+ Revision: 73953
- rebuild for new vdr
- Import vdr-plugin-avolctl

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.3a-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.3a-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.3a-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.3a-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.3a-2mdv2007.0
- rebuild for new vdr

* Fri Jun 16 2006 Anssi Hannula <anssi@mandriva.org> 0.3a-1mdv2007.0
- initial Mandriva release

