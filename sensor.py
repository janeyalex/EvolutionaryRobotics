import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName= linkName
        self.values = np.zeros(1000)
        
    def getValue(self,timeStep):
        self.timeStep =timeStep
        self.values[self.timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if (self.timeStep==999):
            print(self.values)
