Name:		fcgiwrap
Version:	1.1.0
Release:	1%{?dist}
Summary:	Simple FastCGI wrapper for CGI scripts

Group:		Development/Libraries
License:	FOSS
URL:		https://github.com/gnosek/fcgiwrap
Source0:	fcgiwrap-1.1.0.tar.gz
Patch0:		fcgiwrap-1.1.0.patches
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	fcgi-devel
Requires:	fcgi

%description
Simple FastCGI wrapper for CGI scripts


%prep
%setup -q
%patch0 -p1


%build
#chmod +x %{_builddir}/%{name}-%{version}/configure
chmod +x ./configure
touch ./NEWS ./README ./AUTHORS ./ChangeLog
%configure
make %{?_smp_mflags}


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
# install -d -m 755 /usr/local/sbin
# install -m 755 fcgiwrap /usr/local/sbin
# install -d -m 755 /usr/local/man/man8
# install -m 644 fcgiwrap.8 /usr/local/man/man8


