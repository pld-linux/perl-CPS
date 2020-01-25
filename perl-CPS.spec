#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	CPS
%define		pnam	CPS
Summary:	CPS - manage flow of control in Continuation-Passing Style
Summary(pl.UTF-8):	CPS - zarządzanie przepływem sterowania w stylu przekazywania kontynuacji
Name:		perl-CPS
Version:	0.12
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PE/PEVANS/%{pnam}-%{version}.tar.gz
# Source0-md5:	2c69c2fd383ee8f3cdc850681b39211d
URL:		http://search.cpan.org/dist/CPS/
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Identity
BuildRequires:	perl-Test-Refcount
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CPS module allows to manage flow of control in Continuation-Passing
Style.

%description -l pl.UTF-8
Moduł CPS pozwala na zarządzanie przepływem sterowania w stylu
przekazywania kontynuacji (Continuation Passing).

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
%{_mandir}/man3/CPS*.3pm*
