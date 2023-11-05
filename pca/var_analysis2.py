from __future__ import print_function
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
##################################
read_f = sys.argv[1]
save_f = sys.argv[2]    # Suffix of saving file

#============================#
strain = []
mean_var = []
var_var = []

with open(read_f, 'r') as f:
    for line in f:
        dline = line.strip('\r\n').split('\t')
        strain.append(dline[0])
        mean_var.append(dline[1])
        var_var.append(dline[2])
f.close()
#============================#
mean_var_np = np.array([np.float64(v) for v in mean_var])
var_var_np = np.array([np.float64(v) for v in var_var])

plt.hist(mean_var_np, bins=30)
plt.xlabel('Mean of Flux Variances')
plt.ylabel('Frequency')
plt.savefig('./mean_var_' + save_f, dpi=100)

plt.clf()
plt.hist(var_var_np, bins=30)
plt.xlabel('Variance of Flux Variances')
plt.ylabel('Frequency')
plt.savefig('./var_var_' + save_f, dpi=100)

# Find overlapp in top 10 percent
mean_var_npsort = np.sort(mean_var_np)
var_var_npsort = np.sort(var_var_np)
length = len(mean_var_np)
mean_tenth_val = mean_var_npsort[length * 9 / 10 - 1]
var_tenth_val = var_var_npsort[length * 9 / 10 - 1]


comm_f = open('./mean_comm_' + save_f + '.txt', 'w')
mean_f = open('./mean_uniq_' + save_f + '.txt', 'w')
var_f = open('./var_uniq_' + save_f + '.txt', 'w')

for i in range(0, length):
    if mean_var_np[i] >= mean_tenth_val and var_var_np[i] >= var_tenth_val:
        print(strain[i], file=comm_f)
    elif mean_var_np[i] >= mean_tenth_val:
        print(strain[i], file=mean_f)
    elif var_var_np[i] >= var_tenth_val:
        print(strain[i], file=var_f)
