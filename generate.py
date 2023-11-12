import pyrosim.pyrosim as pyrosim
length = 1
width = 1
height = 1
x = 0
z = 0
y = 0.5
pyrosim.Start_SDF("boxes.sdf")
for i in range(10):
    pyrosim.Send_Cube(name="Box", pos=[x,z,y] , size=[length,width,height])
    y = y + height/2
    length = length * 0.9
    width = width * 0.9
    height = height * 0.9
    y = y + height/2
pyrosim.End()