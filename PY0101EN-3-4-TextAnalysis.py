# TEXT ANALYSIS  ----------- CREATING A CLASS WITH METHODS
# You have been recruited by your friend, a linguistics enthusiast,
# to create a utility tool that can perform analysis on a given piece of text.

# Complete the class 'analysedText' with the following methods -
class analysedText(object):

# Constructor - Takes argument 'text',makes it lower case and removes all punctuation.
# Assume only the following punctuation is used - period (.),
# exclamation mark (!), comma (,) and question mark (?). Store the argument in "fmtText"
    def __init__ (self, text):
# remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
# make text lowercase
        formattedText = formattedText.lower()

        self.fmtText = formattedText

# freqAll - returns a dictionary of all unique words in the text
# along with the number of their occurences.
    def freqAll(self):
 # split text into words
        wordList = self.fmtText.split(' ')
# Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        return freqMap

# freqOf - returns the frequency of the word passed in argument.
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0
