from urllib.request import urlopen
import urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite') # creating the file
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGER)')
# this doesn't delete previous data, just adds

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True: #loop to go through the unvisited friends accounts
    acct = input('Enter a Twitter account, or quit: ')
    if (acct == 'quit'): break
    if (len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '20'})
    # this will use the hidden.py program with the keys
    print('Retrieving', url)
    connection = urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())

    print('Remaining', headers['x-rate-limit-remaining']) # to know how many we have left 
    js = json.loads(data)
    # Debugging
    # print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, ))
    # setting the retrieved column to 1, stopping from repeating the above

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1', (friend, ))
        try:
            count = cur.fetchone()[0] # returns a tuple OK becuase limit 1 before otherwise use a for loop
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',(count+1, friend))
            countold = countold + 1 # no in the DB, just to keep track
        except:
            cur.execute('INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)', (friend, ))
            countnew = countnew + 1
    print('New accounts=', countnew, ' revisited=', countold)
    conn.commit()

cur.close()

'''
Since the program’s data is all stored on disk in a database,
the spidering activity can be suspended and resumed as many times
as you like with no loss of data.
'''
