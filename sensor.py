import numpy as np
import pyrosim.pyrosim as pyrosim
import os

class SENSOR:
    def __init__(self, linkName):
        self.linkName= linkName
        self.values = np.zeros(1000)
        
    def getValue(self,timeStep):
        self.timeStep =timeStep
        self.values[self.timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        if (self.timeStep==999):
            print(self.values)

    def Save_Values(self):
        self.save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
        self.file_name = "sensoryData"
        self.completeName = os.path.join(self.save_path, self.file_name)

        np.save(self.completeName,self.values)

    