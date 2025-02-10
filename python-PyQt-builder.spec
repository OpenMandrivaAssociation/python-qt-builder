Name:		python-PyQt-builder
Version:	1.18.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt-builder/pyqt_builder-%{version}.tar.gz
Summary:	The PEP 517 compliant PyQt build system
URL:		https://pypi.org/project/PyQt-builder/
License:	BSD-2-Clause
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildArch:	noarch

%description
The PEP 517 compliant PyQt build system

%prep
%autosetup -p1 -n pyqt_builder-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/*
%{py_sitedir}/pyqtbuild
%{py_sitedir}/PyQt_builder-*.*-info
