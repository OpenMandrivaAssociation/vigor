%define name    vigor
%define version 0.016
%define release %mkrel 13

%define title       Vigor
%define longtitle   The popular Unix editor vi with the addition of the Vigor Assistant

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    The popular Unix editor vi with the addition of the Vigor Assistant
License:    GPL
Group:      Editors
Url:        http://vigor.sourceforge.net/
Source0:    http://heanet.dl.sourceforge.net/sourceforge/vigor/%{name}-%{version}.tar.bz2
Source1:    %{name}-48.png.bz2
Source2:    %{name}-32.png.bz2
Source3:    %{name}-16.png.bz2
Patch:      %{name}.tcltk83.patch.bz2
Requires:       tk
BuildRequires:  libtermcap-devel
BuildRequires:  tcl tcl-devel
BuildRequires:  tk tk-devel
BuildRequires:  XFree86-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Based on the User Friendly comic strip storyline from 4 January to 14 January
2000, Vigor brings all the features of traditional Unix vi, plus the friendly
and helpful Vigor Assistant. (If you aren't familiar with User Friendly the
Comic Strip, quit bothering with Vigor and go out and look there first. It's
well w orth the trip! Don't worry, we'll wait.) Enter the world of Vigor! Come,
join us, watch the paperclip, don't be afraid...

%prep
%setup -q
bzcat %{SOURCE1} > %{name}-16.png
bzcat %{SOURCE2} > %{name}-32.png
bzcat %{SOURCE3} > %{name}-48.png
%patch

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
install -D -m 644 %{name}-16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D -m 644 %{name}-32.png %{buildroot}%{_iconsdir}/%{name}.png 
install -D -m 644 %{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png

# menu entry
install -d -m 755 %{buildroot}%{_menudir}/menu
cat >%{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}):\\
    command="%{_bindir}/%{name}"\\
    needs="text"\\
    icon="%{name}.png"\\
    section="More Applications/Editors"\\
    title="%{title}" \
    longtitle="%{longtitle}" \
    xdg="true"
EOF

install -d -m 755 %{buildroot}%{_datadir}/applications
cat >  %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{title}
Comment=%{longtitle}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=true
Type=Application
StartupNotify=false
Categories=TextEditor
EOF

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root)
%doc FAQ LAYOUT LICENSE README README.vigor
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

