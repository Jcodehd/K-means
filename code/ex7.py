import scipy.io as sc
from runKmeans import runKmeans;
from plotData import plotData;

# 加载数据
data = sc.loadmat('Machine Learning/K-means/ex7data2.mat');
X = data['X'];

# 设置聚类数、迭代次数
K = 3;
max_iters = 10;

# K-means
centroid, idx = runKmeans(X, K, max_iters);



# 画图输出
plotData(X, idx, centroid, K);











