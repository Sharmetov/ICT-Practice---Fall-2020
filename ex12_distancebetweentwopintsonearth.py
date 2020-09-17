import math
print("Enter a latitude:")
t1, g1 = map(int, input().split())
print("Enter a longtitude:")
t2, g2 = map(int, input().split())
distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print(distance)
