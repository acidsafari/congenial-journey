import sqlite3

conn = sqlite3.connect('emaildb.sqlite') # creates the table if it doesn't exist
''' It's not as simple as you just open it and read it,
but you open it and then you send SQL commands the cursor
and then you get your responses through that same cursor
'''
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts') # in case the table is already there

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]  '''the ? acts a a place holder and prevents SQLI
    which will ultimately be replaced by the tuple (email,)'''
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    '''this is not reading but openning a record set'''
    row = cur.fetchone() # grab the first one
    ''' BELOW is kind of the the read it, parse it, check to see if it's there,
    if it's not, insert it, if it is, update it'''
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,)) # it's always better to do an UPDATE (atomic or efficient)
    conn.commit() # adding data from memory to disk

'''Now we are going to read what is in the DB'''
# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
