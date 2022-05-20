#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-tempora
Version  : 5.0.1
Release  : 47
URL      : https://files.pythonhosted.org/packages/57/bf/f22c888ae5aec050ab013d1eadf90e0793741ea64dd205ae35f3281bc77f/tempora-5.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/57/bf/f22c888ae5aec050ab013d1eadf90e0793741ea64dd205ae35f3281bc77f/tempora-5.0.1.tar.gz
Summary  : Objects and routines pertaining to date and time (tempora)
Group    : Development/Tools
License  : MIT
Requires: pypi-tempora-bin = %{version}-%{release}
Requires: pypi-tempora-license = %{version}-%{release}
Requires: pypi-tempora-python = %{version}-%{release}
Requires: pypi-tempora-python3 = %{version}-%{release}
Requires: pypi(jaraco.functools)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jaraco.functools)
BuildRequires : pypi(py)
BuildRequires : pypi(pytz)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://img.shields.io/pypi/v/tempora.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/tempora.svg
:target: `PyPI link`_

%package bin
Summary: bin components for the pypi-tempora package.
Group: Binaries
Requires: pypi-tempora-license = %{version}-%{release}

%description bin
bin components for the pypi-tempora package.


%package license
Summary: license components for the pypi-tempora package.
Group: Default

%description license
license components for the pypi-tempora package.


%package python
Summary: python components for the pypi-tempora package.
Group: Default
Requires: pypi-tempora-python3 = %{version}-%{release}

%description python
python components for the pypi-tempora package.


%package python3
Summary: python3 components for the pypi-tempora package.
Group: Default
Requires: python3-core
Provides: pypi(tempora)
Requires: pypi(jaraco.functools)
Requires: pypi(pytz)

%description python3
python3 components for the pypi-tempora package.


%prep
%setup -q -n tempora-5.0.1
cd %{_builddir}/tempora-5.0.1
pushd ..
cp -a tempora-5.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653058222
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tempora
cp %{_builddir}/tempora-5.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tempora/8e6689d37f82d5617b7f7f7232c94024d41066d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/calc-prorate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tempora/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
