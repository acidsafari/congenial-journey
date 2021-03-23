# (Advanced) Change the socket program so that it only shows data after the headers
# and a blank line have been received.
#Remember that recv receives characters (newlines and all), not lines.

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
        print('Passing hostname, check if incorrect')
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
    x = data.decode() #into a string
    print(x) #print check

y = x.find('\r\n\r\n') #can't work out why it doesn't work
# I had tried '<' which is normally the first item after the file headers
print(y)
print(x[y:])
#print(data.decode(),end='')

mysock.close()
