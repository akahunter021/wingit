import math

h = int(input("enter the height : \n"))

r = int(input("enter the radius : \n"))

c = h * r**2 * math.pi
c = str(c)
t = 2 * math.pi * r * h + 2 * (math.pi * (r)**2)
t = str(t)
print(c + " is the capacity .")
print(t + " is the total area volume .")