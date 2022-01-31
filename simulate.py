from time import sleep
import pybullet as p 
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import os

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(10000)



for i in range(10000):
    sleep(1/60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    
print(backLegSensorValues)
p.disconnect()

save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
file_name = "sensoryData"
completeName = os.path.join(save_path, file_name)

np.save(completeName,backLegSensorValues)
