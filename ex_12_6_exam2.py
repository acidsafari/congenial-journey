"""
Following Links in Python

In this assignment you will write a Python program that expands on
http://www.py4e.com/code3/urllinks.py.
The program will use urllib to read the HTML from the data files below,
extract the href= vaues from the anchor tags, scan for a tag that is in a particular position
relative to the first name in the list, follow that link and repeat the process
a number of times and report the last name you find.

We provide two files for this assignment. One is a sample file where we give you the name
for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times.
The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Karol.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times.
The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: O
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if len(url) < 1 :
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup) #print check
#print('FIRST') #print check

# position and repetition input
ic = input('Enter count: ')
pos = input('Enter position: ')

# Retrieve the wanted number of tags

count = 0
while count < int(ic) :
    tags = soup.find_all('a', limit = int(pos)) # the limit statement gives us the position wanted
    for tag in tags:
        tn = tag.get('href', None) # we need to get the page
        htmlit = urllib.request.urlopen(tn, context=ctx).read() # to loop it
        soup = BeautifulSoup(htmlit, "html.parser") # parse it again
    count = count + 1 # iterate ic times
    #print('TAG:',tag) #this is a visual check of what it is required
    #print(tag.get('href', None)) # this is a check of what tag is reading
    print('Retrieving: ' , tn) # visually looking at the page retrieved
    #print('Contents:',tag.contents[0]) # this will print the name for each page

print('The name you are looking for is: ' , tag.contents[0]) #this will print the final name 

"""
Strategy
The web pages tweak the height between the links and hide the page after a few seconds
to make it difficult for you to do the assignment without writing a Python program.
But frankly with a little effort and patience you can overcome these attempts to make it
a little harder to complete the assignment without writing a Python program.
But that is not the point. The point is to write a clever Python program to solve the program.
"""

"""
Sample execution

Here is a sample execution of a solution:

$ python3 solution.py
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Enter count: 4
Enter position: 3
Retrieving: http://py4e-data.dr-chuck.net/known_by_Fikret.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Montgomery.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Mhairade.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Butchi.html
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anayah.html
"""
