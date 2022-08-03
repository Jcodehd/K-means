import numpy as np;
import scipy.spatial.distance 


def findClosestCentroids(X, Centroids):
    X = np.mat(X);

    m = X.shape[0];

    idx = np.zeros(m);


    for i in range(m):

        distance_ = np.sum(np.power((Centroids-X[i, :]),2), axis=1);

        if len(np.where(distance_ == np.min(distance_, axis=0))[0]) == 1:
            idx[i] = np.where(distance_ == np.min(distance_, axis=0))[0]+1;
        
        else:
            idx[i] = np.where(distance_ == np.min(distance_, axis=0))[0][0]+1
    
    return idx;

