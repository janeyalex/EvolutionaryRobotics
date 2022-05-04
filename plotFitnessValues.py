from cProfile import label
from tkinter import font
import numpy as np
import matplotlib.pyplot as plt
import constants as c
from scipy import stats

avgAdata = np.empty([60,50])
avgBdata = np.empty([60,50])

maxAdata = np.empty([60,50])
maxBdata = np.empty([60,50])

minAdata = np.empty([60,50])
minBdata = np.empty([60,50])

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

    #take min of population for each generation 
    minA = np.min(fitA,axis=0)
    minAdata[i-1] = minA

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

    #take min of population for each generation 
    minB = np.min(fitB,axis=0)
    minBdata[i-1] = minB



# #take the average of each generation over all runs
# overallAvgA = np.average(avgAdata,axis=0)
# overallAvgB = np.average(avgBdata,axis=0)

overallAvgA = np.average(maxAdata,axis=0)
overallAvgB = np.average(maxBdata,axis=0)

print(stats.ttest_ind(a=overallAvgA[49], b=overallAvgB[49], equal_var=True))
exit()

stdDevA = np.std(avgAdata, axis = 0)
stdDevB = np.std(avgBdata, axis = 0)

# #take the max of each generation over all runs
# overallMaxA = np.max(maxAdata,axis=0)
# overallMaxB = np.max(maxBdata,axis=0)


# #take the max of each generation over all runs
# overallMinA = np.max(minAdata,axis=0)
# overallMinB = np.max(minBdata,axis=0)

xNum = list(np.arange(1,51))

with plt.style.context('fivethirtyeight'):
   

#average plot
    # plt.figure(figsize=(8, 8))
    plt.plot(xNum,overallAvgA, color = 'teal', label = 'Robot A: no hidden neuron')
    plt.plot(xNum,overallAvgB, color = 'tomato',label = 'Robot B: one hidden neuron')

#     #max plot
#     # plt.plot(xNum,overallMaxA, color = 'teal' ,label = 'Robot A')
#     # plt.plot(xNum,overallMaxB , color = 'tomato',label = 'Robot B')

#     # #min plot
#     # plt.plot(xNum,overallMinA, color = 'teal')
#     # plt.plot(xNum,overallMinB, color = 'tomato')

    # plt.errorbar(xNum, overallAvgA, yerr = stdDevA,fmt='o',ecolor = 'cyan', color = 'black')
# # plt.errorbar(xNum, overallAvgB, yerr = stdDevB,fmt='o',ecolor = 'magenta', color = 'black')
#     # plt.annotate('Best of A', xy=(15,1.8), xycoords='data', fontsize = 10)
#     # plt.annotate('Best of B', xy=(15,1.45), xycoords='data', fontsize = 10)
#     # plt.annotate('Worst of A', xy=(15,1.1), xycoords='data', fontsize = 10)
#     # plt.annotate('Worst of B', xy=(15,1.3), xycoords='data', fontsize = 10)
    plt.xlim(1, 50)
    plt.yticks(fontsize=12)
    plt.xticks(fontsize=12)
    plt.xlabel('Generation', fontsize= 12)
    plt.ylabel('Averaged Fitness Value',fontsize= 12)
    plt.suptitle("Average Fitness of A and B Robot")
    plt.title('Population Size= 10, Generations = 50', fontsize = 12)

    # plt.ylabel('Max and Min Fitness Values',fontsize= 12)
    # plt.suptitle("Max and Min Fitness of A and B Robot")
    # plt.title('Population Size= 10, Generations = 50', fontsize = 12)
    
    plt.legend(prop= {"size": 10})
    plt.show()
    

# # print(stdDevA)
# # print("")
# # print(stdDevB)
# # exit()
# # plt.subplot(2,1,1)
# # plt.plot(xNum,overallAvgA,'r-')
# # plt.errorbar(xNum, overallAvgA, yerr = stdDevA,fmt='o',ecolor = 'cyan')
# # plt.title('Robot A')
# # # plt.xlim(1, 50)

# # plt.subplot(2,1,2)
# # plt.plot(xNum,overallAvgB,'b*-')
# # plt.errorbar(xNum, overallAvgB, yerr = stdDevB,fmt='o',ecolor = 'magenta')
# # plt.title('Robot B')
# # plt.xlim(1, 50)
# # plt.show()


