%define		php_min_version 5.0.0
Summary:	GeSHi - Generic Syntax Highlighter for PHP
Summary(pl.UTF-8):	GeSHi - ogólna biblioteka PHP do podświetlania składni
Name:		php-geshi
Version:	1.0.9.0
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	https://github.com/GeSHi/geshi-1.0/releases/download/v%{version}/GeSHi-%{version}.tar.bz2
# Source0-md5:	81a2ed8b2e1c28b05ef2badc7583ed45
URL:		http://qbnz.com/highlighter/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php(core) >= %{php_min_version}
Provides:	geshi
Obsoletes:	geshi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeSHi is a generic syntax highlighter, written in PHP. You simply
input the source code you wish to highlight with the language you wish
to use, and the output will be a file syntax highlighted to XHTML
standards.

%description -l pl.UTF-8
GeSHi to ogólna biblioteka podświetlania składni dla PHP. Wystarczy
zaimportować kod źródłowy do podświetlenia w dowolnie wybranym języku,
a na wyjściu powstanie zgodny z XHTML plik z podświetloną składnią.

%prep
%setup -qc
mv geshi .tmp
mv .tmp/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a geshi.php geshi $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/geshi-doc.html
%{php_data_dir}/geshi.php
%{php_data_dir}/geshi
