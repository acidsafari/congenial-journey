finput = input('Insert file name:')
try:#safety for input error
    fhand = open(finput)
except:
    print('File name not found: ' , fhand)
    exit()
x = 0
c = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence'): # Skip 'uninteresting lines'
        x = x + 1#counting the number of lines
        id0 = line.find(':')
        conf = line[id0+1: ]
        conf = conf.lstrip()
        num = float(conf)
        c = num + c
        #continue #goes back to the top

avgspam = (c / x)
print('Average spam confidence: ', avgspam)
