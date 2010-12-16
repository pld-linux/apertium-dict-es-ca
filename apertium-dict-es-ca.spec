Summary:	Spanish-Catalan language pair for Apertium
Summary(pl.UTF-8):	Para języków hiszpański-kataloński dla Apertium
%define	lpair	es-ca
Name:		apertium-dict-%{lpair}
Version:	1.2.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	0cc9676a152947adf703ec81b67654bf
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-apertium32.patch
URL:		http://www.apertium.org/
BuildRequires:	apertium-devel >= 3.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox >= 3.2.0
BuildRequires:	pkgconfig
Requires:	apertium >= 3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an Apertium language pair, which can be used for translating
between Spanish and Catalan, morphological analysis or part-of-speech
tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między hiszpańskim a katalońskim, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apertium/modes

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed here (see modes subdir) and contain wrong (builddir) paths
%{__rm} $RPM_BUILD_ROOT%{_datadir}/apertium/apertium-%{lpair}/*.mode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/ca-es.mode
%{_datadir}/apertium/modes/ca-es-multi.mode
%{_datadir}/apertium/modes/es-ca.mode
%{_datadir}/apertium/modes/es-ca-multi.mode
%{_datadir}/apertium/modes/es-ca_valencia.mode
%{_datadir}/apertium/modes/val-ca-es.mode
%{_datadir}/apertium/modes/val-es-ca.mode
