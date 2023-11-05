from __future__ import print_function
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
##################################
# Explain:  read from gene.max files, get mean of variances
# Author:   xiaopeng xu
# Email:    charlesxu90@gmail.com
# Usage:    python ./var_gene_high.py high high_max/ 1246
##################################
suffix = sys.argv[1]
indir = sys.argv[2]
mut_no = int(sys.argv[3])

mut_var = np.empty([mut_no, 2583])
i = 0

out_f = open('./var_high_' + suffix + '.tsv', 'w')
err_f = open('./var_high_' + suffix + '.tsv.err', 'w')

for filename in os.listdir(indir):
    read_f = indir + filename
    try:
        dat = np.loadtxt(read_f, delimiter='\t', usecols=range(1,2584))
    except IndexError:
        print(filename, file=err_f)
        continue

    # flux variances of each reaction
    var_rxn = np.var(dat, axis=0)

    mut_var[i] = var_rxn
    i = i + 1

    mean_var = np.mean(var_rxn) # Mean of variances
    var_var = np.var(var_rxn)   # Variance of variances
    # Print gene ID, mean of variances, variances of variances into a file
    print(filename[:-4] + "\t" + str("%0.2f" % mean_var) + "\t" + str("%0.2f" % var_var), file=out_f)
out_f.close()
err_f.close()

# Remove empty reactions from consideration
zero_check = np.zeros(len(mut_var))
idx = []
for i in range(0, len(mut_var[0])):
    if not np.array_equal(mut_var[:, i], zero_check):
        idx.append(i)
print(len(idx))
mut_var = mut_var[:, idx]

np.savetxt('high_rxn_var.dat', mut_var, fmt='%10.3f', delimiter=',')

###################################################
# Count frequency within 80 bins for mutants #
# binsize = 80
# varmax = np.amax(mut_var)
# varmin = np.amin(mut_var)
# interval = (varmax - varmin) / binsize
# 
# frequency = np.zeros([mut_no, 80], dtype=int)
# 
# for i in range(0, mut_no):
#     row = np.sort(mut_var[i, :])
#     k = 0
#     for j in range(0, 2583):
#         if ((row[j] >= varmin + k * interval) and (row[j] < varmin + (k + 1) * interval)):
#             frequency[i, k] = frequency[i, k] + 1
#         else:
#             k = k + 1
#             frequency[i, k] = frequency[i, k] + 1
# np.savetxt('high_frequency.dat', frequency, fmt='%i', delimiter=',')
