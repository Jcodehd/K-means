from matplotlib.pyplot import *;
from matplotlib import markers
import numpy as np;

def plotData(X, idx, centroid, K):

    color = ['r', 'g', 'b'];

    fig, ax = subplots(figsize=(6,4));
    for i in range(K):

        pos_ = np.where(idx == i+1)[0];
        ax.scatter(X[pos_][:,:1], X[pos_][:,1:], c=color[i], marker='o');
    

    ax.scatter(centroid[:,:1], centroid[:,1:], c = 'black', marker='X');

    show();


