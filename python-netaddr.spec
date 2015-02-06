%define module netaddr

Name:           python-%module
Version:        0.7.10
Release:        2
License:        BSD3c
Summary:        Pythonic manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses
Url:            http://code.google.com/p/netaddr
Group:          Development/Python
Source:         https://github.com/downloads/drkjam/netaddr/netaddr-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildArch:      noarch

%description
A pure Python network address representation and manipulation library.

netaddr provides a Pythonic way of working with:
    - IPv4 and IPv6 addresses and subnets (including CIDR notation);
    - MAC (Media Access Control) addresses in multiple formats;
    - IEEE EUI-64, OUI and IAB identifiers;
    - a user friendly IP glob-style format.

Included are routines for:
    - generating, sorting and summarizing IP addresses;
    - converting IP addresses and ranges between various different formats;
    - performing set based operations on groups of IP addresses and subnets;
    - arbitrary IP address range calculations and conversions;
    - querying IEEE OUI and IAB organisational information;
    - querying of IP standards related data from key IANA data sources.

%prep
%setup -q -n %module-%{version}
chmod -x AUTHORS CHANGELOG COPYRIGHT README LICENSE THANKS # remove executable bit from docs

%build
CFLAGS="%{optflags}" python setup.py build

%install
%{__python} setup.py install --root %{buildroot} --install-purelib=%{py_puresitedir}

%clean

%files
%doc AUTHORS CHANGELOG COPYRIGHT README LICENSE THANKS
%{_bindir}/%module
%{py_puresitedir}/*



%changelog
* Wed Jun 08 2011 Antoine Ginies <aginies@mandriva.com> 0.7.5-1mdv2011.0
+ Revision: 683258
- import python-netaddr


* Wed Jun 8 2011 Antoine Ginies <aginies@mandriva.com> 0.7.5
- first release for Mandriva 

