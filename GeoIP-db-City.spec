Summary:	GeoLite City - City database for GeoIP
Summary(pl.UTF-8):	GeoLite City - baza danych miast dla GeoIP
Name:		GeoIP-db-City
# Updated every month:
Version:	2017.11.06
Release:	1
License:	CC 3.0 BY-SA
Group:		Applications/Databases
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.xz?/GeoLiteCity-%{version}.dat.xz
# Source0-md5:	cde483f8b8bed96d53416f9d442c4ed8
Source1:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/GeoLiteCityv6.dat.gz?/GeoLiteCityv6-%{version}.dat.gz
# Source1-md5:	7ce2a81a13b434ada3c6678ca6a211f1
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
przez MaxMind, dostępne z <http://www.maxmind.com/>.

%prep
%setup -qcT
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

xz -d GeoLiteCity-%{version}.dat.xz
gunzip GeoLiteCityv6-%{version}.dat.gz

%build
# get file DATE in GMT timezone
filedate() {
	TZ=GMT stat -c '%y' "$1" | awk '{print $1}'
}

# use newest file date as version
d1=$(filedate GeoLiteCity-%{version}.dat)
d2=$(filedate GeoLiteCityv6-%{version}.dat)
if [ "$(echo $d1 | tr -d -)" -gt "$(echo $d2 | tr -d -)" ]; then
	d=$d1
else
	d=$d2
fi

ver=$(echo $d | tr - .)
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
