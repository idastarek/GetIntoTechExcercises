import math
g = 9.81
v = 44
theta = 80*(math.pi/180)
x = 0.5
y = 1
print(y + x*math.tan(theta)-(g*x**2/(2*(v*math.cos(theta)**2))))


z = float(input("Please enter a value: "))
u = float(input("Please enter a value: "))
print(z+u)