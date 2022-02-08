from time import sleep
import pybullet as p 
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import math
import random

#back leg variables
amplitudeBack = np.pi/4
frequencyBack = 10
phaseOffsetBack = 0

#front leg variables
amplitudeFront = np.pi/4
frequencyFront = 1
phaseOffsetFront = (3/2)*np.pi
#amplitude * sin(frequency * i + phaseOffset)

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

x = np.linspace(0, 2*(np.pi), 1000)

targetAnglesBack = np.zeros(1000)
targetAnglesFront = np.zeros(1000)
for i in range(1000):
    targetAnglesBack[i] = amplitudeBack *(np.sin((frequencyBack*x[i])+phaseOffsetBack))
    targetAnglesFront[i] = amplitudeFront *(np.sin((frequencyFront*x[i])+phaseOffsetFront))



# save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
# file_name2 = "sinBackData"
# completeName2 = os.path.join(save_path, file_name2)
# np.save(completeName2,targetAnglesBack)

# file_name3 = "sinFrontData"
# completeName3 = os.path.join(save_path, file_name3)
# np.save(completeName3,targetAnglesFront)

# exit()

for i in range(1000):
    sleep(1/500)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i]= pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesBack[i],
        maxForce = 500)
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAnglesFront[i],
        maxForce = 500)

p.disconnect()

save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
file_name = "sensoryDataBackLeg"
completeName = os.path.join(save_path, file_name)

np.save(completeName,backLegSensorValues)

file_name1 = "sensoryDataFrontLeg"
completeName1 = os.path.join(save_path, file_name1)

np.save(completeName1,frontLegSensorValues)

