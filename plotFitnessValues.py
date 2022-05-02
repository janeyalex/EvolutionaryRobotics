from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import constants as c

avgAdata = np.empty([60,50])
avgBdata = np.empty([60,50])

maxAdata = np.empty([60,50])
maxBdata = np.empty([60,50])

for i in range(1,41):
    #read in all A files
    filename = '/Users/janeyalex/Documents/CS206/JaneysBots/data/fitnessDataA'
    filename = filename + str(i)+'.npy'
    fitA = np.load(filename)

    #take average of population for each generation
    fitAvgA = np.average(fitA,axis=0)
    avgAdata[i-1] = fitAvgA

    #take max of population for each generation 
    maxA = np.max(fitA,axis=0)
    maxAdata[i-1] = maxA

    #read in all B files
    filename1 = '/Users/janeyalex/Documents/CS206/JaneysBots/data/fitnessDataB'
    filename1 = filename1 + str(i)+'.npy'
    fitB = np.load(filename1)

    #take average of population for each generation
    fitAvgB = np.average(fitB,axis=0)
    avgBdata[i-1] = fitAvgB

    #take max of population for each generation
    maxB = np.max(fitB,axis=0)
    maxBdata[i-1] = maxB

#take the average of each generation over all runs
overallAvgA = np.average(avgAdata,axis=0)
overallAvgB = np.average(avgBdata,axis=0)

stdDevA = np.std(avgAdata, axis = 0)
stdDevB = np.std(avgBdata, axis = 0)

#take the max of each generation over all runs
overallMaxA = np.max(maxAdata,axis=0)
overallMaxB = np.max(maxBdata,axis=0)

xNum = list(np.arange(1,51))

#average plot
# plt.plot(xNum,overallAvgA,'r-', label = 'Robot A')
# plt.plot(xNum,overallAvgB,'b*-', label = 'Robot B')

#max plot
plt.plot(xNum,overallMaxA,'r-', label = 'Robot A')
plt.plot(xNum,overallMaxB,'b*-', label = 'Robot B')

# plt.errorbar(xNum, overallAvgA, yerr = stdDevA,fmt='o',ecolor = 'cyan', color = 'black')
# plt.errorbar(xNum, overallAvgB, yerr = stdDevB,fmt='o',ecolor = 'magenta', color = 'black')
plt.xlim(1, 50)
plt.xlabel('Generation')
plt.ylabel('Averaged Fitness Value')
plt.title('Fitness of A and B Robot 60 simulations (Population Size= 10, Generations = 50)' )
plt.legend()
plt.show()

