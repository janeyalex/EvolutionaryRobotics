from time import sleep
import pybullet as p 
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")
for i in range(10000):
    sleep(1/60)
    p.stepSimulation()
    print(i)
p.disconnect()