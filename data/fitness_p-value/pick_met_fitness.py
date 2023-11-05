from __future__ import print_function
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')

import numpy as np
import sys
import re
import hashStruct
import csv
import time
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################

start = time.time()
time.clock()

############# 1. Genes in data and model ################
gene_fd = open('./ECK_in_data_model.tsv', 'rb')

gene_ECK = [] # Genes in data and model, ECK id
for gene in gene_fd:
    gene_ECK.append(gene.rstrip())

#print('\t'.join(gene_ECK) + '\t' + str(len(gene_ECK)))
gene_fd.close()
tcounter = time.time() - start 
print("Reading genes finished. Require time " + str(tcounter))


############# 2. Get fitness data of met genes ################
# Complete fitness data
fit_dat_fd = open('./ColonyData.txt', 'rb')

fit_dat = hashStruct.AutoVivification() # Fit data of metabolic gene mutants

fit_dat_fd.next()
fit_dat_csv = csv.reader(fit_dat_fd, delimiter='\t')

for row in fit_dat_csv:

    ptnmr1 = re.search(r"^(ECK\d{4})", row[0], re.IGNORECASE)
    gene = ptnmr1.group(1)
    if gene in gene_ECK:
        fit_dat[row[0]] = row[1:325]
    
fit_dat_fd.close()

tcounter = time.time() - start - tcounter
print("Get metabolic gene fitness finished. require time " + str(tcounter))


############# 3. Print out metabolic gene fitness  ################
met_fit_dat = open('./met_fit_dat.txt', 'w')
for gene in fit_dat.keys():
    print(gene + '\t' + '\t'.join(fit_dat[gene]), file=met_fit_dat)

met_fit_dat.close()
