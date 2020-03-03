Summary:	Build system for PyQt and projects that extend it
Name:		python-qt-builder
Version:	1.2.0
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		http://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt-builder/PyQt-builder-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-sip >= 1:5.0.0
BuildRequires:	python-sip-qt5
BuildRequires:	python3dist(toml)
BuildArch:	noarch

%description
PyQt-builder is the PEP 517 compliant build system for PyQt and projects that
extend PyQt.

It extends the sip build system and uses Qt’s qmake to perform the actual
compilation and installation of extension modules.

Projects that use PyQt-builder provide an appropriate pyproject.toml file
and an optional project.py script. Any PEP 517 compliant frontend, for
example sip-install or pip can then be used to build and install the project.

%files -f %{name}.list
%{py_puresitedir}/pyqtbuild/__pycache__
%{py_puresitedir}/pyqtbuild/bundle/__pycache__
%{py_puresitedir}/pyqtbuild/bundle/packages/__pycache__

#------------------------------------------------------------
%prep
%autosetup -p1 -n PyQt-builder-%{version}

%build
%setup_compile_flags

export LDFLAGS="%{ldflags} -lpython3.8"

python setup.py \
	build

%install
python setup.py \
	install \
	--root="%{buildroot}" \
	--record="%{name}.list"

%check
python setup.py \
	check
