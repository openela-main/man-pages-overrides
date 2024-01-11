%global debug_package   %{nil}

Summary: Complementary and updated manual pages
Name: man-pages-overrides
Version: 9.0.0.0
Release: 1%{?dist}
# license is the same as for the man-pages package
License: GPL+ and GPLv2+ and BSD and MIT and Copyright only and IEEE
# there is no public download location for this package
Source: man-pages-overrides-%{version}.tar.xz

Patch0: 1706882-mpo-9.0.0.0-rpc.3.patch

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
* Mon Nov 30 2020 Nikola Forró <nforro@redhat.com> - 9.0.0.0-1
- Initial package for RHEL 9
