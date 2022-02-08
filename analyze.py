from cProfile import label
import numpy as np
import matplotlib.pyplot as plt


# backLegSensorValues = np.load('/Users/janeyalex/Documents/CS206/JaneysBots/data/sensoryDataBackLeg.npy')
# frontLegSensorValues = np.load('/Users/janeyalex/Documents/CS206/JaneysBots/data/sensoryDataFrontLeg.npy')

# plt.plot(backLegSensorValues, label = "Back Leg Sensor", linewidth = 3)
# plt.plot(frontLegSensorValues, label = "Front Leg Sensor")
# plt.xlim(0, 100)
# plt.legend()
# plt.show()

targetValuesBack = np.load('/Users/janeyalex/Documents/CS206/JaneysBots/data/sinBackData.npy')
targetValuesFront = np.load('/Users/janeyalex/Documents/CS206/JaneysBots/data/sinFrontData.npy')
plt.plot(targetValuesBack, label = "Back Leg Sensor", linewidth = 3)
plt.plot(targetValuesFront, label = "Front Leg Sensor")
plt.xlim(0, 1000)
plt.legend()
plt.show()

