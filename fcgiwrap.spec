Name:		fcgiwrap
Version:	1.1.0
Release:	1%{?dist}
Summary:	Simple FastCGI wrapper for CGI scripts

Group:		Development/Libraries
License:	BSD-like
URL:		https://github.com/rdempseyidb/fcgiwrap
Source0:	fcgiwrap-1.1.0.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	fcgi-devel
Requires:	fcgi

%description
Simple FastCGI wrapper for CGI scripts


%prep
%setup -q


%build
%configure
make


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/usr/sbin/fcgiwrap
%doc %{_mandir}/man8/fcgiwrap.8.gz



%changelog

