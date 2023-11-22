import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
z = 0
y = 0.5

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x-2,z+2,y], size=[length,width,height])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[x,z,y], size=[length,width,height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[x,z,y+0.5])
    pyrosim.Send_Cube(name="Link1", pos=[x,z,y], size=[length,width,height])
    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[x,z,y+0.5])
    pyrosim.Send_Cube(name="Link2", pos=[x,z,y], size=[length,width,height])
    pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[x+0.5,z,y])
    pyrosim.Send_Cube(name="Link3", pos=[x+1,z,y], size=[length,width,height])
    
    pyrosim.End()

Create_World()
Create_Robot()