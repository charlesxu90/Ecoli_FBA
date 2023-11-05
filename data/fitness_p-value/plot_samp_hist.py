from __future__ import print_function
import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################

count_f = sys.argv[1]
count_fd = open(count_f, 'rb')

ca_ess = [] # count array of conditional essential genes
ca_disp = [] # count array of conditional dispensable genes

count_csv = csv.reader(count_fd, delimiter='\t')

for row in count_csv:
    ca_ess.append(int(row[0]))
    ca_disp.append(int(row[1]))

count_fd.close()

plt.figure(figsize=(16,8))
max_val = max(ca_ess)
plt.hist(ca_ess, bins=max_val)
plt.xlabel('No. of conditional essential genes')
plt.ylabel('Frequency')
plt.savefig('./bin_cond_ess_genes.svg', dpi=100)

max_val = max(ca_disp)
plt.clf()
plt.hist(ca_disp, bins=max_val)
plt.xlabel('No. of conditional dispensable genes')
plt.ylabel('Frequency')
plt.savefig('./bin_cond_disp_genes.svg', dpi=100)
