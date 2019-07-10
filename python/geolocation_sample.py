import geoip2.database


reader = geoip2.database.Reader('/usr/GeoLite2/GeoLite2-City.mmdb')
response = reader.city('128.101.101.101')

print('country iso_code:', response.country.iso_code, '\n')
print('subdivision name:', response.subdivisions.most_specific.name, '\n')
print('subdivision iso_code:', response.subdivisions.most_specific.iso_code, '\n')
print('city name:', response.city.name, '\n')
print('postal code:', response.postal.code, '\n')
print('latitude:', response.location.latitude, '\n')
print('longitude:', response.location.longitude, '\n')

reader.close()
