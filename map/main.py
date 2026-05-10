import geocoder

import requests
freegeoip = "http://freegeoip.net/json/"
geo_r = requests.get(freegeoip)
print("geo_r: " + str(geo_r))
geo_json = geo_r.json()

address="192.168.1.179"
g= geocoder.google(address)
lat_ad=g.latlng[0]
lon_ad=g.latlng[1]

user_postition = [geo_json["latitude"], geo_json["longitude"]]
lat_ip=user_postition[0]
lon_ip=user_postition[1]

#Calculate the great circle distance between two points on the earth (specified in decimal degrees)

from math import radians, cos, sin, asin, sqrt
# convert decimal degrees to radians 
lon_ad, lat_ad, lon_ip, lat_ip = map(radians, [lon_ad, lat_ad, lon_ip, lat_ip])

# haversine formula 
dlon = lon_ip - lon_ad 
dlat = lat_ip - lat_ad 
a = sin(dlat/2)**2 + cos(lat_ad) * cos(lat_ip) * sin(dlon/2)**2
c = 2 * asin(sqrt(a)) 
km = 6367 * c
#end of calculation

#limit decimals
km = ('%.0f'%km)

print(address+' is about '+str(km)+' km away from you')