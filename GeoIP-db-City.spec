Summary:	GeoLite City - City database for GeoIP
Name:		GeoIP-db-City
# Updated every month:
Version:	2007.08.01
Release:	1
License:	OPEN DATA LICENSE (see LICENSE.txt)
Group:		Applications/Databases
Source0:	http://www.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
# Source0-md5:	04b160944385f4d5989bedef89124a9d
Source1:	http://www.maxmind.com/download/geoip/database/LICENSE.txt
# Source1-md5:	8c0bc6e8ebe6ec3bc1580021edb4bba1
URL:		http://www.maxmind.com/app/geolitecity
BuildArch:	noarch
Requires:	GeoIP-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoIP is a C library that enables the user to find the country that
any IP address or hostname originates from. It uses a file based
database that is accurate as of March 2003. This database simply
contains IP blocks as keys, and countries as values. This database
should be more complete and accurate than using reverse DNS lookups.

GeoLite City is similar to the GeoIP City database, but is not as accurate.
Should you require greater accuracy, GeoIP City is a drop-in replacement
for GeoLite City.

License disclaimer:
This product includes GeoLite data created by MaxMind, available from
http://www.maxmind.com/.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

gunzip GeoLiteCity.dat.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP

install GeoLiteCity.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/GeoIP/*.dat
