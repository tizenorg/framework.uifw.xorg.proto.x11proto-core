Name:       xorg-x11-proto-xproto
Summary:    X.Org X11 Protocol xproto
Version:    7.0.20
Release:    0
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/xproto-%{version}.tar.gz
Provides:   xproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure --disable-shared

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%files
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/xproto.pc
%{_includedir}/X11/*.h
%{_docdir}/xproto/*.xml


