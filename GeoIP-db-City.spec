Summary:	GeoLite City - City database for GeoIP
Summary(pl.UTF-8):	GeoLite City - baza danych miast dla GeoIP
Name:		GeoIP-db-City
# Updated every month:
Version:	2009.11.02
Release:	1
License:	OPEN DATA LICENSE (see LICENSE.txt)
Group:		Applications/Databases
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
# Source0-md5:	d90b9ee5a8ee2d6d29f58b6e5dbcede8
Source1:	http://www.maxmind.com/download/geoip/database/LICENSE.txt
# Source1-md5:	a1381bd1aa0a0c91dc31b3f1e847cf4a
URL:		http://www.maxmind.com/app/geolitecity
Requires:	GeoIP-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Determine country, state/region, city, US postal code, US area code,
metro code, latitude, and longitude information for IP addresses
worldwide.

License disclaimer: this product includes GeoLite data created by
MaxMind, available from <http://www.maxmind.com/>.

%description -l pl.UTF-8
Znajdź państwo, stan/region, miasto, kod pocztowy, kod regionu, kod
miejski, szerokość i wysokość geograficzną dla adresów IP z całego
świata.

Informacja licencyjna: ten produkt zawiera dane GeoLite stworzone
przez MaxWind, dostępne z <http://www.maxwind.com/>.

%prep
%setup -q -c -T
cp %{SOURCE0} .
cp %{SOURCE1} .

gunzip GeoLiteCity.dat.gz

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP

install GeoLiteCity.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP
ln -s   GeoLiteCity.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP/GeoIPCity.dat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/GeoIP/*.dat
