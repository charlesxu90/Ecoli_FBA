from __future__ import print_function
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
# Usage python ./var_analysis.py ./var_heat_max.tsv heat
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

#plt.hist(mean_var_np, bins=80)
#plt.xlabel('Mean of Flux Variances')
#plt.ylabel('Frequency')
#plt.savefig('./bin80_mean_flux_' + save_f, dpi=100)
#
#plt.clf()
#plt.hist(var_var_np, bins=80)
#plt.xlabel('Variance of Flux Variances')
#plt.ylabel('Frequency')
#plt.savefig('./bin80_var_flux_' + save_f, dpi=100)

mean_sorted_idx = np.argsort(mean_var_np)
var_sorted_idx = np.argsort(var_var_np)
length = len(mean_var_np)

stop = False
if stop == True:
    sys.exit(0)

# Show genes in each 10 percent bin
mean_10_val = mean_var_np[mean_sorted_idx[length * 1 / 10]]
mean_20_val = mean_var_np[mean_sorted_idx[length * 2 / 10]]
mean_30_val = mean_var_np[mean_sorted_idx[length * 3 / 10]]
mean_40_val = mean_var_np[mean_sorted_idx[length * 4 / 10]]
mean_50_val = mean_var_np[mean_sorted_idx[length * 5 / 10]]
mean_60_val = mean_var_np[mean_sorted_idx[length * 6 / 10]]
mean_70_val = mean_var_np[mean_sorted_idx[length * 7 / 10]]
mean_80_val = mean_var_np[mean_sorted_idx[length * 8 / 10]]
mean_90_val = mean_var_np[mean_sorted_idx[length * 9 / 10]]

p10_mean_f = open('./p10_' + save_f + '.txt', 'w')
p20_mean_f = open('./p20_' + save_f + '.txt', 'w')
p30_mean_f = open('./p30_' + save_f + '.txt', 'w')
p40_mean_f = open('./p40_' + save_f + '.txt', 'w')
p50_mean_f = open('./p50_' + save_f + '.txt', 'w')
p60_mean_f = open('./p60_' + save_f + '.txt', 'w')
p70_mean_f = open('./p70_' + save_f + '.txt', 'w')
p80_mean_f = open('./p80_' + save_f + '.txt', 'w')
p90_mean_f = open('./p90_' + save_f + '.txt', 'w')
p100_mean_f = open('./p100_' + save_f + '.txt', 'w')

j = 1
for i in mean_sorted_idx:
    if mean_var_np[i] <= mean_10_val:
        print(strain[i][:-4] + '\t' + str(j), file=p10_mean_f)
    elif mean_var_np[i] <= mean_20_val:
        print(strain[i][:-4] + '\t' + str(j), file=p20_mean_f)
    elif mean_var_np[i] <= mean_30_val:
        print(strain[i][:-4] + '\t' + str(j), file=p30_mean_f)
    elif mean_var_np[i] <= mean_40_val:
        print(strain[i][:-4] + '\t' + str(j), file=p40_mean_f)
    elif mean_var_np[i] <= mean_50_val:
        print(strain[i][:-4] + '\t' + str(j), file=p50_mean_f)
    elif mean_var_np[i] <= mean_60_val:
        print(strain[i][:-4] + '\t' + str(j), file=p60_mean_f)
    elif mean_var_np[i] <= mean_70_val:
        print(strain[i][:-4] + '\t' + str(j), file=p70_mean_f)
    elif mean_var_np[i] <= mean_80_val:
        print(strain[i][:-4] + '\t' + str(j), file=p80_mean_f)
    elif mean_var_np[i] <= mean_90_val:
        print(strain[i][:-4] + '\t' + str(j), file=p90_mean_f)
    else:
        print(strain[i][:-4] + '\t' + str(j), file=p100_mean_f)
    j = j + 1
