%undefine _debugsource_packages
#define pymajor %(rpm -q --qf '%%{VERSION}' python |cut -d. -f1-2)

Summary:	Build system for PyQt and projects that extend it
Name:		python-qt-builder
Version:	1.16.4
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt-builder/pyqt_builder-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python-sip >= 5.0.0
BuildRequires:	python-sip-qt5
BuildRequires:	python%{py_ver}dist(toml)
BuildRequires:	python%{py_ver}dist(setuptools-scm)
BuildSystem:	python

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt.

It extends the sip build system and uses Qt’s qmake to perform the actual
compilation and installation of extension modules.

Projects that use PyQt-builder provide an appropriate pyproject.toml file
and an optional project.py script. Any PEP 517 compliant frontend, for
example sip-install or pip can then be used to build and install the project.

%files
%{_bindir}/pyqt-bundle
%{_bindir}/pyqt-qt-wheel
%{python_sitelib}/PyQt_builder-%{version}*-info
%{python_sitelib}/pyqtbuild/
