from world import WORLD
from robot import ROBOT
import pybullet as p 
import pybullet_data
import pyrosim.pyrosim as pyrosim
from time import sleep

class SIMULATION:
    def __init__(self):
        
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)
        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)

    def Run(self):
        for i in range(1000):
            #print(i)
             sleep(1/100)
             p.stepSimulation()
        #     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
        #     frontLegSensorValues[i]= pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
        #     pyrosim.Set_Motor_For_Joint(
        #         bodyIndex = robotId,
        #         jointName = "Torso_BackLeg",
        #         controlMode = p.POSITION_CONTROL,
        #         targetPosition = targetAnglesBack[i],
        #         maxForce = c.maxForce)
            
        #     pyrosim.Set_Motor_For_Joint(
        #         bodyIndex = robotId,
        #         jointName = "Torso_FrontLeg",
        #         controlMode = p.POSITION_CONTROL,
        #         targetPosition = targetAnglesFront[i],
        #         maxForce = c.maxForce)
        
    def __del__(self):
        p.disconnect()


    