import numpy as np;
from findClosestCentroids import findClosestCentroids;
from computeCentroids import computeCentroids;
from kMeansInitCentroids import kMeansInitCentroids;

def runKmeans(X, K, max_iters):
    X = np.mat(X);

    init_centroids = kMeansInitCentroids(X, K);

    for i in range(max_iters):

        idx = findClosestCentroids(X, init_centroids);

        init_centroids = computeCentroids(X, idx, K);


    return init_centroids, idx;