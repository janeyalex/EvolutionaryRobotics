import numpy as np
import matplotlib.pyplot as plt


backLegSensorValues = np.load('/Users/janeyalex/Documents/CS206/JaneysBots/data/sensoryData.npy')
print(backLegSensorValues)

plt.plot(backLegSensorValues)
plt.xscale
plt.show()




