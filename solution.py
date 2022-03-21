
import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = np.empty([c.numSensorNeurons,c.numMotorNeurons])
        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                self.weights [i][j] = np.random.rand()
        self.weights = self.weights * 2 - 1
        
  
    def Start_Simulation(self, displaySetting):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
    
    
        os.system('python3 simulate.py ' + displaySetting +' '+ str(self.myID)+' '+'2&>1'+ ' &')

    def Wait_For_Simulation_To_End(self):
        self.fileName = 'fitness'+str(self.myID)+'.txt'

        while not os.path.exists(self.fileName):
            time.sleep(0.01)

        f = open(self.fileName, "r")
        self.fitness = float(f.read())
        # print(self.fitness)
        f.close()

        os.system('rm ' +self.fileName)

        
        

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[c.x,c.y,c.z] , size=[c.length,c.width,c.height])       
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[c.length, c.width, c.height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1,0.2,0.2])
        pyrosim.End()


    def Create_Brain(self):
        self.brainName = "brain"+ str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(self.brainName)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")

        row = list(range(0,c.numSensorNeurons))
        col = list(range(0,c.numMotorNeurons))
        for currentRow in row:
            for currentColumn in col:
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        self.randRow = random.randint(0,c.numSensorNeurons-1)
        self.randCol = random.randint(0,c.numMotorNeurons-1)


        self.weights[self.randRow][self.randCol]= (np.random.rand()) *2 -1
    
    def Set_ID(self, nextID):
        self.myID = nextID + 1