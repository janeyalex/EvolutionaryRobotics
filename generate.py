import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
#box 1 variables
length=1
width=1
height=1
x=0
y=0
z=0.5
#box 2 variables
#length1=1
#width1=1
#height1=1

#x1=1
#y1=1
#z1=1

#pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#pyrosim.Send_Cube(name="Box2", pos=[x1,y1,z1] , size=[length1,width1,height1])
for k in range(10):
    length = length*0.9
    width=width*0.9
    height=height*0.9
    for j in range(6):
        for i in range(6):
            pyrosim.Send_Cube(name="Box", pos=[i,j,k+0.5] , size=[length,width,height])
            #x=i
            #y=j
            #z=k+0.5

                
            
            
    
pyrosim.End()

            
