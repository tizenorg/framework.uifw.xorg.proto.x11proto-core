Name:       xorg-x11-proto-xproto
Summary:    X.Org X11 Protocol xproto
Version:    7.0.20
Release:    0
Group:      Graphics/X Window System
License:    MIT
URL:        http://www.x.org
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-xproto.manifest 
Provides:   xproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%reconfigure --disable-shared

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%files
%manifest xorg-x11-proto-xproto.manifest
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/xproto.pc
%{_includedir}/X11/*.h
%{_docdir}/xproto/*.xml


