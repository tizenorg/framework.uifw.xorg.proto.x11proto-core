Name:     xorg-x11-proto-core
Summary:  X.Org X11 Protocol xproto
Version:  7.0.31
Release:  2
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.gz
Provides: xproto

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)
BuildRequires: python

# some file to be intalled can be ignored when rpm generates packages
%define _unpackaged_files_terminate_build 0

%description
Description: %{summary}

%prep
%setup -q
export TIZEN_PROFILE="%{?tizen_profile_name}"

%build
./autogen.sh
%reconfigure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%remove_docs

mkdir -p %{buildroot}/opt/var/xkb
%if "%{?tizen_profile_name}" == "mobile"
  cp -rf keylayout/tizen_layout_mobile.txt %{buildroot}/opt/var/xkb/tizen_key_layout.txt
%else
  %if "%{?tizen_profile_name}" == "wearable"
    cp -rf keylayout/tizen_layout_wearable.txt %{buildroot}/opt/var/xkb/tizen_key_layout.txt
  %else
    %if "%{?tizen_profile_name}" == "tv"
      cp -rf keylayout/tizen_layout_tv.txt %{buildroot}/opt/var/xkb/tizen_key_layout.txt
    %endif
  %endif
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_includedir}/X11/*.h
%{_datadir}/pkgconfig/*.pc
/opt/var/xkb/tizen_key_layout.txt
