#
# Conditional build:
%bcond_with debug
#
Summary:	DOS/UNIX text file conversion tool
Summary(pl.UTF-8):	Narzędzie do konwersji plików tekstowych między formatami DOS i UNIX
Name:		tofrodos
Version:	1.7.6
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://tofrodos.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	518b32d041879702e883f651c77c0fcc
URL:		http://www.thefreecountry.com/tofrodos/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DOS text files traditionally have CR/LF (carriage return/line feed)
pairs as their new line delimiters while Unix text files traditionally
have LFs (line feeds) to terminate each line.

tofrodos comprises two programs, "fromdos" and "todos", which convert
text files to and from these formats. Use "fromdos" to convert DOS
text files to the Unix format, and "todos" to convert Unix text files
to the DOS format.

%description -l pl.UTF-8
W systemach z rodziny DOS/Windows końce linii w plikach tekstowych są
tradycyjnie oznaczane przez CR/LF (powrót karetki / nowa linia).
Wynika to z braku elementarnej obsługi drukarek w systemie DOS. W
systemach UNIX końce linii są oznaczane przez LF.

tofrodos jest zestawem dwóch narzędzi "fromdos" i "todos", które służą
do konwersji plików tekstowych między tymi formatami. Program
"fromdos" służy do konwersji plików z formatu DOSa do formatu UNIXa,
natomiast "todos" służy do konwersji z formatu UNIXa do formatu DOSa.

%prep
%setup -c -q

%build
%{__make} -C src/ \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -c" \
	LDFLAGS="%{rpmldflags}" \
	%{?with_debug:DEBUG=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install src/fromdos $RPM_BUILD_ROOT%{_bindir}
install src/fromdos.1 $RPM_BUILD_ROOT%{_mandir}/man1

ln -sf fromdos $RPM_BUILD_ROOT%{_bindir}/todos

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt tofrodos.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
