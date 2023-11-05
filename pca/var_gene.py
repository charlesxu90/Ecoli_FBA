from __future__ import print_function
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
##################################
out_f = open('./var_ret.csv', 'w')
for filename in os.listdir('../temperatures/'):
    read_f = '../temperatures/' + filename
    try:
        dat = np.loadtxt(read_f, delimiter='\t', usecols=range(1,2584))
    except IndexError:
        print(filename + ' IndexError')
        continue
    
    # flux variances of each reaction
    var_rxn = np.var(dat, axis=0)
    mean_var = np.mean(var_rxn) # Mean of variances
    var_var = np.var(var_rxn)   # Variance of variances
    # Print gene ID, mean of variances, variances of variances into a file
    print(filename + "\t" + str("%0.2f" % mean_var) + "\t" + str("%0.2f" % var_var), file=out_f)
out_f.close()
