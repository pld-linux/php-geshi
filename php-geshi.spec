Summary:	GeSHi - Generic Syntax Highlighter for PHP
Summary(pl.UTF-8):	GeSHi - ogólna biblioteka PHP do podświetlania składni
Name:		geshi
Version:	1.0.7.20
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/geshi/GeSHi-%{version}.tar.bz2
# Source0-md5:	22e57bf1936319ad07423fd32fa3a78a
URL:		http://qbnz.com/highlighter/
Requires:	php-dirs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir	/usr/share/php

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
install -d $RPM_BUILD_ROOT%{_phpdir}
cp -a geshi.php geshi $RPM_BUILD_ROOT%{_phpdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{BUGS,CHANGES,README,THANKS,TODO}
%doc docs/geshi-doc.txt
%{_phpdir}/geshi.php
%{_phpdir}/geshi
