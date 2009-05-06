Summary:	GeoLite City - City database for GeoIP
Summary(pl.UTF-8):	GeoLite City - baza danych miast dla GeoIP
Name:		GeoIP-db-City
# Updated every month:
Version:	2009.05.03
Release:	1
License:	OPEN DATA LICENSE (see LICENSE.txt)
Group:		Applications/Databases
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
# Source0-md5:	a7e6c29b6c0daf4e5c79601fe0ab083d
Source1:	http://www.maxmind.com/download/geoip/database/LICENSE.txt
# Source1-md5:	a1381bd1aa0a0c91dc31b3f1e847cf4a
URL:		http://www.maxmind.com/app/geolitecity
Requires:	GeoIP-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GeoIP is a C library that enables the user to find the country that
any IP address or hostname originates from. It uses a file based
database that is accurate as of March 2003. This database simply
contains IP blocks as keys, and countries as values. This database
should be more complete and accurate than using reverse DNS lookups.

GeoLite City is similar to the GeoIP City database, but is not as
accurate. Should you require greater accuracy, GeoIP City is a drop-in
replacement for GeoLite City.

License disclaimer: this product includes GeoLite data created by
MaxMind, available from <http://www.maxmind.com/>.

%description -l pl.UTF-8
GeoIP jest biblioteką napisaną w C umożliwiającą użytkownikowi
odnalezienie państwa, z którego pochodzi dany adres IP lub domena.
Używa do tego zapisanej w pliku bazy danych (z marca 2003). W bazie
tej adresy IP są kluczami, a państwa wartościami. Powinna ona być
dokładniejsza niż sprawdzanie odwrotnego DNS. 

GeoLite City jest podobna do bazy danych GeoIP City, ale nie jest tak
dokładna. Jeśli wymagana jest większa dokładność, GeoIP City jest
zamiennikiem GeoLite City.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_datadir}/GeoIP/*.dat
