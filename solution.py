
import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        # self.weights = np.empty([c.numSensorNeurons,c.numMotorNeurons])
        # for i in range(c.numSensorNeurons):
        #     for j in range(c.numMotorNeurons):
        #         self.weights [i][j] = np.random.rand()
        # self.weights = self.weights * 2 - 1

        # Weights for sensor neurons
        self.sensorWeights = np.empty([c.numSensorNeurons,c.numHiddenNeurons])
        for i in range(c.numSensorNeurons):
            for j in range(c.numHiddenNeurons):
                self.sensorWeights [i][j] = np.random.rand()
        self.sensorWeights = self.sensorWeights * 2 - 1

        # Weights for Motor neurons
        self.motorWeights = np.empty([c.numMotorNeurons,c.numHiddenNeurons])
        for i in range(c.numMotorNeurons):
            for j in range(c.numHiddenNeurons):
                self.motorWeights [i][j] = np.random.rand()
        self.motorWeights = self.sensorWeights * 2 - 1
  
    def Start_Simulation(self, displaySetting):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
    
    
        os.system('python3 simulate.py ' + displaySetting +' '+ str(self.myID)+' '+'2&>1'+ ' &')
        # os.system('python3 simulate.py ' + displaySetting +' '+ str(self.myID)+ ' &')

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
        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute", position=[0.5, 0, 1], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5, 0, 0], size=[1,0.2,0.2])
        pyrosim.Send_Joint(name="FrontLeg_FrontLowerLeg", parent="FrontLeg", child="FrontLowerLeg", type="revolute", position=[0, 1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="BackLeg_BackLowerLeg", parent="BackLeg", child="BackLowerLeg", type="revolute", position=[0, -1, 0], jointAxis= "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="RightLeg_RightLowerLeg", parent="RightLeg", child="RightLowerLeg", type="revolute", position=[1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        pyrosim.Send_Joint(name="LeftLeg_LeftLowerLeg", parent="LeftLeg", child="LeftLowerLeg", type="revolute", position=[-1, 0, 0], jointAxis= "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0, 0, -0.5], size=[0.2,0.2,1])
        pyrosim.End()


    def Create_Brain(self):
        self.brainName = "brain"+ str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(self.brainName)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftLowerLeg")

        pyrosim.Send_Hidden_Neuron( name = 9 )


        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "BackLeg_BackLowerLeg")  
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_RightLowerLeg") 
        pyrosim.Send_Motor_Neuron( name = 17 , jointName = "LeftLeg_LeftLowerLeg")

        # row = list(range(0,c.numSensorNeurons))
        # col = list(range(0,c.numMotorNeurons))
        # for currentRow in row:
        #     for currentColumn in col:
        #         pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

        # send synapse from all sensor neurons to hidden neuron
        sRow = list(range(0,c.numSensorNeurons))
        mRow = list(range(0,c.numMotorNeurons))
        col = list(range(0,c.numHiddenNeurons))

        for currentRow in sRow:
            for currentColumn in col:
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=c.numSensorNeurons, weight=self.sensorWeights[currentRow][currentColumn])

        # send synapse from hidden neuron to all motor neurons
        for currentRow in mRow:
            for currentColumn in col:
                pyrosim.Send_Synapse(sourceNeuronName=c.numSensorNeurons, targetNeuronName=currentRow+c.numSensorNeurons+c.numHiddenNeurons, weight=self.motorWeights[currentRow][currentColumn])

        pyrosim.End()

        
    

    def Mutate(self):
        # self.randRow = random.randint(0,c.numSensorNeurons-1)
        # self.randCol = random.randint(0,c.numMotorNeurons-1)

        # self.weights[self.randRow][self.randCol]= (np.random.rand()) *2 -1

        #mutate first matrix with sensor neurons to hidden neuron
        self.sensRandRow = random.randint(0,c.numSensorNeurons-1)
        self.sensorWeights[self.sensRandRow][0]= (np.random.rand()) *2 -1

        #mutate second matrix with hidden neuron to motor neurons
        self.motorRandRow = random.randint(0,c.numMotorNeurons-1)
        self.motorWeights[self.motorRandRow][0]= (np.random.rand()) *2 -1
    
    def Set_ID(self, nextID):
        self.myID = nextID + 1