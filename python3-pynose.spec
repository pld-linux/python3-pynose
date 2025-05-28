Summary:	pynose - an updated version of nose
Summary(pl.UTF-8):	pynose - uaktualniona wesja nose
Name:		python3-pynose
Version:	1.5.4
Release:	3
License:	LGPL v2.1
Group:		Libraries/Python
Source0:	https://pypi.debian.net/pynose/pynose-%{version}.tar.gz
# Source0-md5:	f9ee9d97377b9d9132dcff559f811710
URL:		https://pypi.org/project/pynose/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:68.0.0
BuildRequires:	python3-wheel >= 0.42
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.7
Obsoletes:	python3-nose < %{version}-%{release}
Provides:	python3-nose = %{version}-%{release}
Provides:	python%{py3_ver}dist(nose) = %{version}-%{release}
Conflicts:	python-nose < 1.3.7-15
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pynose fixes nose to extend unittest and make testing easier.

%description -l pl.UTF-8
pynose poprawia nose, aby rozszerzyć możliwości modułu unittest i
ułatwić testowanie.

%prep
%setup -q -n pynose-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

ln -sf nosetests $RPM_BUILD_ROOT%{_bindir}/nosetests-%{py3_ver}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.md
%attr(755,root,root) %{_bindir}/nosetests
%attr(755,root,root) %{_bindir}/nosetests-%{py3_ver}
%attr(755,root,root) %{_bindir}/pynose
%{py3_sitescriptdir}/nose
%{py3_sitescriptdir}/pynose-%{version}.dist-info
