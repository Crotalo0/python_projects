import math
import random

pi = math.pi
print("pi-greco from math library:",pi)

#pi approximation (found on https://en.wikipedia.org/wiki/Approximations_of_%CF%80)
#counting the points falling inside of a quarter of a circle
#As points are randomly scattered inside the unit square, some fall within the unit circle. The fraction of points inside the circle over all points approaches pi/4 as the number of points goes toward infinity

counter = 0
n = int(input("How many points we want compute: "))
for i in range(n):
    x = random.uniform(-1,1)    #generating random x y coordinates of points
    y = random.uniform(-1,1)    #.uniform gives us floats
    if (math.sqrt((x**2)+(y**2)) )<= 1:  #if the (x,y) generated falls into the circle, i add +1 to a counter
        counter = counter + 1

pi_test = 4*counter/n
print("Pi approximation:",pi_test)


