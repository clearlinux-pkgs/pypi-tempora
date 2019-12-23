#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tempora
Version  : 2.0.0
Release  : 18
URL      : https://files.pythonhosted.org/packages/51/ff/0c5d907c38160a6eff9477b411f1b6e7ae9f16d86ba508fd7d1971724180/tempora-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/51/ff/0c5d907c38160a6eff9477b411f1b6e7ae9f16d86ba508fd7d1971724180/tempora-2.0.0.tar.gz
Summary  : Objects and routines pertaining to date and time (tempora)
Group    : Development/Tools
License  : MIT
Requires: tempora-bin = %{version}-%{release}
Requires: tempora-license = %{version}-%{release}
Requires: tempora-python = %{version}-%{release}
Requires: tempora-python3 = %{version}-%{release}
Requires: jaraco.functools
Requires: pytz
BuildRequires : buildreq-distutils3
BuildRequires : jaraco.functools
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytz
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/tempora.svg
:target: https://pypi.org/project/tempora

%package bin
Summary: bin components for the tempora package.
Group: Binaries
Requires: tempora-license = %{version}-%{release}

%description bin
bin components for the tempora package.


%package license
Summary: license components for the tempora package.
Group: Default

%description license
license components for the tempora package.


%package python
Summary: python components for the tempora package.
Group: Default
Requires: tempora-python3 = %{version}-%{release}

%description python
python components for the tempora package.


%package python3
Summary: python3 components for the tempora package.
Group: Default
Requires: python3-core

%description python3
python3 components for the tempora package.


%prep
%setup -q -n tempora-2.0.0
cd %{_builddir}/tempora-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1577143765
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tempora
cp %{_builddir}/tempora-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/tempora/a1474494d96f6ddb3a9a0d767a09871ffc388faf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/calc-prorate

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tempora/a1474494d96f6ddb3a9a0d767a09871ffc388faf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
