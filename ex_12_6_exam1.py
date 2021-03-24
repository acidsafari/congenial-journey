# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py
""" # To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file  """
# import statements
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/comments_1144066.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup) #print check
#print('FIRST') #print check
# THIS METHOD WORKS
# Retrieve all of the anchor tags
tags = soup.find_all('span')
count = 0
for tag in tags:
    count = int(tag.contents[0]) + count
    """# Look at the parts of a tag
    #print('TAG:',tag)
    #print(count)
    #print('Contents:',tag.contents[0])"""

print('Sum of numbers in the span tag: ' , count)
#print('LAST') #print check


""" The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1144066.html (Sum ends with 15)"""

""" The file is a table of names and comment counts.
You can ignore most of the data in the file except for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

You are to find all the <span> tags in the file and pull out the numbers from the tag and
sum the numbers."""


""" It shows how to find all of a certain kind of tag,
loop through the tags and extract the various aspects of the tags.
...
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
   # Look at the parts of a tag
   print 'TAG:',tag
   print 'URL:',tag.get('href', None)
   print 'Contents:',tag.contents[0]
   print 'Attrs:',tag.attrs
You need to adjust this code to look for span tags and pull out the text content of the span tag,
convert them to integers and add them up to complete the assignment."""
