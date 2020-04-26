import random
import math
def randomWalk(steps):
    # define the initial coordinate
    x = 0
    y = 0
    z = 0
    # loop for deciding the step direction
    for i in range(0, steps):
        r = random.random()

        if r < 0.17:
            x = x - 1
        elif r < 0.33:
            x = x + 1
        elif r < 0.5:
            y = y - 1
        elif r < 0.67:
            y = y + 1
        elif r < 0.83:
            z = z - 1
        elif r < 1:
            z = z + 1
    print("x: "+str(x)+" y:"+str(y)+" z:"+str(z))
    # measure the distance
    dist = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    print("Distance: " + str(dist))
randomWalk(10000)