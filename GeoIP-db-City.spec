Summary:	GeoLite City - City database for GeoIP
Summary(pl.UTF-8):	GeoLite City - baza danych miast dla GeoIP
Name:		GeoIP-db-City
# Updated every month:
Version:	2014.03.05
Release:	1
License:	CC 3.0 BY-SA
Group:		Applications/Databases
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.xz?/GeoLiteCity-%{version}.dat.xz
# Source0-md5:	9f6d3dad3a21c545d5ad02f1573521cd
Source1:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/GeoLiteCityv6.dat.gz?/GeoLiteCityv6-%{version}.dat.gz
# Source1-md5:	4b04a01c82ea61c14c02cbecccb8efd8
URL:		http://dev.maxmind.com/geoip/legacy/geolite/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%setup -qcT
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

xz -d GeoLiteCity-%{version}.dat.xz
gunzip GeoLiteCityv6-%{version}.dat.gz

ver=$(TZ=GMT stat -c '%y' GeoLiteCity-%{version}.dat | awk '{print $1}' | tr - .)
if [ "$ver" != %{version} ]; then
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/GeoIP
cp -p GeoLiteCity-%{version}.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP/GeoLiteCity.dat
ln -s GeoLiteCity.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP/GeoIPCity.dat

cp -p GeoLiteCityv6-%{version}.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP/GeoLiteCityv6.dat
ln -s GeoLiteCityv6.dat $RPM_BUILD_ROOT%{_datadir}/GeoIP/GeoIPCityv6.dat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/GeoIP/*.dat
