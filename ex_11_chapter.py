#REGULAR EXPRESSIONS
#re.search()
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):#more powerful version of line.find()
        print(line)     #or startswith()

#USE OF THE . TO MATCH ANY CHARACTER
# i.e. 'F..m'
# USE OF * AND + FOR REPETITIONS ---- CALLED WILDCARD

# findall() very powerful to pick sections of strings -> in list form
import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\S+@\S+', s)
print(lst)

#this can be used for files to extract emails
import re
hand = open('mbox-short.txt')
y = 0
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        y = y + 1 #I've have added a counter
        print(x)

print(y)

# SEARCHING AND EXTRACTING
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X\S*: [0-9.]+', line):
        print(line)
# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal. === ^X-.*: [0-9.]+


# parentheses indicate that while you want the whole expression to match,
#you only are interested in extracting a portion of the substring
#that matches the regular expression.
import re
hand = open('mbox-short.txt')
l = list() #make a list
for line in hand:
    line = line.rstrip()
    x = re.findall('^X\S*: ([0-9.]+)', line) #with just the numbers between ()
    if len(x) > 0:
        l = l + x
        print(x)

print(l) #though the numbers are in a string format

# POSSIBLE EXERCISE TO FIND THE Maximumimport re
hand = open('mbox-short.txt')
l = list()
i = 1
for line in hand:
    line = line.rstrip()
    x = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(x) != 1 : continue
    num = float(x[0])
    l.append(num) #list of floats
    i = i + 1 #counter

print(i)
print(l)
print('Maximum: ', max(l))
