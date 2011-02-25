# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CPS
%define		pnam	CPS
Summary:	CPS - manage flow of control in Continuation-Passing Style
Name:		perl-CPS
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/%{pnam}-%{version}.tar.gz
# Source0-md5:	e4f36f053f538a6fa1ea4ed1de038f9e
URL:		http://search.cpan.org/dist/CPS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPS - manage flow of control in Continuation-Passing Style.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/CPS.pm
%{perl_vendorlib}/CPS
%{_mandir}/man3/CPS*.3*
