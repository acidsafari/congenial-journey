# SIMPLE WEB CONNECTION
import socket
# socket.socket creates a point ready to connect, but not yet connected
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# .socket can be used to connect to other servers,
#just need to follow the appropiate protocol
mysock.connect(('data.pr4e.org', 80)) #this is the actual connection
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #needs an empty line
# .encode() transforms string into a BYTES OBJECT
# which can be done with b'<string>' also #DIFFERENT TYPE OF OBJECT
mysock.send(cmd)

while True:
    data = mysock.recv(512) #receiving packets
    if len(data) < 1: #finish when it is nothing left coming in
        break
    print(data.decode(),end='') # transforms BYTES -> STRINGS

mysock.close()

# RETRIEVING AN IMAGE
import socket
import time
HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""
while True:
    data = mysock.recv(5120)
    if len(data) < 1: break
    #time.sleep(0.25) #this is for FLOW CONTROL
    count = count + len(data)
    print(len(data), count) #this is to see how the data has been sent
    picture = picture + data

mysock.close()
# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())
# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

# URLLIB  - a library that has coded in methods with the previos stuff
import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand: #the for loop is to read the file
    print(line.decode().strip()) # READING THE FILE ONLY

#the urllib code cleans the data received and only shows the contents of the file

# another way to use the urllib
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# This is like if we read a file on our own computer
counts = dict() # this time we are counting the words of the text
for line in fhand:
    words = line.decode().split() # IMPORTANT TO DECODE as it is coming from outside on UTF-8
    for word in words:
        counts[word] = counts.get(word, 0) + 1

print(counts)

#this saves the file in your disk
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg', 'wb')
fhand.write(img) #if the file is too big, it might give you problems
fhand.close()

# so similar to the control flow, we download it in blocks, to reduce errors
import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True: # for the data blocks
    info = img.read(100000) # instead of .recv
    if len(info) < 1: break
    size = size + len(info)
    fhand.write(info) # writing it to disk, block by block

print(size, 'characters copied.')
fhand.close()

# URLLIB AND PARSING WITH RE ------------------------
"""# we can construct a RE to parse
<h1>The First Page</h1>
<p>
If you like, you can switch to the
<a href="http://www.dr-chuck.com/page2.htm"> Second Page</a>.
</p>
# to get the website from the page
href="http[s]?://.+?" #[s]? means 0 or 1 s
# (.+?) means one or more characters till " non-greedy"""

# complete code looks like:
import urllib.request, urllib.parse, urllib.error
import re
import ssl #libary to access HTTPS site
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # https or http format website
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
# list of all strings that match our RE , returning the link text between espressions
for link in links:
    print(link.decode())

# LIBRARY  BeautifulSoup for broken HTML code
# There are a number of Python libraries which can help you parse HTML and extract data from the pages
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser') # this cleans the data IT IS A SOUP OBJECT

# Retrieve all of the anchor tags
tags = soup('a') # this gives us a list of the anchor tags
# READ THE BeautifulSoup PAGE FOR MORE INFO
for tag in tags:
    print(tag.get('href', None))

# there is another way to print things you need, in the book
