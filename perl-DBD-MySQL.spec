Name:           perl-DBD-MySQL
Version:        4.013
Release:        3%{?dist}
Summary:        A MySQL interface for perl

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DBD-mysql/
Source0:        http://www.cpan.org/authors/id/C/CA/CAPTTOFU/DBD-mysql-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Prevent bug #443495
BuildRequires:  perl(DBI) >= 1.607

BuildRequires:  mysql, mysql-devel, zlib-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl-DBD-mysql = %{version}-%{release}

%description 
An implementation of DBI for MySQL for Perl.


%prep
%setup -q -n DBD-mysql-%{version}
# Correct file permissions
find . -type f | xargs chmod -x

for file in lib/DBD/mysql.pm ChangeLog; do
  iconv -f iso-8859-1 -t utf-8 <$file >${file}_ && mv -f ${file}_ $file
done


%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" --ssl
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
# Full test coverage requires a live MySQL database
# make test


%clean 
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog INSTALL.html README TODO
%{perl_vendorarch}/Bundle/
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/auto/DBD/
%{_mandir}/man3/*.3*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 4.013-3
- rebuild against perl 5.10.1

* Mon Oct 26 2009 Stepan Kasal <skasal@redhat.com> - 4.013-2
- new upstream version

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 4.011-3
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.011-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 Stepan Kasal <skasal@redhat.com> - 4.011-1
- new upstream version
- apply iconv on primary source

* Mon Apr  6 2009 Marcela Mašláňová <mmaslano@redhat.com> - 4.010-1
- update to the latest version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.005-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.005-9
- respin (mysql)

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.005-8
- Rebuild for perl 5.10 (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 4.005-7
- Autorebuild for GCC 4.3

* Mon Jan 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 4.005-6
- rebuild for new perl

* Wed Dec  5 2007 Robin Norwood <rnorwood@redhat.com> - 4.005-5
- Rebuild for new openssl

* Wed Oct 24 2007 Robin Norwood <rnorwood@redhat.com> - 4.005-4
- Fix utf-8 rpmlint warning

* Tue Oct 23 2007 Robin Norwood <rnorwood@redhat.com> - 4.005-3
- Use fixperms macro
- Remove BR: perl

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 4.005-2.1
- add BR: perl(ExtUtils::MakeMaker)

* Fri Aug 24 2007 Robin Norwood <rnorwood@redhat.com> - 4.005-2
- rebuild

* Mon Aug 13 2007 Robin Norwood <rnorwood@redhat.com> - 4.005-1
- New version from CPAN: 4.005

* Thu Jun 07 2007 Robin Norwood <rnorwood@redhat.com> - 4.004-1
- New version from CPAN: 4.004
- Move requires filter into spec file

* Sat Dec 02 2006 Robin Norwood <rnorwood@redhat.com> - 3.0008-1
- New version from CPAN: 3.0008

* Fri Sep 29 2006 Robin Norwood <rnorwood@redhat.com> - 3.0007-1
- Bugzilla: 208633
- Upgrade to upstream version 3.0007 version to fix some minor bugs.

* Mon Jul 17 2006 Jason Vas Dias <jvdias@redhat.com> - 3.0006-1.FC6
- Upgrade to 3.0006

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com>
- rebuild

* Wed May 31 2006 Jason Vas Dias <jvdias@redhat.com> - 3.0004-1.FC6
- upgrade to upstream version 3.0004

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.0002-2.2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0002-2.2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 3.0002-2.2
- rebuild for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Thu Nov 10 2005 Tomas Mraz <tmraz@redhat.com> - 3.0002-2
- rebuilt against new openssl

* Mon Jul 11 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 3.0002-1
- Update to 3.0002.

* Wed Apr 27 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.9007-1
- Update to 2.9007. (#156059)

* Thu Apr 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 2.9006-1
- Update to 2.9006.
- Specfile cleanup. (#154755)

* Thu Nov 25 2004 Miloslav Trmac <mitr@redhat.com> - 2.9004-4
- Convert man page to UTF-8

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Chip Turner <cturner@redhat.com> 2.9003-1
- update to 2.9003

* Mon Jul  7 2003 Chip Turner <cturner@redhat.com> 2.9002-1
- move to 2.9002

* Thu Jul  3 2003 Chip Turner <cturner@redhat.com> 2.1021-5
- rebuild

* Mon Jan 27 2003 Chip Turner <cturner@redhat.com>
- version bump and rebuild

* Wed Jan  1 2003 Chip Turner <cturner@redhat.com>
- turn ssl on and allow Makefile.PL to yse mysql_config to find proper link flags
- update to 2.1021

* Sat Dec 14 2002 Chip Turner <cturner@redhat.com>
- don't use internal rpm dep generator

* Wed Nov 20 2002 Chip Turner <cturner@redhat.com>
- rebuild

* Wed Aug  7 2002 Trond Eivind GlomsrÃ¸d <teg@redhat.com> 2.1017-3
- Rebuild

* Tue Jun 25 2002 Trond Eivind GlomsrÃ¸d <teg@redhat.com> 2.1017-2
- Rebuild, to fix #66304

* Wed Jun  5 2002 Trond Eivind GlomsrÃ¸d <teg@redhat.com> 2.1017-1
- New version - no longer integrated into msql-mysql modules

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Feb 22 2002 Trond Eivind GlomsrÃ¸d <teg@redhat.com> 1.2219-6
- Rebuild

* Fri Feb  8 2002 Chip Turner <cturner@minbar.devel.redhat.com>
- filter out "soft" dependencies: perl(Data::ShowTable)

* Thu Feb  7 2002 Trond Eivind GlomsrÃ¸d <teg@redhat.com> 1.2219-4
- Rebuild

* Tue Jan 22 2002 Trond Eivind GlomsrÃ¸d <teg@redhat.com> 1.2219-3
- Rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jan  8 2002 Trond Eivind GlomsrÃ¸d <teg@redhat.com> 1.2219-1
- 1.2219

* Fri Jul 20 2001 Trond Eivind GlomsrÃ¸d <teg@redhat.com>
- Add zlib-devel to buildrequires (#49536)

* Sun Jul  1 2001 Trond Eivind GlomsrÃ¸d <teg@redhat.com>
- Add perl and perl-DBI to BuildRequires

* Wed May 30 2001 Trond Eivind GlomsrÃ¸d <teg@redhat.com>
- Change Group to Applications/Databases

* Tue May  1 2001 Trond Eivind GlomsrÃ¸d <teg@redhat.com>
- 1.2216
- Add doc files
- Minor cleanups

* Thu Nov 30 2000 Trond Eivind GlomsrÃ¸d <teg@redhat.com>
- First cut
