from world import WORLD
from robot import ROBOT
import pybullet as p 
import pybullet_data
import pyrosim.pyrosim as pyrosim
from time import sleep
import constants as c

class SIMULATION:
    def __init__(self, directOrGui):
        if( directOrGui == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        

    def Run(self):
        for timeStep in range(c.numTimeSteps):
             sleep(c.sleep)
             p.stepSimulation()
             self.robot.Sense(timeStep)
             self.robot.Think()
             self.robot.Act()

    def Get_Fitness(self):
        self.robot.Get_Fitness()
        
    def __del__(self):
        p.disconnect()


    