import numpy as np
import random

def kMeansInitCentroids(X, K):

    m = X.shape[0];
    n = X.shape[1];

    centroids = np.zeros((K, n));

    randidx = random.sample(range(m), K);

    centroids = X[randidx,:];

    return centroids;
