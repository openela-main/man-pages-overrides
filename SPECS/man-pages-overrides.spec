%global debug_package   %{nil}

Summary: Complementary and updated manual pages
Name: man-pages-overrides
Version: 8.9.0.0
Release: 1%{?dist}
# license is the same as for the man-pages package
License: GPL+ and GPLv2+ and BSD and MIT and Copyright only and IEEE
Group: Documentation
# there is no public download location for this package
Source: man-pages-overrides-%{version}.tar.xz

Patch1: 1673142-mpo-8.2.0.0-copy_file_range.2.patch
Patch2: 1517305-mpo-8.2.0.1-jose-.1.patch
Patch3: 1828296-mpo-8.3.0.0-xattr.7.patch
Patch4: 1829031-mpo-8.3.0.0-execve.2.patch
Patch5: 1731058-mpo-8.3.0.1-radvd.8.patch
Patch6: 1850065-mpo-8.3.0.2-sgdisk.8.patch
Patch7: 1899552-mpo-8.5.0.0-statx.2.patch
Patch8: 1928160-mpo-8.5.0.0-resolv.conf.5.patch
Patch9: 1981853-mpo-8.5.0.1-tcp.7.patch
Patch10: 2184023-mpo-8.9.0.0-resolv.conf.5.patch

BuildArch: noarch

# make sure man-pages-overrides is installed with man-pages
Supplements: man-pages

%description
A collection of manual ("man") pages to complement other packages or update
those contained therein. Always have the latest version of this package
installed.

%prep
%autosetup -p1
# remove unwanted *.orig files
find -name "*.orig" -delete

%build
# nothing to build

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/overrides
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
for i in *; do
    if [[ -d "$i" ]]; then
        for j in $(ls "$i"); do
           if [[ -d "$i/$j" ]]; then
               mkdir -p "$RPM_BUILD_ROOT%{_mandir}/overrides/$j"
               for k in $(ls "$i/$j"); do
                   if [[ -d "$i/$j/$k" ]]; then
                       mkdir -p "$RPM_BUILD_ROOT%{_mandir}/overrides/$j/$k"
                       cp -f "$i/$j/$k"/* "$RPM_BUILD_ROOT%{_mandir}/overrides/$j/$k"
                   else
                       cp -f "$i/$j"/* "$RPM_BUILD_ROOT%{_mandir}/overrides/$j"
                   fi
               done
           else
              mkdir -p "$RPM_BUILD_ROOT%{_docdir}/%{name}/$i"
              cp "$i/$j" "$RPM_BUILD_ROOT%{_docdir}/%{name}/$i"
           fi
        done
    fi
done

%files
%doc %{_docdir}/%{name}
%{_mandir}/overrides/

%changelog
* Wed Apr 12 2023 Lukas Javorsky <ljavorsk@redhat.com> - 8.9.0.0-1
- Upload new tarball
- resolv.conf.5: Add option no-aaaa
  resolves: #2184023

* Thu Feb 03 2022 Nikola Forró <nforro@redhat.com> - 8.6.0.0-1
- Upload new tarball
- rpc.3: remove the man page
  resolves: #2042972

* Fri Jul 16 2021 Nikola Forró <nforro@redhat.com> - 8.5.0.1-1
- Upload new tarball
- tcp.7: remove tcp_tso_win_divisor option
  resolves: #1981853

* Fri Jul 09 2021 Nikola Forró <nforro@redhat.com> - 8.5.0.0-1
- Upload new tarball
- statx.2: add STATX_ATTR_DAX
  resolves: #1899552
- resolv.conf.5: update information about search list and
  attempt to clarify domain/search interaction
  resolves: #1928160

* Thu Aug 20 2020 Nikola Forró <nforro@redhat.com> - 8.3.0.2-2
- xattr.7: add attr(1) and selinux(8) as relevant pages to SEE ALSO
  related: #1828296

* Thu Jun 25 2020 Nikola Forró <nforro@redhat.com> - 8.3.0.2-1
- Upload new tarball
- sgdisk.8: fix typo
  resolves: #1850065

* Mon Jun 15 2020 Nikola Forró <nforro@redhat.com> - 8.3.0.1-1
- Upload new tarball
- radvd.8: add nodaemon option
  resolves: #1731058

* Thu Apr 30 2020 Nikola Forró <nforro@redhat.com> - 8.3.0.0-1
- Upload new tarball
- Use unversioned docdir
  resolves: #1824824
- xattr.7: add attr(1) as a relevant page to SEE ALSO
  resolves: #1828296
- execve.2: clarify signal sent to the process on late failure
  resolves: #1829031

* Thu Dec 19 2019 Nikola Forró <nforro@redhat.com> - 8.2.0.2-1
- Upload new tarball
- kernel_lockdown.7: add missing .RE macro
  related: #1781945

* Wed Dec 18 2019 Nikola Forró <nforro@redhat.com> - 8.2.0.1-1
- Upload new tarball
- jose-*.1: fix typographical errors
  resolves: #1517305

* Fri Dec 13 2019 Nikola Forró <nforro@redhat.com> - 8.2.0.0-1
- Upload new tarball
- kernel_lockdown.7: add new manpage
  resolves: #1781945
- copy_file_range.2: update ERRORS
  resolves: #1673142

* Wed Jun 19 2019 Nikola Forró <nforro@redhat.com> - 8.1.0.0-2
- Mark this package as man-pages supplement
  related: #1706882

* Wed May 29 2019 Nikola Forró <nforro@redhat.com> - 8.1.0.0-1
- Upload new tarball
- rpc.3: indicate that <rpc/rpc.h> is provided by libtirpc-devel, not glibc
  resolves: #1706882

* Thu Jul 26 2018 Nikola Forró <nforro@redhat.com> - 8.0.0-1
- Initial package for RHEL 8.0
