from __future__ import print_function
import csv
import sys
import matplotlib.pyplot as plt
import gene2React
import numpy as np
from sklearn.decomposition import PCA
##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
##################################
read_f = '../temperatures/ECK2194-NAPC.txt'
#conditions = 
dat = np.loadtxt(read_f, delimiter='\t', usecols=range(1,2584))
pca = PCA(n_components=2583)
ret = pca.fit(dat).transform(dat)
print('explained variance ratio: %s'
              % str(pca.explained_variance_ratio_))
print(len(ret), len(ret[0]))

pca = PCA(n_components=7)
ret = pca.fit(np.transpose(dat)).transform(np.transpose(dat))
print('explained variance ratio: %s'
              % str(pca.explained_variance_ratio_))
print(len(ret), len(ret[0]))
#plt.figure()
#for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
#    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], c=c, label=target_name)
#plt.legend()
#plt.title('PCA of flux dataset')
#
#plt.show()

