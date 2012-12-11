Name:		vigor
Version:	0.016
Release:	20
Summary:	The popular Unix editor vi with the addition of the Vigor Assistant
License:	GPL
Group:		Editors
URL:		http://vigor.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-48.png
Source2:	%{name}-32.png
Source3:	%{name}-16.png
Patch0:		%{name}.tcltk83.patch
Patch1:		vigor-0.016-tcl86.patch
Requires:	tk
BuildRequires:	termcap-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel

%define debug_package %{nil}

%description
Based on the User Friendly comic strip storyline from 4 January to 14 January
2000, Vigor brings all the features of traditional Unix vi, plus the friendly
and helpful Vigor Assistant. (If you aren't familiar with User Friendly the
Comic Strip, quit bothering with Vigor and go out and look there first. It's
well w orth the trip! Don't worry, we'll wait.) Enter the world of Vigor! Come,
join us, watch the paperclip, don't be afraid...

%prep
%setup -q
%patch0
%patch1 -p1 -b .tcl86

%build
cd build
%configure --enable-curses --enable-db --enable-re
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}
(cd build && %makeinstall)
chmod 755 %{buildroot}%{_bindir}/%{name}
chmod 755 %{buildroot}%{_datadir}/%{name}/recover

# icons
install -D -m 644 %{SOURCE3} %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png 
install -D -m 644 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png

# menu entry

install -d -m 755 %{buildroot}%{_datadir}/applications
cat >  %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=vigor
Comment=The popular Unix editor vi with the addition of the Vigor Assistant
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=true
Type=Application
StartupNotify=false
Categories=TextEditor
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc FAQ LAYOUT LICENSE README README.vigor
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 0.016-19mdv2011.0
+ Revision: 634752
- drop unneeded BR

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.016-18mdv2010.0
+ Revision: 445693
- rebuild

* Sat Dec 06 2008 Adam Williamson <awilliamson@mandriva.org> 0.016-17mdv2009.1
+ Revision: 311006
- rebuild for new tcl
- patch for tcl 8.6
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.016-15mdv2009.0
+ Revision: 255549
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.016-13mdv2008.1
+ Revision: 136570
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
    - import vigor


* Tue Jul 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.016-13mdv2007.0
- xdg menu
- requires tk
- fix menu entry

* Tue Jan 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.016-12mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.016-11mdk 
- better description (Adam Williamson <awilliamson@mandriva.com>)

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.016-10mdk 
- spec cleanup

* Sat Jul 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.016-9mdk 
- fixed menu category
- fixed perms

* Wed May 26 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.016-8mdk
- rebuild
- rpmbuildupdate aware

* Mon Apr 28 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.016-7mdk
- quiet setup
- rm -rf buildroot in %%install, not %%prep
- rebuild against tcl8.4
- rm -rf buildroot in %%clean, not builddir
- remove redundant requires
- fix buildrequires
- updated URL

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.016-6mdk
- rebuild

* Tue Apr 23 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.016-5mdk
- rebuild with latest tcl

* Wed Mar 27 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.016-4mdk
- fixed tcl/tk 8.3 compilation
- used png icons

* Wed Jan 09 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.016-3mdk
- the return of the son of the revenge (and he's angry)
- bzipped icons

* Thu Sep 06 2001 Etienne Faure <etienne@mandrakesoft.com> 0.016-2mdk
- rebuild after testing it. Its worth using it.

* Thu May 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.016-1mdk
- added in contribs by Guillaume Rousse <g.rousse@linux-mandrake.com> :
    - first Mandrake release
