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
    fract = steps/(p-1)

    if my_rank != 0:
        # here process with rank other than '0' are receiving (x,y,z) from process '0'
        x, y, z = [0,0,0]
        message = "Hello from "+str(my_rank)
        # condition to check whether this piece is the final fraction  or not
        if steps < (my_rank-1) * fract + fract:
            # define the range
            rang = range((my_rank-1) * fract, steps)
        else:
            # define the range
            rang = range((my_rank-1) * fract, (my_rank-1) * fract + fract)
        # loop for deciding the step direction
        for i in rang:
            # random.seed(seed)
            r = random.random()
            print(str(r))
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

        # sending the (x,y,z) to process 0
        comm.send([x, y, z], dest=0)
    else:
        # ans is the container of x,y,z
        final_dest = [0, 0, 0]
        sum_vector = np.array(final_dest)
        # for loop to send and receive all response from other process
        for procid in range(1, p):

            # receive (x,y,z) to from process
            ans = comm.recv(source=procid)
            vector2 = np.array(ans)
            sum_vector = sum_vector + vector2

        print(sum_vector)
        dist = math.sqrt(sum_vector[1] ** 2 + sum_vector[2] ** 2 + sum_vector[2] ** 2)

        print("Distance: "+str(dist))
randomwalk(1000)

