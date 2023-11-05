from __future__ import print_function
import csv
import numpy as np
import hashStruct
import sys
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################
# Input:
csize_file = '../data/ColonyData.txt'
optgr_file = '../fba/result/6.fba_result.txt'
# Colony Size file format
# || GeneKnockout  Condition1  Condition2
# || ECK2194-NAPC  0.2         0.1

# Optimal Growth Rate file format
# || GeneKnockout  OptimalGrowthRate
# || ECK2194-NAPC    8.5712968149

# Output:
gr_file = './result/growthRate.txt'
# || Conditions    ECK2194-NAPC    ECK3762-ILVE ...
# || SDS0.5%/EDTA0.1   8.51        8.34
# || SDS0.5%/EDTA0.5   4.32        4.53
#=============================================#

optGR = hashStruct.AutoVivification()
with open(optgr_file, 'rb') as optgr_f:
    optgr_f.next();
    tsvin = csv.reader(optgr_f, delimiter='\t')
    for row in tsvin:
        optGR[row[0]] = np.float64(row[1])
optgr_f.close()

# print("\t".join([k for k in optGR])) # OK
conditions = []
strainCSize = hashStruct.AutoVivification()
with open(csize_file, 'rb') as csize_f:
    tsvin = csv.reader(csize_f, delimiter='\t')
    for row in tsvin:
        if row[0] == 'Gene':
            conditions = row[1:len(row)]
            continue
        strainCSize[row[0]] = row[1:len(row)]
csize_f.close()
# print("\t".join(conditions)) # OK

NO_OF_GENES = len(optGR)    # No of genes in model and data
NO_OF_CONDITIONS = len(conditions)  # No of conditions in data

# Store into a 2d array, for easy access using index
# Reduce all genes to only genes included in Model
csizeC2G = np.full((NO_OF_GENES, NO_OF_CONDITIONS), 0)
optGrA = np.full((NO_OF_GENES, 1), 0)

i = 0
for gene in optGR:
    j = 0
    optGrA[i] = optGR[gene]
    for cond in conditions:
        csizeC2G[i][j] = np.nan if len(strainCSize[gene][j]) < 1 else np.float64(strainCSize[gene][j])
        j += 1
    i += 1

# calculate GR and print out
##Match maximum colony size match with WT opt Growth Rate,
# Minimum colony size match with Growth Rate 0
# B * (Xmin + C) = GRmin (0)
# B * (Xmax + C) = GRmax (In a given condition)
# GR = B * (X + C) = GRmax / (Xmax - Xmin) * ( X - Xmin)
# GrowthRate = Min(GR, OptGR(gene))
cmax = np.nanmax(csizeC2G, axis=0)
cargmax = np.nanargmax(csizeC2G, axis=0)
cmin = np.nanmin(csizeC2G, axis=0)

gr_f = open(gr_file, 'w')
print('Conditions' + '\t' + '\t'.join([k for k in optGR]), file=gr_f)

#print("\t".join(map(str, optGrA[:, 0])))  # OK
#print("\t".join([str(v) for v in cargmax]))
#print("\t".join([str(v) for v in cmax]))
#print("\t".join([str(v) for v in cmin]))
for j in range(0, NO_OF_CONDITIONS):
    cminFc = np.full((1, NO_OF_GENES), cmin[j])
    grs = optGrA[cargmax[j]] / (cmax[j] - cmin[j]) * (csizeC2G[:, j] - cminFc)
    gr = np.minimum(grs, optGrA.transpose())
    # print("\t".join(map(str, grs[0, :]))) # OK
    print(conditions[j]  + "\t" + "\t".join(map(str, gr[0, :])), file=gr_f)
    j += 1
gr_f.close()


def clnysize(csize_file, cmin):
    """ Read colony size data into hash matrix"""
    clony_size = hashStruct.AutoVivification()
    with open(csize_file, 'rb') as tsvfin:
        tsvfin.next()
        tsvin = csv.reader(tsvfin, delimiter='\t')
        for row in tsvin:
            if len(row) < 1:
                break
            for i in range(1, len(row)):
                if len(row[i]) < 1:
                    row[i] = np.nan
            row_d = [np.float64(value) for value in row[1:len(row)]]
            dmin = 100.0
            try:
                dmin = np.nanmin(row_d)
            except TypeError:
                dmin = 100.0
            cmin[0] = np.fmin(cmin[0], dmin)
            clony_size[row[0]] = row_d
    return clony_size


def getGrowthRate():
    """ Read growth rate from file. """
    GrowthRate = hashStruct.AutoVivification()
    with open('./result/growthRate.txt', 'rb') as gr_f:
        tsvin = csv.reader(gr_f, delimiter='\t')
        for row in tsvin:
            if row[0] == 'Conditions':
                genes = row[1:len(row)]
                continue
            for i in range(1,len(row)):
                GrowthRate[row[0]][genes[i - 1]] = np.float64(row[i])
    return GrowthRate
