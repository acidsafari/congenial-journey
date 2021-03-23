# Change your socket program so that it counts the number of characters it has received
# and stops displaying any text after it has shown 3000 characters.
# The program should retrieve the entire document and count the total number of characters
# and display the count of the number of characters at the end of the document.
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

count = 0
while True:
    data = mysock.recv(512)
    if len(data) < 1: break
    count = count + len(data)
    print('Total Data Received', count)
    x = data.decode()
    print(x[:3000])
    #print(data.decode(),end='')

mysock.close()
