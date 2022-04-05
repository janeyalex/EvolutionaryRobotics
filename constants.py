import numpy as np

length = 1
width = 1
height =1

x = -2.5
y = 2.5
z = 0.5

#back leg variables
amplitudeBack = np.pi/6
frequencyBack = 50
phaseOffsetBack = np.pi/4

#front leg variables
amplitudeFront = np.pi/6
frequencyFront = 10
phaseOffsetFront = -(3/2)*np.pi

maxForce = 25

numberOfGenerations = 10

numTimeSteps = 1000

sleep = 1/2000

populationSize = 15

numSensorNeurons = 13

numMotorNeurons = 12

motorJointRange = 0.1