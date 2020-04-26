from mpi4py import MPI
import random
import numpy as np
import math

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
p = comm.Get_size()

def randomwalk(stepSize):
    # here we are setting the number of steps we have to take
    steps = stepSize
    # divide the steps by number of available process p
    fract = steps/p


    # here process with rank other than '0' are receiving (x,y,z) from process '0'

    x, y, z = [0,0,0]
    message = "Hello from "+str(my_rank)
    # condition to check whether this piece is the final fraction  or not
    if steps < (my_rank * fract) + fract:
        # define the range
        rang = range(((my_rank * fract)+1), steps + 1)
    else:
        # define the range
        rang = range((my_rank * fract)+1, (my_rank * fract) + fract + 1)
    # loop for deciding the step direction
    for i in rang:
        # choose r randomly before taking steps
        r = random.random()
        print(str(r))
        # decision for taking step
        if r < 0.17:
            x = x-1
        elif r < 0.33:
            x = x+1
        elif r < 0.5:
            y = y-1
        elif r < 0.67:
            y = y+1
        elif r < 0.83:
            z = z-1
        elif r < 1:
            z = z+1

        print(str(x)+" "+str(y)+" "+str(z))
    # reduce (x,y,z) to sum
    sum = comm.reduce([x, y, z], op=MPI.SUM, root=0)
    if my_rank == 0:
        # measure the distance
        dist = math.sqrt(sum[0] ** 2 + sum[1] ** 2 + sum[2] ** 2)
        # print the distance
        print(str(sum[0])+" "+str(sum[1])+" "+str(sum[2]))
        print("Distance: "+str(dist))
randomwalk(1000)

