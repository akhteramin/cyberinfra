import numpy as np
import pickle
import sys
import time
from numpy.linalg import norm
from pyspark.shell import sc
import matplotlib.pyplot as plt


def parse_data(row):
    '''
    Parse each pandas row into a tuple of
    (station_name,  feature_vec),`l
    where feature_vec is the concatenation of the projection vectors
    of TAVG, TRANGE, and SNWD.
    '''
    return (row[0],
            np.concatenate([row[1], row[2], row[3]]))
## Read data
data = pickle.load(open("stations_projections.pickle", "rb"))
rdd = sc.parallelize([parse_data(row[1])
          for row in data.iterrows()])
rdd.take(1)
# Number of centroids
K = 5
# Number of K-means runs that are executed in parallel. Equivalently, number of sets of initial points
RUNS = 25
# For reproducability of results
RANDOM_SEED = 60295531
# The K-means algorithm is terminated when the change in the
# location of the centroids is smaller than 0.1
converge_dist = 0.1