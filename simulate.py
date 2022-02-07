from time import sleep
import pybullet as p 
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os
import math
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)



for i in range(1000):
    sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i]= pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_BackLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-math.pi/2.0, math.pi/2.0),
        maxForce = 75)
    
    pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = "Torso_FrontLeg",
        controlMode = p.POSITION_CONTROL,
        targetPosition = random.uniform(-math.pi/2.0, math.pi/2.0),
        maxForce = 75)

p.disconnect()

save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
file_name = "sensoryDataBackLeg"
completeName = os.path.join(save_path, file_name)

np.save(completeName,backLegSensorValues)

file_name1 = "sensoryDataFrontLeg"
completeName1 = os.path.join(save_path, file_name1)

np.save(completeName1,frontLegSensorValues)