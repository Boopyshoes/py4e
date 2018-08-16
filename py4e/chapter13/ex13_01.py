# Python for Everyone
# Chapter 13 exercise 1
# modify geojson.py to
# 1) print out the two character country code
# 2) handle the case where country code isn't there gracefully
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    country = None
    for component in js["results"][0]["address_components"]:
            print(component["types"][0])
            if component["types"][0] == "country":
                country = component["short_name"]

    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    if country is None:
        print('No country found for location:',address)
    else:
        print('Country',country)
