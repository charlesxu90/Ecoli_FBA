from __future__ import print_function
import sys
import os
import gene2React
import hashStruct
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################
# Usage: python ./cond2gkfile.py itv ./0_itv/

suffix = sys.argv[1]
infolder = sys.argv[2]
outfolder = sys.argv[3]

# Input: Condition files
# Format:
# 16C.itv
# ECK2194-NAPC    0.00    12.31   0.00    0.00    ...

# Output: Gene Knockout fluxes under conditions files
# Format:
# ECK2194-NAPC
# 16C    0.00    12.31   0.00    0.00    ...


conditions = []  # list of all conditons
condFlux = hashStruct.AutoVivification()

for filename in os.listdir(infolder):
    '''
        Save all data into a hash struct.
    '''
    if not filename.endswith('.' + suffix):
        continue

    cond = filename[:-4]
    conditions.append(cond)
    with open(infolder + filename, 'r') as cond_f:
        for line in cond_f:
            [geneId, fluxes] = line.strip().split('\t', 1)
            condFlux[cond][geneId] = fluxes

Gene_Reacts = gene2React.gene2react()


for geneId in Gene_Reacts:
    out_f = open(outfolder + geneId + '.' + suffix, 'w')

    for idx in range(0, len(conditions)):
        cond = conditions[idx]
        if (cond in condFlux) and (geneId in condFlux[cond]):
            print(cond + '\t' + condFlux[cond][geneId], file=out_f)
        else:
            print(cond, file=out_f)

    out_f.close()
