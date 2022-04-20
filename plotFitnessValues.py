from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
import constants as c


fitA = np.load('/Users/janeyalex/Documents/CS206/JaneysBots/data/fitnessDataA.npy')
fitB = np.load('/Users/janeyalex/Documents/CS206/JaneysBots/data/fitnessDataB.npy')



xNum = [1,2,3,4,5,6,7,8,9,10]


# for i in range(c.numberOfGenerations):
#     plt.plot(xNum,fitA[i,:],'r-',linewidth = 3)
    
#     plt.plot(xNum,fitB[i,:],'b*-')
    
# plt.plot([],[], 'r-', label='Robot A')
# plt.plot([],[], 'b*-', label='Robot B')

# plt.xlim(1, 10)
# plt.xlabel('Run in the Popluation')
# plt.ylabel('Fitness Value')
# plt.title('Fitness of A and B Robot (Population Size= 10, Generations = 10)' )
# plt.legend()
# plt.show()

fitAvgA = np.average(fitA,axis=0)
fitAvgB = np.average(fitB,axis=0)

plt.plot(xNum,fitAvgA,'r-')
plt.plot(xNum,fitAvgB,'b*-')
plt.xlim(1, 10)
plt.xlabel('Generation')
plt.ylabel('Averaged Fitness Value over 10 Runs')
plt.title('Fitness of A and B Robot (Population Size= 10, Generations = 10)' )
plt.legend()
plt.show()