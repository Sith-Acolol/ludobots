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
    pyrosim.Send_Cube(name="Torso", pos=[x,z,y+1], size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[x-0.5,z,y+0.5])
    pyrosim.Send_Cube(name="BackLeg", pos=[x-0.5,z,y-1], size=[length,width,height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[x+0.5,z,y+0.5])
    pyrosim.Send_Cube(name="FrontLeg", pos=[x+0.5,z,y-1], size=[length,width,height])

    pyrosim.End()

# Create_World()
Create_Robot()