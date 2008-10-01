Summary:	GeSHi - Generic Syntax Highlighter for PHP
Summary(pl.UTF-8):	GeSHi - ogólna biblioteka PHP do podświetlania składni
Name:		geshi
Version:	1.0.8
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/geshi/%{name}-%{version}.tar.bz2
# Source0-md5:	ad28015b57c4f47eb9fa664d0f9b4fc0
URL:		http://qbnz.com/highlighter/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common
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
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a geshi.php geshi $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{BUGS,CHANGES,README,THANKS,TODO}
%doc docs/geshi-doc.html
%{php_data_dir}/geshi.php
%{php_data_dir}/geshi
