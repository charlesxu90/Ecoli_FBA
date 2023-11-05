from __future__ import print_function
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
##################################
suffix = sys.argv[1]
indir = sys.argv[2]
mut_no = int(sys.argv[3])

mut_var = np.empty([mut_no, 2583])
i = 0

out_f = open('./var_heat_' + suffix + '.tsv', 'w')
err_f = open('./var_heat_' + suffix + '.tsv.err', 'w')

for filename in os.listdir(indir):
    read_f = indir + filename
    try:
        dat = np.loadtxt(read_f, delimiter='\t', usecols=range(1,2584))
    except IndexError:
        print(filename, file=err_f)
        continue

    # flux standard deviation of each reaction
    var_rxn = np.std(dat, axis=0)

    mut_var[i] = var_rxn
    i = i + 1

    mean_var = np.mean(var_rxn) # Mean of variances
    var_var = np.var(var_rxn)   # Variance of variances
    # Print gene ID, mean of variances, variances of variances into a file
    print(filename + "\t" + str("%0.2f" % mean_var) + "\t" + str("%0.2f" % var_var), file=out_f)
out_f.close()
err_f.close()

#np.savetxt('heat_rxn_var.dat', mut_var, fmt='%10.3f', delimiter=',')
###################################################
## Count frequency within 80 bins for 1241 mutants #
#binsize = 80
#varmax = np.amax(mut_var)
#varmin = np.amin(mut_var)
#interval = (varmax - varmin) / binsize
#
#frequency = np.zeros([1241, 80], dtype=int)
#
#for i in range(0, 1241):
#    row = np.sort(mut_var[i, :])
#    k = 0
#    for j in range(0, 2583):
#        if ((row[j] >= varmin + k * interval) and (row[j] < varmin + (k + 1) * interval)):
#            frequency[i, k] = frequency[i, k] + 1
#        else:
#            k = k + 1
#            frequency[i, k] = frequency[i, k] + 1
#np.savetxt('heat_frequency.dat', frequency, fmt='%i', delimiter=',')
