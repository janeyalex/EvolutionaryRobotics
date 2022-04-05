
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

        #pyrosim.Send_Joint(name="Torso_BackLeg1", parent="Torso", child="BackLeg1", type="revolute", position=[0.25, -0.5, 1], jointAxis= "1 0 0")
        #pyrosim.Send_Cube(name="BackLeg1", pos=[0, -0.5, 0], size=[0.2,1,0.2])

        #changed from position=[-0.25, -0.5, 1] to position=[0, -0.5, 1]
        pyrosim.Send_Joint(name="Torso_BackLeg2", parent="Torso", child="BackLeg2", type="revolute", position=[0, -0.5, 1], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0, -0.5, 0], size=[0.2,1,0.2])

        # pyrosim.Send_Joint(name="Torso_FrontLeg1", parent="Torso", child="FrontLeg1", type="revolute", position=[0.25, 0.5, 1], jointAxis = "1 0 0")
        # pyrosim.Send_Cube(name="FrontLeg1", pos=[0, 0.5, 0], size=[0.2,1,0.2])

        #changed from position=[-0.25, -0.5, 1] to position=[0, -0.5, 1]
        pyrosim.Send_Joint(name="Torso_FrontLeg2", parent="Torso", child="FrontLeg2", type="revolute", position=[0, 0.5, 1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0, 0.5, 0], size=[0.2,1,0.2])

        #changed pos from [-0.5,0.25,1]
        pyrosim.Send_Joint(name="Torso_LeftLeg1", parent="Torso", child="LeftLeg1", type="revolute", position=[-0.5, 0.25, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg1", pos=[-0.5, 0, 0], size=[1,0.2,0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2", type="revolute", position=[-0.5, -0.25, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[-0.5, 0, 0], size=[1,0.2,0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg1", parent="Torso", child="RightLeg1", type="revolute", position=[0.5, 0.25, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg1", pos=[0.5, 0, 0], size=[1,0.2,0.2])

        #changed pos from [-0.5,-0.25,1]
        pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2", type="revolute", position=[0.5, -0.25, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg2", pos=[0.5, 0, 0], size=[1,0.2,0.2])

        # pyrosim.Send_Joint(name="FrontLeg1_FrontLowerLeg1", parent="FrontLeg1", child="FrontLowerLeg1", type="revolute", position=[0, 1, 0], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="FrontLowerLeg1", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="FrontLeg2_FrontLowerLeg2", parent="FrontLeg2", child="FrontLowerLeg2", type="revolute", position=[0, 1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg2", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        # pyrosim.Send_Joint(name="BackLeg1_BackLowerLeg1", parent="BackLeg1", child="BackLowerLeg1", type="revolute", position=[0, -1, 0], jointAxis= "1 0 0")
        # pyrosim.Send_Cube(name="BackLowerLeg1", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="BackLeg2_BackLowerLeg2", parent="BackLeg2", child="BackLowerLeg2", type="revolute", position=[0, -1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg2", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="RightLeg1_RightLowerLeg1", parent="RightLeg1", child="RightLowerLeg1", type="revolute", position=[1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg1", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="RightLeg2_RightLowerLeg2", parent="RightLeg2", child="RightLowerLeg2", type="revolute", position=[1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="LeftLeg1_LeftLowerLeg1", parent="LeftLeg1", child="LeftLowerLeg1", type="revolute", position=[-1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg1", pos=[0, 0, -0.5], size=[0.2,0.2,1])

        pyrosim.Send_Joint(name="LeftLeg2_LeftLowerLeg2", parent="LeftLeg2", child="LeftLowerLeg2", type="revolute", position=[-1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0, 0, -0.5], size=[0.2,0.2,1])

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
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg1")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg2")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLeg1")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg2")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg1")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "LeftLeg2")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "RightLeg1")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "RightLeg2")
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "FrontLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "FrontLowerLeg2")
        # pyrosim.Send_Sensor_Neuron(name = 9, linkName = "BackLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name = 8, linkName = "BackLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name = 9, linkName = "RightLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name = 10, linkName = "RightLowerLeg2")
        pyrosim.Send_Sensor_Neuron(name = 11, linkName = "LeftLowerLeg1")
        pyrosim.Send_Sensor_Neuron(name = 12, linkName = "LeftLowerLeg2")

        # pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_BackLeg1")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_BackLeg2")
        # pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_FrontLeg1")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "Torso_FrontLeg2")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "Torso_LeftLeg1")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "Torso_LeftLeg2")
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "Torso_RightLeg1")
        pyrosim.Send_Motor_Neuron( name = 18 , jointName = "Torso_RightLeg2")
        # pyrosim.Send_Motor_Neuron( name = 19 , jointName = "FrontLeg1_FrontLowerLeg1")
        pyrosim.Send_Motor_Neuron( name = 19 , jointName = "FrontLeg2_FrontLowerLeg2")
        # pyrosim.Send_Motor_Neuron( name = 21 , jointName = "BackLeg1_BackLowerLeg1")
        pyrosim.Send_Motor_Neuron( name = 20 , jointName = "BackLeg2_BackLowerLeg2")
        pyrosim.Send_Motor_Neuron( name = 21 , jointName = "RightLeg1_RightLowerLeg1")
        pyrosim.Send_Motor_Neuron( name = 22 , jointName = "RightLeg2_RightLowerLeg2") 
        pyrosim.Send_Motor_Neuron( name = 23 , jointName = "LeftLeg1_LeftLowerLeg1")
        pyrosim.Send_Motor_Neuron( name = 24 , jointName = "LeftLeg2_LeftLowerLeg2") 


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