from pandas import array
import scipy.io as sc
import numpy as np;
from runKmeans import runKmeans;
from PIL import Image;
# 加载数据

data = sc.loadmat('Machine Learning/K-means/bird_small.mat');
X = data['A']/255;

m = X.shape[0];
n = X.shape[1];

# 设置参数
K = 16; 
max_iters = 10;

X = np.reshape(X, (m*n, 3));


centroids, idx = runKmeans(X, K, max_iters);


for i in range(K):
    pos_ = np.where(idx == i+1)[0];

    X[pos_] = centroids[i, ];

X = np.reshape(X, (m, n, 3))*255;



image = Image.fromarray(np.uint8(X));
image = image.resize((520,520));

image.show();


