from time import sleep
import pybullet as p 
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import math
import random
import constants as c
from simulation import SIMULATION

# #back leg variables
# amplitudeBack = c.amplitudeBack
# frequencyBack = c.frequencyBack
# phaseOffsetBack = c.phaseOffsetBack

# #front leg variables
# amplitudeFront = c.amplitudeFront
# frequencyFront = c.frequencyFront
# phaseOffsetFront = c.phaseOffsetFront
# #amplitude * sin(frequency * i + phaseOffset)






# backLegSensorValues = np.zeros(1000)
# frontLegSensorValues = np.zeros(1000)

# x = np.linspace(0, 2*(np.pi), 1000)

# targetAnglesBack = np.zeros(1000)
# targetAnglesFront = np.zeros(1000)
# for i in range(1000):
#     targetAnglesBack[i] = amplitudeBack *(np.sin((frequencyBack*x[i])+phaseOffsetBack))
#     targetAnglesFront[i] = amplitudeFront *(np.sin((frequencyFront*x[i])+phaseOffsetFront))



# # save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
# # file_name2 = "sinBackData"
# # completeName2 = os.path.join(save_path, file_name2)
# # np.save(completeName2,targetAnglesBack)

# # file_name3 = "sinFrontData"
# # completeName3 = os.path.join(save_path, file_name3)
# # np.save(completeName3,targetAnglesFront)

# # exit()





# save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
# file_name = "sensoryDataBackLeg"
# completeName = os.path.join(save_path, file_name)

# np.save(completeName,backLegSensorValues)

# file_name1 = "sensoryDataFrontLeg"
# completeName1 = os.path.join(save_path, file_name1)

# np.save(completeName1,frontLegSensorValues)

simulation = SIMULATION()
simulation.Run()