from __future__ import print_function
import csv
import sys
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################
# Usage: python ./cond2gkfile.py itv ./0_itv/

suffix = sys.argv[1]
outfolder = sys.argv[2]
# Input: Condition files
# Format:
# ECK2194-NAPC    0.00    12.31   0.00    0.00    ...
#f_C1 = open('./data/PH4.' + suffix, 'rb')
#f_C2 = open('./data/PH4.5.' + suffix, 'rb')
#f_C3 = open('./data/PH5.' + suffix, 'rb')
#f_C4 = open('./data/PH6.' + suffix, 'rb')
f_C5 = open('./data/PH8.' + suffix, 'rb')
f_C6 = open('./data/PH9.' + suffix, 'rb')
f_C7 = open('./data/PH9.5.' + suffix, 'rb')
f_C8 = open('./data/PH10.' + suffix, 'rb')

# Output: Gene Knockout fluxes under conditions files
# geneId_f = '../temperatures/' + geneId + '.txt'
#gk_C1 = {} 
#gk_C2 = {} 
#gk_C3 = {} 
#gk_C4 = {} 
gk_C5 = {} 
gk_C6 = {} 
gk_C7 = {} 
gk_C8 = {}

#for line in f_C1:
#    row_C1 = line.rstrip().split('\t')
#    gk_C1[row_C1[0]] = 'PH4' + '\t' + '\t'.join(row_C1[1:len(row_C1)]) 
#f_C1.close()
#
#for line in f_C2:
#    row_C2 = line.rstrip().split('\t')
#    gk_C2[row_C2[0]] = 'PH4.5' + '\t' + '\t'.join(row_C2[1:len(row_C2)]) 
#f_C2.close()
#
#for line in f_C3:
#    row_C3 = line.rstrip().split('\t')
#    gk_C3[row_C3[0]] = 'PH5' + '\t' + '\t'.join(row_C3[1:len(row_C3)]) 
#f_C3.close()
#
#for line in f_C4:
#    row_C4 = line.rstrip().split('\t')
#    gk_C4[row_C4[0]] = 'PH6' + '\t' + '\t'.join(row_C4[1:len(row_C4)]) 
#f_C4.close()

for line in f_C5:
    row_C5 = line.rstrip().split('\t')
    gk_C5[row_C5[0]] = 'PH8' + '\t' + '\t'.join(row_C5[1:len(row_C5)]) 
f_C5.close()

for line in f_C6:
    row_C6 = line.rstrip().split('\t')
    gk_C6[row_C6[0]] = 'PH9' + '\t' + '\t'.join(row_C6[1:len(row_C6)]) 
f_C6.close()

for line in f_C7:
    row_C7 = line.rstrip().split('\t')
    gk_C7[row_C7[0]] = 'PH9.5' + '\t' + '\t'.join(row_C7[1:len(row_C7)]) 
f_C7.close()

for line in f_C8:
    row_C8 = line.rstrip().split('\t')
    gk_C8[row_C8[0]] = 'PH10' + '\t' + '\t'.join(row_C8[1:len(row_C8)]) 
f_C8.close()


geneIds = []
#geneIds.extend([k for k in gk_C1])
#geneIds.extend([k for k in gk_C2])
#geneIds.extend([k for k in gk_C3])
#geneIds.extend([k for k in gk_C4])
geneIds.extend([k for k in gk_C5])
geneIds.extend([k for k in gk_C6])
geneIds.extend([k for k in gk_C7])
geneIds.extend([k for k in gk_C8])

geneIds = list(set(geneIds))

for geneId in geneIds:

    out_f = open(outfolder + geneId + '.txt', 'w')

    #if geneId in gk_C1:
    #    print(gk_C1[geneId], file=out_f)
    #else:
    #    print('PH4', file=out_f)

    #if geneId in gk_C2:
    #    print(gk_C2[geneId], file=out_f)
    #else:
    #    print('PH4.5', file=out_f)

    #if geneId in gk_C3:
    #    print(gk_C3[geneId], file=out_f)
    #else:
    #    print('PH5', file=out_f)

    #if geneId in gk_C4:
    #    print(gk_C4[geneId], file=out_f)
    #else:
    #    print('PH6', file=out_f)

    if geneId in gk_C5:
        print(gk_C5[geneId], file=out_f)
    else:
        print('PH8', file=out_f)

    if geneId in gk_C6:
        print(gk_C6[geneId], file=out_f)
    else:
        print('PH9', file=out_f)

    if geneId in gk_C7:
        print(gk_C7[geneId], file=out_f)
    else:
        print('PH9.5', file=out_f)

    if geneId in gk_C8:
        print(gk_C8[geneId], file=out_f)
    else:
        print('PH10', file=out_f)

    out_f.close()
