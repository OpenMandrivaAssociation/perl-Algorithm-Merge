%define upstream_name    Algorithm-Merge
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Implements 3-way merge and diff algorithms
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Algorithm/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Algorithm::Diff)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
