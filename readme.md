# To run these file in Cluster
First: scp the file to corresponding master cluster, in our case it is tardis. 

Second: ssh to the master cluster and go to the directory where the files have been transferred. Run the commands given below.

# Run this command for Random Walk Reduce using 2 cluster, you can replace 2 with your desired number of cluster
 mpiexec -n 2 python randomWalkReduce.py

# Run this command for Random Walk implemented using Send and Receive using 2 cluster, you can replace 2 with your desired number of cluster
 mpiexec -n 2 python randomWalkP2P.py

# Run this command for Random Walk Sequential 
 python randomWalk.py

# If you want to change the number of steps then open the designated file and change this line:
randomwalk(1000)

# Output
You will observe the output in terminal

