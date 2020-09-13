import math
''' A program that computes various properties of a sphere '''

radius = input('Hello and welcome to my perfect sphere calculator, May I have a Radius?')
radius = float(radius)
d = (2*radius)
c = ((2*radius)*(math.pi))
a = ((4*(math.pi))*(radius**2))
v = ((4/3)*(math.pi)*(radius**3))

print("Diameter:", d,"Circumference:", c,"Area:", a,"Volume:", v)

#RS
