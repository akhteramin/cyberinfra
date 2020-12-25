import numpy as np
import pickle
import sys
import time
from numpy.linalg import norm
from pyspark.shell import sc
# import matplotlib.pyplot as plt

# Number of centroids
K = 3
# Number of K-means runs that are executed in parallel. Equivalently, number of sets of initial points
RUNS = 5
# For reproducability of results
RANDOM_SEED = 100
# The K-means algorithm is terminated when the change in the
# location of the centroids is smaller than 0.1
converge_dist = 0.1
def parse_data(row):
    # Parse each pandas

    return (row[0],
            np.concatenate([row[1], row[2], row[3]]))

def choice(p):

    # Generates a random sample
    random = np.random.random()
    r = 0.0
    for idx in range(len(p)):
        r = r + p[idx]
        if r > random:
            return idx
    assert (False)

def kmeans_init(rdd, K, RUNS, seed):

    # Select RUNS sets of initial points

    shape = rdd.take(1)[0][1].shape[0]
    centers = np.zeros((RUNS, K, shape))
    def update_dist(vec, dist, k):
        new_dist = norm(vec - centers[:, k], axis=1)**2
        return np.min([dist, new_dist], axis=0)
    # The second element `dist` in the tuple below is the
    # closest distance from each data point to the selected
    # points in the initial set, where `dist[i]` is the
    # closest distance to the points in the i-th initial set
    data = (rdd
            .map(lambda p: (p, [np.inf] * RUNS)) \
            .cache())
    # Collect the feature vectors of all data points
    # for-loop
    print(data)
    local_data = (rdd
                    .map(lambda (name, vec): vec)
                    .collect())
    # Randomly select the first point for every run of
    sample = [local_data[k] for k in
        np.random.randint(0, len(local_data), RUNS)]
    centers[:, 0] = sample
    for idx in range(K - 1):

        #Update distance
        data = (data
            .map(lambda ((name,vec),dist):
                    ((name,vec),update_dist(vec,dist,idx)))
            .cache())
        #Calculate sum of D_i(x)^2
        d1 = data.map(lambda ((name,vec),dist): (1,dist))
        d2 = d1.reduceByKey(lambda x,y: np.sum([x,y], axis=0))
        total = d2.collect()[0][1]
        #Normalize each distance to get the probabilities and
        #reshapte to 12140x25
        prob = (data
            .map(lambda ((name,vec),dist):
                np.divide(dist,total))
            .collect())
        prob = np.reshape(prob,(len(local_data), RUNS))
        #K'th centroid for each run
        data_id = [choice(prob[:,i]) for i in xrange(RUNS)]
        sample = [local_data[i] for i in data_id]
        centers[:, idx+1] = sample
    return centers


def get_closest(p, centers):
    # Return the indices the nearest centroids of point p.

    best = [0] * len(centers)
    closest = [np.inf] * len(centers)
    for idx in range(len(centers)):
        for j in range(len(centers[0])):
            temp_dist = norm(p - centers[idx][j])
            if temp_dist < closest[idx]:
                closest[idx] = temp_dist
                best[idx] = j
    return best

def kmeans(rdd, K, RUNS, converge_dist, seed):

    # Run K-means algorithm on rdd, where `RUNS` is the number of initial sets to use.

    k_points = kmeans_init(rdd, K, RUNS, seed)
    temp_dist = 1.0

    iters = 0
    while temp_dist > converge_dist:
        # Update all `RUNS` sets of centroids using standard k-means
        temp_dist = np.max([
            np.sum([norm(k_points[idx][j] - new_points[(idx,
                                                        j)]) for idx, j in new_points.keys()])
        ])

        iters = iters + 1

        # update old centroids
        # You modify this for-loop to meet your need
        for ((idx, j), p) in new_points.items():
            k_points[idx][j] = p

    return k_points

## Read data
data = pickle.load(open("stations_projections.pickle", "rb"))
print(data)
rdd = sc.parallelize([parse_data(row[1])
          for row in data.iterrows()])
rdd.take(1)
np.random.seed(RANDOM_SEED)
centroids = kmeans(rdd, K, RUNS, converge_dist,
                   np.random.randint(1000))
group = rdd.mapValues(lambda p: get_closest(p, centroids)) \
           .collect()
