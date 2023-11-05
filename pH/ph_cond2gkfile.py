from __future__ import print_function
import csv
import sys
import gene2React
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
# Usage: python ./cond2gkfile.py max ./data/
##################################


suffix = sys.argv[1]
outfolder = sys.argv[2]

# Input: Condition files
# Format:
# ECK2194-NAPC    0.00    12.31   0.00    0.00    ...
f_PH4 = open('./fva_data/PH4.' + suffix, 'rb')
f_PH45 = open('./fva_data/PH4.5.' + suffix, 'rb')
f_PH5 = open('./fva_data/PH5.' + suffix, 'rb')
f_PH6 = open('./fva_data/PH6.' + suffix, 'rb')
f_PH8 = open('./fva_data/PH8.' + suffix, 'rb')
f_PH9 = open('./fva_data/PH9.' + suffix, 'rb')
f_PH95 = open('./fva_data/PH9.5.' + suffix, 'rb')
f_PH10 = open('./fva_data/PH10.' + suffix, 'rb')

# Output: Gene Knockout fluxes under conditions files
# geneId_f = '../temperatures/' + geneId + '.txt'
Gene_Reacts = gene2React.gene2react()
match_PH4 = True
match_PH45 = True
match_PH5 = True
match_PH6 = True
match_PH8 = True
match_PH9 = True
match_PH95 = True
match_PH10 = True

for geneId in Gene_Reacts:
    out_f = open(outfolder + geneId + '.txt', 'w')

    if match_PH4 == True:
        line = f_PH4.readline().strip()
        row_PH4 = line.split('\t')
    if row_PH4[0] == geneId:
        print('PH4' + '\t' + '\t'.join(row_PH4[1:len(row_PH4)]), file=out_f)
        match_PH4 = True
    else:
        print('PH4', file=out_f)
        match_PH4 = False

    if match_PH45 == True:
        line = f_PH45.readline().strip()
        row_PH45 = line.split('\t')
    if row_PH45[0] == geneId:
        print('PH45' + '\t' + '\t'.join(row_PH45[1:len(row_PH45)]), file=out_f)
        match_PH45 = True
    else:
        print('PH45', file=out_f)
        match_PH45 = False

    if match_PH5 == True:
        line = f_PH5.readline().strip()
        row_PH5 = line.split('\t')
    if row_PH5[0] == geneId:
        print('PH5' + '\t' + '\t'.join(row_PH5[1:len(row_PH5)]), file=out_f)
        match_PH5 = True
    else:
        print('PH5', file=out_f)
        match_PH5 = False

    if match_PH6 == True:
        line = f_PH6.readline().strip()
        row_PH6 = line.split('\t')
    if row_PH6[0] == geneId:
        print('PH6' + '\t' + '\t'.join(row_PH6[1:len(row_PH6)]), file=out_f)
        match_PH6 = True
    else:
        print('PH6', file=out_f)
        match_PH6 = False

    if match_PH8 == True:
        line = f_PH8.readline().strip()
        row_PH8 = line.split('\t')
    if row_PH8[0] == geneId:
        print('PH8' + '\t' + '\t'.join(row_PH8[1:len(row_PH8)]), file=out_f)
        match_PH8 = True
    else:
        print('PH8', file=out_f)
        match_PH8 = False

    if match_PH9 == True:
        line = f_PH9.readline().strip()
        row_PH9 = line.split('\t')
    if row_PH9[0] == geneId:
        print('PH9' + '\t' + '\t'.join(row_PH9[1:len(row_PH9)]), file=out_f)
        match_PH9 = True
    else:
        print('PH9', file=out_f)
        match_PH9 = False

    if match_PH95 == True:
        line = f_PH95.readline().strip()
        row_PH95 = line.split('\t')
    if row_PH95[0] == geneId:
        print('PH95' + '\t' + '\t'.join(row_PH95[1:len(row_PH95)]), file=out_f)
        match_PH95 = True
    else:
        print('PH95', file=out_f)
        match_PH95 = False

    if match_PH10 == True:
        line = f_PH10.readline().strip()
        row_PH10 = line.split('\t')
    if row_PH10[0] == geneId:
        print('PH10' + '\t' + '\t'.join(row_PH10[1:len(row_PH10)]), file=out_f)
        match_PH10 = True
    else:
        print('PH10', file=out_f)
        match_PH10 = False

    out_f.close()
