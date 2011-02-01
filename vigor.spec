Name:		vigor
Version:	0.016
Release:	%{mkrel 19}
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
BuildRequires:	libtermcap-devel
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
