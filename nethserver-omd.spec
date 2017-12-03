Summary: NethServer omd configuration
Name: nethserver-omd
Version: 0.1.0
Release: 2%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: omd-labs-edition
Requires: check-mk-agent
Requires: nethserver-base

BuildRequires: perl
BuildRequires: nethserver-devtools 

%description
NethServer omd configuration

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sun Dec 03 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-2
- Added require check-mk-agent
* Fri Nov 11 2017 Markus Neuberger <info@markusneuberger.at> - 0.1.0-1
- First NS7 release

