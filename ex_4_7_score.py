gradescore = input("Enter Score between 0 and 1: ")

score = float(gradescore)

def computegrade(score):
    print('Enter score: ',score)
    return score

computegrade(score)

if score < 0 and score > 1 :
    print('Error, PLEASE ENTER VALUES BETWEEN 0 AND 1!')
elif score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
elif score < 0.6 :
    print('F')

#add at the beginning
#def computegrade(score):
    #print('Enter score: ',score)
    #return score
