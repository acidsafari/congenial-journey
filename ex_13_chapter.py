# Parsing XML

import xml.etree.ElementTree as ET
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''
tree = ET.fromstring(data) # converts the string representation of the XML into a “tree” of XML elements
print('Name:', tree.find('name').text) # calling each of the tags with tree.find
# the .text calls for the item between the tags, which is text in this case
print('Attr:', tree.find('email').get('hide')) # in this instance we're calling for the attribute


import xml.etree.ElementTree as ET
input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''
stuff = ET.fromstring(input) # this creates the tree format
lst = stuff.findall('users/user') # looking for the CHILD tag on the parent/CHILD try
print('User count:', len(lst)) #becuase it finds 2 tags
for item in lst: # this is to go through the main tags with mutiple tags under them
    print('Name', item.find('name').text) # calling each of the tags
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

# Parsing JSON
import json
data = ''' [
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
},
{ "id" : "009",
"x" : "7",
    "name" : "Brent"
  }
]'''
info = json.loads(data) # this generates a list in NATIVE PYTHON STRUCTURE
print('User count:', len(info))
for item in info: # extracting the values of the list, moving through the nested dicts
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

'''
TWITTER
# hidden.py ------   Keep this file separate
The Twitter web service are accessed using a URL like this:
https://api.twitter.com/1.1/statuses/user_timeline.json
'''

def oauth():
    return {"consumer_key": "MBha6D8OUedUqZwzSuku0wWGT",
            "consumer_secret": "oVSrjZP9gegZ5CV45eRvGLPMkGnZWbD94pF5mhlUvGoQlfqKXv",
            "token_key": "2479049365-6SHkD0W7ZHo1gmAr1KI7drpcAhEREGB8FAcSinz",
            "token_secret": "Zr3gv9ZTMY5cnetbgeBYxVIfHLZdDJbHNrVULtJPsoTvR"}

'''
we hide all the complexity in the files oauth.py and twurl.py
'''
# TWITTER1.PY

import urllib.request, urllib.parse, urllib.error
import twurl
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250])
    headers = dict(connection.getheaders())
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])

# TWITTER2.PY
