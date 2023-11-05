from __future__ import print_function
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
##################################
# Usage: python ./var_gene.py 
out_f = open('./flux_var.csv', 'w')
mut_var = np.empty([1241, 2583])
i = 0
for filename in os.listdir('../temperatures/'):
    read_f = '../temperatures/' + filename
    try:
        dat = np.loadtxt(read_f, delimiter='\t', usecols=range(1,2584))
    except IndexError:
        print(filename + ' IndexError')
        continue
    
    # flux variances of each reaction
    var_rxn = np.var(dat, axis=0)
    mut_var[i] = var_rxn
    i = i + 1
    plt.clf()
    plt.hist(var_rxn, bins=80)
    plt.xlabel('Flux Variances')
    plt.ylabel('Frequency')
    plt.savefig('./var_plt/' + filename + '.png', dpi=100)


    mean_var = np.mean(var_rxn) # Mean of variances
    var_var = np.var(var_rxn)   # Variance of variances
    # Print gene ID, mean of variances, variances of variances into a file
    print(filename + "\t" + str("%0.2f" % mean_var) + "\t" + str("%0.2f" % var_var), file=out_f)
out_f.close()

np.savetxt('var_plt.dat', mut_var, fmt='%10.3f', delimiter=',')

###################################################
# Count frequency within 80 bins for 1241 mutants #
binsize = 80
varmax = np.amax(mut_var)
varmin = np.amin(mut_var)
interval = (varmax - varmin) / binsize

frequency = np.zeros([1241, 80], dtype=int)

for i in range(0, 1241):
    row = np.sort(mut_var[i, :])
    k = 0
    for j in range(0, 2583):
        if ((row[j] >= varmin + k * interval) and (row[j] < varmin + (k + 1) * interval)):
            frequency[i, k] = frequency[i, k] + 1
        else:
            k = k + 1
            frequency[i, k] = frequency[i, k] + 1
    #
np.savetxt('frequency.dat', frequency, fmt='%i', delimiter=',')

