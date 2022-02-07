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
     
    # pyrosim.Send_Cube(name="Link_0", pos=[0,0,0.5] , size=[length,width,height])
    # pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link_0" , child = "Link_1" , type = "revolute", position = [0,0,1])
    # pyrosim.Send_Cube(name="Link_1", pos=[0,0,0.5] , size=[length,width,height])
    # pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link_1" , child = "Link_2" , type = "revolute", position = [0,0,1])
    # pyrosim.Send_Cube(name="Link_2", pos=[0,0,0.5] , size=[length,width,height])
    # pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link_2" , child = "Link_3" , type = "revolute", position = [0,0.5,0.5])
    # pyrosim.Send_Cube(name="Link_3", pos=[0,0.5,0] , size=[length,width,height])
    # pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link_3" , child = "Link_4" , type = "revolute", position = [0,1,0])
    # pyrosim.Send_Cube(name="Link_4", pos=[0,0.5,0] , size=[length,width,height])
    # pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link_4" , child = "Link_5" , type = "revolute", position = [0,0.5,-0.5])
    # pyrosim.Send_Cube(name="Link_5", pos=[0,0,-0.5] , size=[length,width,height])
    # pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link_5" , child = "Link_6" , type = "revolute", position = [0,0,-1])
    # pyrosim.Send_Cube(name="Link_6", pos=[0,0,-0.5] , size=[length,width,height])
    
    pyrosim.Send_Cube(name="Torso", pos=[0,0,1.5] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [-0.5,0,1])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.5,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5] , size=[length,width,height])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5] , size=[length,width,height]) 

 
    pyrosim.End()

Create_World()
Create_Robot()