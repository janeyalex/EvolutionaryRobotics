from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import constants as c

avgAdata = np.empty([20,50])
avgBdata = np.empty([20,50])

for i in range(1,21):
    filename = '/Users/janeyalex/Documents/CS206/JaneysBots/data/fitnessDataA'
    filename = filename + str(i)+'.npy'
    fitA = np.load(filename)
    fitAvgA = np.average(fitA,axis=0)
    avgAdata[i-1] = fitAvgA

    filename1 = '/Users/janeyalex/Documents/CS206/JaneysBots/data/fitnessDataB'
    filename1 = filename1 + str(i)+'.npy'
    fitB = np.load(filename1)
    fitAvgB = np.average(fitB,axis=0)
    avgBdata[i-1] = fitAvgB


overallAvgA = np.average(avgAdata,axis=0)
overallAvgB = np.average(avgBdata,axis=0)

stdDevA = np.std(avgAdata, axis = 0)
stdDevB = np.std(avgBdata, axis = 0)


xNum = list(np.arange(1,51))

plt.plot(xNum,overallAvgA,'r-', label = 'Robot A')
plt.plot(xNum,overallAvgB,'b*-', label = 'Robot B')
# plt.errorbar(xNum, overallAvgA, yerr = stdDevA,fmt='o',ecolor = 'cyan')
plt.errorbar(xNum, overallAvgB, yerr = stdDevB,fmt='o',ecolor = 'magenta')
plt.xlim(1, 50)
plt.xlabel('Generation')
plt.ylabel('Averaged Fitness Value')
plt.title('Fitness of A and B Robot 20 simulations (Population Size= 10, Generations = 50)' )
plt.legend()
plt.show()

