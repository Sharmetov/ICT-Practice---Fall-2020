import math

s = int(input())
n = int(input())

area = (n*s**2)/(4*math.tan(math.pi/n))

print(area)
