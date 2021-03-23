# Change the socket program socket1.py to prompt the user for the URL
# so it can read any web page. You can use split('/') to break the URL
# into its component parts so you can extract the host name for the socket connect call.
# Add error checking using try and except to handle the condition
# where the user enters an improperly formatted or non-existent URL.

import socket
import re

def extracthost(x) :
    x.lower()
    hn = re.findall('http.?://[www]*?[\.]*?(.+?)?/', x)
    print('webhost: ', hn)
    shn = hn[0]
    return shn

wh = input('Please enter the complete url: ')
hostname = extracthost(wh)
try:
    if len(hostname) > 1 :
        print('Passed')
except:
    print("An error occured. Recheck your url")

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname, 80))
#we got up to here need to figure out how to write the next line
getpart = 'GET ' + wh + 'HTTP/1.0\r\n\r\n'
cmd = getpart.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    print(data.decode(),end='')
mysock.close()
