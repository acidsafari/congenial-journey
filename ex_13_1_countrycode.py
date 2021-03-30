import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ') #The program takes the search string and constructs a URL
    if len(address) < 1: break # to break the loop we just press enter

    parms = dict() #with the search string as a properly encoded parameter and then uses urllib
    parms['address'] = address #to retrieve the text from the Google geocoding API.
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms) # this gives us the right coding to make the call

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK': #debugging for errors 
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    try :
        abcountry = js['results'][0]["address_components"][5]['short_name']
        print('Country Code: ', abcountry)
    else :
        print('Could not find the country code! Sorry')


""""
    try :
        abcountry = js['results'][0]["address_components"][5]['short_name']
    except IndexError :
        pass
        print('==== NA ====')
    except :
        lent(abcountry) < 1
        print('==== Not a Country ====')
"""
