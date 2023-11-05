from __future__ import print_function
import sys
import matplotlib.pyplot as plt
import numpy as np
##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
##################################
read_f = './var_ret.csv'
dat = np.loadtxt(read_f, delimiter='\t', usecols=range(1,3))
print(len(dat), len(dat[0]))
plt.plot(dat[:, 0])
plt.savefig('./mean_var.png', dpi=100)
plt.clf()
plt.plot(dat[:,1])
plt.savefig('./var_var.png',dpi=100)
