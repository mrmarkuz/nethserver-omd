Summary: NethServer OMD
Name: nethserver-omd
Version: 0.0.1
Release: 4%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: omd-labs-edition, check-mk-agent, nethserver-base, xinetd
BuildRequires: nethserver-devtools 

%description
NethServer Open Monitoring Distribution

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
* Sat Jan 24 2017 Markus Neuberger <info@markusneuberger.at> - 0.0.1-4
- Add to backup
- Tidy up
- Edit README
* Mon Dec 04 2017 Markus Neuberger <info@markusneuberger.at> - 0.0.1-3
- Tidy up spec and createlinks
- Added require xinetd
- Create and restart site
- Added installation and documentation to README
- Added xinetd restart
* Sun Dec 03 2017 Markus Neuberger <info@markusneuberger.at> - 0.0.1-2
- Added require check-mk-agent
* Fri Nov 10 2017 Markus Neuberger <info@markusneuberger.at> - 0.0.1-1
- First NS7 release
