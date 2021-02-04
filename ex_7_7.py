fname = input('Enter the file name: ')
try: #making full proof for invalid file names
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
count = 0
for line in fhand:#counting selected lines
    if line.startswith('Subject:'):
        count = count + 1

print('There were', count, 'subject lines in', fname)
