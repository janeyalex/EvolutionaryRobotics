from time import sleep
import pybullet as p 

physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")
for i in range(1000):
    sleep(1/60)
    p.stepSimulation()
    print(i)
p.disconnect()