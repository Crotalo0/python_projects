import math

En = 10**25
v = 20000
r = 7

m = 2*En/(v**2)
print(f"{m} kg")

volume = (4*(r**3)*math.pi)/4
print(f"{volume} km^3")

d = m/volume
print(f"{d} kg/km^3")
