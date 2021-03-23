# Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and
# (3) counting the overall number of characters in the document.
# Don’t worry about the headers for this exercise,
# simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error
import re
import ssl

def extracthost(x) :
    x.lower()
    hn = re.findall('http.?://[www]*?[\.]*?(.+?)?/', x)
    print('webhost: ', hn)
    shn = hn[0]
    return shn

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

wh = input('Please enter the complete url: ')
hostname = extracthost(wh)
try:
    if len(hostname) > 1 :
        print('Passing hostname, repeat if incorrect')
except:
    print("An error occured. Recheck your url")

html = urllib.request.urlopen(wh, context=ctx).read()
text = html.decode() # IMPORTANT TO DECODE as it is coming from outside on UTF-8
if len(text) > 3000 :
    print(text[:3000])
    print('NOT THE COMPLETE TEXT!')

print('operation closed')
