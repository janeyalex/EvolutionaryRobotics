
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

        pyrosim.Send_Joint(name="Torso_BackLeg1", parent="Torso", child="BackLeg1", type="revolute", position=[0.25, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLeg1", pos=[0, -0.5, 0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg2", parent="Torso", child="BackLeg2", type="revolute", position=[-0.25, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0, -0.5, 0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name="Torso_FrontLeg1", parent="Torso", child="FrontLeg1", type="revolute", position=[0.25, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg1", pos=[0, 0.5, 0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name="Torso_FrontLeg2", parent="Torso", child="FrontLeg2", type="revolute", position=[-0.25, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0, 0.5, 0], size=[0.2,1,0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg1", parent="Torso", child="LeftLeg1", type="revolute", position=[-0.5, 0.25, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg1", pos=[-0.5, 0, 0], size=[1,0.2,0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2", type="revolute", position=[-0.5, -0.25, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[-0.5, 0, 0], size=[1,0.2,0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg1", parent="Torso", child="RightLeg1", type="revolute", position=[0.5, 0.25, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg1", pos=[0.5, 0, 0], size=[1,0.2,0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2", type="revolute", position=[0.5, -0.25, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg2", pos=[0.5, 0, 0], size=[1,0.2,0.2])



        # pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[0, -0.5, 1], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="BackLeg", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        # pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        # pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute", position=[-0.5, 0, 1], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5, 0, 0], size=[1,0.2,0.2])
        # pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1,0.2,0.2])
        # pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        # pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        # pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        # pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis= "0 1 0")
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        pyrosim.End()


    def Create_Brain(self):
        self.brainName = "brain"+ str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(self.brainName)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg1")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLeg2")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLeg1")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "FrontLeg2")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LeftLeg1")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LeftLeg2")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLeg1")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLeg2")


        # pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron( name = 13 , jointName = "FrontLeg_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 14 , jointName = "BackLeg_BackLowerLeg")  
        # pyrosim.Send_Motor_Neuron( name = 15 , jointName = "RightLeg_RightLowerLeg") 
        # pyrosim.Send_Motor_Neuron( name = 16 , jointName = "LeftLeg_LeftLowerLeg")

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