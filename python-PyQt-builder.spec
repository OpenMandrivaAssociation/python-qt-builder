%undefine _debugsource_packages

Summary:	Build system for PyQt and projects that extend it
Name:		python-PyQt-builder
Version:	1.19.1
Release:	2
Group:		Development/Python
License:	BSD-2-Clause
Url:		https://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt-builder/pyqt_builder-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python-sip >= 5.0.0
BuildRequires:	python-sip-qt5
BuildRequires:	python%{pyver}dist(build)
BuildRequires:	python%{pyver}dist(toml)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python
# Renamed 2025/12/01 after 6.0
%rename python-qt-builder

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt.

It extends the sip build system and uses Qt’s qmake to perform the actual
compilation and installation of extension modules.

Projects that use PyQt-builder provide an appropriate pyproject.toml file
and an optional project.py script. Any PEP 517 compliant frontend, for
example sip-install or pip can then be used to build and install the project.

%prep -a
# Apparently the tarball is missing some metadata to find the correct
# version number, so it goes with 0.0.0 unless we force something else
sed -i -e 's,dynamic = \["version"\],version = "%{version}",' pyproject.toml

%files
%{_bindir}/pyqt-bundle
%{_bindir}/pyqt-qt-wheel
%{python_sitelib}/pyqt_builder-%{version}*-info
%{python_sitelib}/pyqtbuild/
