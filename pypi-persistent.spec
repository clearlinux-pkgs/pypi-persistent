#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-persistent
Version  : 4.9.2
Release  : 72
URL      : https://files.pythonhosted.org/packages/4e/48/0df545cca6280920c2175851416ef45c7dfd3c4f52aba7b8657a0f197340/persistent-4.9.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/48/0df545cca6280920c2175851416ef45c7dfd3c4f52aba7b8657a0f197340/persistent-4.9.2.tar.gz
Summary  : Translucent persistent objects
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-persistent-filemap = %{version}-%{release}
Requires: pypi-persistent-lib = %{version}-%{release}
Requires: pypi-persistent-license = %{version}-%{release}
Requires: pypi-persistent-python = %{version}-%{release}
Requires: pypi-persistent-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cffi)
BuildRequires : pypi(py)
BuildRequires : pypi(zope.interface)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
BuildRequires : python3-dev

%description
===========================================================
``persistent``:  automatic persistence for Python objects
===========================================================

%package dev
Summary: dev components for the pypi-persistent package.
Group: Development
Requires: pypi-persistent-lib = %{version}-%{release}
Provides: pypi-persistent-devel = %{version}-%{release}
Requires: pypi-persistent = %{version}-%{release}

%description dev
dev components for the pypi-persistent package.


%package filemap
Summary: filemap components for the pypi-persistent package.
Group: Default

%description filemap
filemap components for the pypi-persistent package.


%package lib
Summary: lib components for the pypi-persistent package.
Group: Libraries
Requires: pypi-persistent-license = %{version}-%{release}
Requires: pypi-persistent-filemap = %{version}-%{release}

%description lib
lib components for the pypi-persistent package.


%package license
Summary: license components for the pypi-persistent package.
Group: Default

%description license
license components for the pypi-persistent package.


%package python
Summary: python components for the pypi-persistent package.
Group: Default
Requires: pypi-persistent-python3 = %{version}-%{release}

%description python
python components for the pypi-persistent package.


%package python3
Summary: python3 components for the pypi-persistent package.
Group: Default
Requires: pypi-persistent-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(persistent)
Requires: pypi(cffi)
Requires: pypi(zope.interface)

%description python3
python3 components for the pypi-persistent package.


%prep
%setup -q -n persistent-4.9.2
cd %{_builddir}/persistent-4.9.2
pushd ..
cp -a persistent-4.9.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667844037
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-persistent
cp %{_builddir}/persistent-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-persistent/a0b53f43aab58b46bf79ba756c50771c605ab4c5 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.11/persistent/cPersistence.h
/usr/include/python3.11/persistent/ring.h

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-persistent

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-persistent/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
