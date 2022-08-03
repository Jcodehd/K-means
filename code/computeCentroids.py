import numpy as np;


def computeCentroids(X, idx, K):
    X = np.mat(X);

    m = X.shape[0];
    n = X.shape[1];


    centroids = np.zeros((K, n));

    for i in range(K):

        pos_ = np.where(idx == i+1)[0];

        centroids[i,:] =  np.mean(X[pos_], axis=0);

    return centroids;

