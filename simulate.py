from time import sleep
import pybullet as p 
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import math
import random

amplitude = np.pi/4
frequency = 10
phaseOffset = 0
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
targetAngles = np.zeros(1000)
for i in range(1000):
    targetAngles[i] = amplitude *(np.sin((frequency*x[i])+phaseOffset))


#targetAngles = np.sin(x)*(np.pi/4)

save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
file_name2 = "sinData"
completeName2 = os.path.join(save_path, file_name2)

np.save(completeName2,targetAngles)
exit()

for i in range(1000):
    sleep(1/10000)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i]= pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[i],
        maxForce = 500)
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = targetAngles[i],
        maxForce = 500)

p.disconnect()

save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
file_name = "sensoryDataBackLeg"
completeName = os.path.join(save_path, file_name)

np.save(completeName,backLegSensorValues)

file_name1 = "sensoryDataFrontLeg"
completeName1 = os.path.join(save_path, file_name1)

np.save(completeName1,frontLegSensorValues)

