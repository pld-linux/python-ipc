
%define         module	ipc

Summary:	Python module implementing inter-process communication
Summary(pl):	Modu³ Pythona implementuj±cy komunikacjê miêdzyprocesow±
Name:		python-%{module}
Version:	0.0.1
Release:	1
License:	GNU
Group:		Development/Languages/Python
Source0:	http://www.heiho.net/python-ipc/python-ipc.tar.gz
# Source0-md5:	af8a8e6b69dc8cd9240bafb1824f5f34
Patch0:		%{name}-pld.patch
URL:		http://www.heiho.net/python-ipc/
BuildRequires:	python-devel >= 2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	swig
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module implementing inter-process communication.

%description -l pl
Modu³ Pythona implementuj±cy komunikacjê miêdzyprocesow±.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CFLAGS

%{__make}
python -c "import compiler;compiler.compileFile('ipc.py')"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install ipc.pyc _ipc.so $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitedir}/%{module}.pyc
%attr(755,root,root) %{py_sitedir}/_%{module}.so
