'''
Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib
and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1144069.json (Sum ends with 80)
You do not need to save these files to your folder since your program will read the data directly
from the URL. Note: Each student will have a distinct data url for the assignment
- so only use your own data url for analysis.
'''
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

''' THIS WILL BE USEFUL TO KEEP FOR FUTURE USES WHEN API KEYS ARE NEEDED
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ') #The program takes the search string and constructs a URL
    if len(address) < 1: break

    parms = dict() #with the search string as a properly encoded parameter and then uses urllib
    parms['address'] = address #to retrieve the text from the Google geocoding API.
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
'''
# INPUT URL
url = input('Enter url- ')
if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/comments_1144069.json"

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode()) #print check THIS IS A DICTIONARY!!
data.decode()

js = json.loads(data)
j = js['comments']
#print(j) #print check

x = 0
for item in j:
    i = item['count']
    x = x + i

print('Total count = ', x)
