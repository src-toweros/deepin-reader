Name:           deepin-reader
Version:        5.7.0.21
Release:        1
Summary:        A simple PDF reader, supporting bookmarks, highlights and annotations
License:        GPLv3+
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: qt5-devel

BuildRequires:  dtkcore-devel
BuildRequires:  dtkwidget-devel
BuildRequires:  dtkgui-devel
BuildRequires: pkgconfig(ddjvuapi)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(cairo)
BuildRequires: openjpeg2-devel
BuildRequires: poppler-qt5-devel
BuildRequires: libspectre-devel
BuildRequires: kf5-karchive-devel
BuildRequires: libtiff-devel

%description
%{summary}.

%prep
%autosetup

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
mkdir build && pushd build
%qmake_qt5 ../ DAPP_VERSION=%{version} DEFINES+="VERSION=%{version}"
%make_build
popd

%install
%make_install -C build INSTALL_ROOT="%buildroot"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jul 07 2021 weidong <weidong@uniontech.com> - 5.7.0.21-1
- Update to 5.7.0.21

* Tue Sep 1 2020 chenbo pan <panchenbo@uniontech.com> - 5.6.9-2
- fix compile fail

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.2-1
- Package init

