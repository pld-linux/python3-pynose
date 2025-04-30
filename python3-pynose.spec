# Conditional build:
%bcond_with	doc	# API documentation
%bcond_with	tests	# unit tests

%define		module	nose
%define		pyname	pynose
Summary:	pynose is an updated version of nose, originally made by Jason Pellerin
Name:		python3-%{pyname}
Version:	1.5.4
Release:	3
License:	LGPL
Group:		Libraries/Python
Source0:	https://pypi.debian.net/%{pyname}/%{pyname}-%{version}.tar.gz
# Source0-md5:	f9ee9d97377b9d9132dcff559f811710
URL:		https://pypi.org/project/pynose/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-wheel >= 0.42
%if %{with tests}
#BuildRequires:	python3-
#BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.2
Obsoletes:	python3-nose < %{version}-%{release}
Provides:	python3-nose = %{version}-%{release}
Provides:	python%{py3_ver}dist(nose) = %{version}-%{release}
Conflicts:	python-nose < 1.3.7-15
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pynose fixes nose to extend unittest and make testing easier.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n %{pyname}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
%{__python3} -m zipfile -e build-3/*.whl build-3-test
# use explicit plugins list for reliable builds (delete PYTEST_PLUGINS if empty)
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS= \
%{__python3} -m pytest -o pythonpath="$PWD/build-3-test" tests
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
rm -rf docs/_build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/nosetests
%attr(755,root,root) %{_bindir}/pynose
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{pyname}-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
