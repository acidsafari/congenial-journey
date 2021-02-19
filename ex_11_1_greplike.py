# Write a simple program to simulate the operation of the grep command on Unix.
import re
# Ask the user to enter a regular expression and
hand = open('mbox.txt')
lookfor = input('Please enter regular expression: ')
i = 0 #counter
for line in hand:
    line = line.rstrip()
    if re.search(lookfor, line):
        i = i + 1

print('mbox.txt had ', i, 'lines that matched ', lookfor)
#count the number of lines that matched the regular expression:




# $ python grep.py
# Enter a regular expression: ^Author
# mbox.txt had 1798 lines that matched ^Author
