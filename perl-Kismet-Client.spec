#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Kismet
%define	pnam	Client
Summary:	Kismet::Client - Object-oriented module to connect to a Kismet server
#Summary(pl.UTF-8):	
Name:		perl-Kismet-Client
Version:	0.03
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KA/KAYSB/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a81f66327936122df9d518c9deef0bb0
# generic URL, check or change before uncommenting
URL:		http://search.cpan.org/dist/Kismet-Client/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an object-oriented module to connect to a Kismet server created
by Mike Kershaw <dragorn@kismetwireless.net>



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT{%{perl_vendorlib}/%{pdir}/demo.pl,%{_examplesdir}/%{name}-%{version}/}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Kismet
%{perl_vendorlib}/Kismet/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/demo.pl
%{_mandir}/man3/*
