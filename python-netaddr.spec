%define module netaddr

Name:           python-%module
Version:        1.3.0
Release:        2
License:        BSD3c
Summary:        Pythonic manipulation of IPv4, IPv6, CIDR, EUI and MAC network addresses
Url:            https://pypi.org/project/netaddr/
Group:          Development/Python
#Source:         https://github.com/downloads/drkjam/netaddr/netaddr-%{version}.tar.gz
Source:		https://files.pythonhosted.org/packages/source/n/netaddr/netaddr-%{version}.tar.gz
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

%build
%py_build

%install
%py_install

%files
%{_bindir}/%module
%{py_puresitedir}/*
