import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    #box 1 variables
    length=1
    width=1
    height=1
    x=1
    y=2
    z=0.5
   # pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])       
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    length=1
    width=1
    height=1
     
    
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,1])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[length,width,height])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length,width,height]) 

 
    pyrosim.End()

Create_World()
Create_Robot()