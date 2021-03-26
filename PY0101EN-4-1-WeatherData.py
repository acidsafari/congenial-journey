# Given below is a file "resources/ex4.csv",
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/ex4.csv
# which contains some precipiation data for the month of June.
#Each line in the file has the format - Date,Precipation (upto two decimal places)
# Your task is to complete the getNAvg function
#  that computes a simple moving average for N days for the precipiation data,
# where N is a parameter.
# Your function should return a list of moving averages for the given data.
# 𝑀𝑖 = 𝑀𝑖−1+((𝑛𝑖−𝑛𝑖−𝑘)/𝑘),for i = k to m ; where 𝑀𝑖 is the moving average

import matplotlib.pyplot as plt
import urllib.request, urllib.parse, urllib.error

url = https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/ex4.csv
filename = "ex4.csv"
urllib.request.urlretrieve(url, filename)

statData ="ex4.csv"

def getNAvg(file,N):
    """
    file - File containting all the raw weather station data
    N - The number of days to compute the moving average over

    Return a list of containg the moving average of all data points
    """
    row = 0 # keep track of rows
    lastN = [] # keep track of last N points
    mean = [0] # running avg


    with open(file,"r") as rawData:
        for line in rawData:
            if (row == 0): # Ignore the headers
                row = row + 1
                continue

            line = line.strip('\n')
            lineData = float(line.split(',')[1])

            if (row<=N):
                lastN.append(lineData)
                mean[0] = (lineData + mean[0]*(row-1))/row
            else:
                mean.append( mean[row - N -1]+ (lineData - lastN[0])/N)
                lastN = lastN[1:]
                lastN.append(lineData)

            row = row +1
        return mean


def plotData(mean,N):
        """
        mean - series to plot
        N - parameter for legend
        Plots running averages

        """
        mean = [round(x,3) for x in mean]
        plt.plot(mean,label=str(N) + ' day average')
        plt.xlabel('Day')
        plt.ylabel('Precipiation')
        plt.legend()

plotData(getNAvg(statData,1),1)
plotData ([0 for x in range(1,5)]+ getNAvg(statData,5),5 )
plotData([0 for x in range(1,7)] + getNAvg(statData,7),7)

#           ---------------- VERIFYING CODE -----------------------
avg5 =[4.18,4.78,4.34,4.72,5.48,5.84,6.84,6.76,6.74,5.46,4.18,2.74,2.52,2.02,2.16,2.82,2.92,4.36,4.74,5.12,5.34,6.4,6.56,6.1,5.74,5.62,4.26]
avg7 =[4.043,4.757,5.071,5.629,6.343,5.886,6.157,5.871,5.243,4.386,3.514,2.714,2.586,2.443,2.571,3.643,4.143,4.443,4.814,5.6,6.314,6.414,5.429,5.443,4.986]

def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return ' Test Failed'

print("getNAvg : ")
try:
    sol5 = getNAvg(statData,5)
    sol7 = getNAvg(statData,7)

    if(len(sol5)==len( avg5) and (len(sol7)==len(avg7))):
        err5 = sum([abs(avg5[index] - sol5[index])for index in range(len(avg5))])
        err7 = sum([abs(avg7[index] - sol7[index])for index in range(len(avg7))])
        print(testMsg((err5 < 1) and (err7 <1)))

    else:
        print(testMsg(false))
except NameError as e:
    print('Error! Code: {c}, Message: {m}'.format(c = type(e).__name__, m = str(e)))
except:
    print("An error occured. Recheck your function")
