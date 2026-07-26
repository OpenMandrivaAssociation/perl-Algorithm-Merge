%define upstream_name    Algorithm-Merge
Name:		perl-%{upstream_name}
Version:	0.08
Release:	7

Summary:	Implements 3-way merge and diff algorithms
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Algorithm-Merge
Source0:	https://cpan.metacpan.org/authors/id/J/JS/JSMITH/Algorithm-Merge-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::Diff)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 654848
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 471166
- import perl-Algorithm-Merge


* Sun Nov 29 2009 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist
