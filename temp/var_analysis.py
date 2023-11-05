from __future__ import print_function
import sys
import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
##################################
read_f = sys.argv[1]
save_f = sys.argv[2]    # Suffix of saving file

# Usage python ./var_analysis.py ./var_heat_max.tsv heat

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

plt.figure(figsize=(16,8))
plt.hist(mean_var_np, bins=80)
plt.xlabel('Mean of Flux Variances')
plt.ylabel('Frequency')

font = {
#        'family' : 'normal',
#        'weight' : 'bold',
        'size'   : 34}

matplotlib.rc('font', **font)

plt.savefig('./bin80_mean_flux_' + save_f + '.svg', dpi=100)

plt.clf()
plt.hist(var_var_np, bins=80)
plt.xlabel('Variance of Flux Variances')
plt.ylabel('Frequency')

matplotlib.rc('font', **font)


plt.savefig('./bin80_var_flux_' + save_f + '.svg', dpi=100)

stop = True
if stop == True:
    sys.exit(0)

mean_sorted_idx = np.argsort(mean_var_np)
var_sorted_idx = np.argsort(var_var_np)
length = len(mean_var_np)

# Compare bottom 10 percent
mean_btm10_val = mean_var_np[mean_sorted_idx[length * 1 / 10]]
var_btm10_val = var_var_np[var_sorted_idx[length * 1 / 10]]
# Compare top 10 percent
mean_top10_val = mean_var_np[mean_sorted_idx[length * 9 / 10 - 1]]
var_top10_val = var_var_np[var_sorted_idx[length * 9 / 10 - 1]]

btm_comm_f = open('./btm_mean_com_var_' + save_f + '.txt', 'w')
btm_mean_f = open('./btm_mean_' + save_f + '.txt', 'w')
btm_var_f = open('./btm_var_' + save_f + '.txt', 'w')

top_comm_f = open('./top_mean_com_var_' + save_f + '.txt', 'w')
top_mean_f = open('./top_mean_' + save_f + '.txt', 'w')
top_var_f = open('./top_var_' + save_f + '.txt', 'w')

j = 1
for i in mean_sorted_idx:
    if mean_var_np[i] <= mean_btm10_val and var_var_np[i] <= var_btm10_val:
        print(strain[i] + '\t' + str(j), file=btm_comm_f)
    if mean_var_np[i] <= mean_btm10_val:
        print(strain[i] + '\t' + str(j), file=btm_mean_f)
    if var_var_np[i] <= var_btm10_val:
        print(strain[i] + '\t' + str(j), file=btm_var_f)

    if mean_var_np[i] > mean_top10_val and var_var_np[i] > var_top10_val:
        print(strain[i] + '\t' + str(j), file=top_comm_f)
    if mean_var_np[i] > mean_top10_val:
        print(strain[i] + '\t' + str(j), file=top_mean_f)
    if var_var_np[i] > var_top10_val:
        print(strain[i] + '\t' + str(j), file=top_var_f)
    j = j + 1
