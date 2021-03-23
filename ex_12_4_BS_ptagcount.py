# Change the urllinks.py program to extract and count paragraph (p) tags
# from the retrieved HTML document and display the count of the paragraphs,
# as the output of your program. Do not display the paragraph text, only count them.
# Test your program on several small web pages as well as some larger web pages.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 :
    url = "https://www.coursera.org/learn/python-network-data/lecture/bqeq7/bonus-interview-tim-berners-lee-inventing-the-web"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup) #print check
print('FIRST') #print check
# THIS METHOD WORKS
# Retrieve all of the anchor tags
tags = soup.find_all('p')
count = 0
for tag in tags:
    count = 1 + count
    # Look at the parts of a tag
    #print('TAG:',tag)
    #print(count)
    #print('Contents:',tag.contents[0])

print('Number of p tags: ' , count)
#print('LAST') #print check
