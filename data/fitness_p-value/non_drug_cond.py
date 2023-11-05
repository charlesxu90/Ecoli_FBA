from __future__ import print_function
import sys
import re
sys.path.append('/usr/lib/python2.7/dist-packages')
import numpy as np
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################

drug_fd = open('./drug.tsv', 'rb')
cond_fd = open('./Conditions.txt', 'rb')
non_drug_cond_fd = open('./non_drug_cond.txt', 'w')

drugs = []

for drug in drug_fd:
    drugs.append(drug.rstrip())
#print('\t'.join(drugs))
drug_fd.close()

for cond in cond_fd:
    cond = cond.rstrip()
    matched = False
    for drug in drugs:
        ptnmr1 = re.search(re.escape(drug), cond, re.IGNORECASE)
        if ptnmr1 is None:
            continue
        else:
            matched = True
    if matched is False:
        print(cond, file=non_drug_cond_fd)

cond_fd.close()
non_drug_cond_fd.close()
print("Finished running!")
