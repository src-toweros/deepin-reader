%bcond_with check

%global with_debug 1
%if 0%{?with_debug}
%global debug_package   %{nil}
%endif

Name:           deepin-reader
Version:        5.6.2
Release:        1
Summary:        Document Viewer is a simple PDF reader, supporting bookmarks, highlights and annotations.
License:        GPLv3+
URL:            https://uos-packages.deepin.com/uos/pool/main/d/deepin-reader/
Source0:        %{name}-%{version}.orig.tar.xz

BuildRequires: qt5-qtbase-devel
BuildRequires: dtkwidget-devel
BuildRequires: kf5-karchive-devel
BuildRequires: qt5-linguist
BuildRequires: poppler-qt5
BuildRequires: poppler-qt5-devel
BuildRequires: poppler
BuildRequires: poppler-devel
BuildRequires: djvulibre-devel
BuildRequires: djvulibre-libs
BuildRequires: libspectre-devel
BuildRequires: libspectre
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libtiff
BuildRequires: libtiff-devel
BuildRequires: libuuid-devel
BuildRequires: libuuid

%description
Document Viewer is a simple PDF reader, supporting bookmarks, highlights and annotations.


%prep
%autosetup

%build
sed -i '/^SUBDIRS/,$d' deepin_reader.pro
echo 'SUBDIRS += \' >>  deepin_reader.pro
echo '    DBService \' >>  deepin_reader.pro
echo '    ModelService \' >>  deepin_reader.pro
echo '    application' >>  deepin_reader.pro

export PATH=$PATH:/usr/lib64/qt5/bin
mkdir build && cd build
%{_libdir}/qt5/bin/qmake ..
%{__make}

%install
pushd %{_builddir}/%{name}-%{version}/build
%make_install INSTALL_ROOT=%{buildroot}
popd

mkdir -p %{?buildroot}%{_libdir}
mv %{?buildroot}//usr/lib/* %{?buildroot}%{_libdir}

%files
%{_bindir}/deepin-reader
%{_libdir}/*
%{_datadir}/applications/deepin-reader.desktop
%{_datadir}/deepin-reader/translations/deepin-reader_en_US.qm
%{_datadir}/deepin-reader/translations/deepin-reader_zh_CN.qm
%{_datadir}/icons/hicolor/scalable/apps/deepin-reader.svg

%doc README.md

%changelog
* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.6.2-1
- Package init
