"""
Extracting Data from XML

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/geoxml.py.
The program will prompt for a URL, read the XML data from that URL using urllib
and then parse and extract the comment counts from the XML data,
compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing
and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1144068.xml (Sum ends with 2)
You do not need to save these files to your folder
since your program will read the data directly from the URL.
Note: Each student will have a distinct data url for the assignment
    - so only use your own data url for analysis.

"""


"""
Data Format and Approach
The data consists of a number of names and comment counts in XML as follows:

<comment>
  <name>Matthias</name>
  <count>97</count>
</comment>

You are to look through all the <comment> tags and find the <count> values sum the numbers.
The closest sample code that shows how to parse XML is geoxml.py.
But since the nesting of the elements in our data is different than the data we are parsing
in that sample code you will have to make real changes to the code.
To make the code a little simpler, you can use an XPath selector string to look
through the entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count') THIS DID NOT WORK FOR ME

Take a look at the Python ElementTree documentation and look for the supported XPath syntax
for details. You could also work from the top of the XML down to the comments node
and then loop through the child nodes of the comments node.
"""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ')
if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/comments_1144068.xml"

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
data.decode()
tree = ET.fromstring(data)

lst = tree.findall('comments/comment') # looking for the CHILD tag on the parent/CHILD try
x = 0
print('count tags:', len(lst)) # it is telling us how many count-tags there are
for item in lst: # this is to go through the main tags with mutiple tags under them
    x = x + int(item.find('count').text)
    #print('Count', item.find('count').text) # calling each of the tags

print('Sum of counts tag: ' , x)
