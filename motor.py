import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p 
import os

class MOTOR:
    def __init__(self, jointName):
        self.jointName= jointName
        print(self.jointName)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        if(self.jointName == "Torso_BackLeg"):
            self.amplitude = c.amplitudeBack
            self.frequency = 2
            self.offset = c.phaseOffsetBack
        else:
            self.amplitude = c.amplitudeBack
            self.frequency = c.frequencyBack
            self.offset = c.phaseOffsetBack

        self.x = np.linspace(0, 2*(np.pi), 1000)

        self.motorValues = np.zeros(1000)
        for i in range(1000):
            self.motorValues[i] = self.amplitude *(np.sin((self.frequency*self.x[i])+self.offset))

    def Set_Value(self, robotId, timeStep):
        self.timeStep =timeStep
        self.robotId = robotId
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = self.robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = self.motorValues[self.timeStep],
        maxForce = c.maxForce)

    def Save_Values(self):
        self.save_path = '/Users/janeyalex/Documents/CS206/JaneysBots/data'
        self.file_name = "motorData"
        self.completeName = os.path.join(self.save_path, self.file_name)
        np.save(self.completeName,self.motorValues)
