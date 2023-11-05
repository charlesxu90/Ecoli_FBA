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
#f_C1 = open('./data/16C.' + suffix, 'rb')
#f_C2 = open('./data/18C.' + suffix, 'rb')
#f_C3 = open('./data/20C.' + suffix, 'rb')
f_C4 = open('./data/40C.' + suffix, 'rb')
f_C5 = open('./data/42C.' + suffix, 'rb')
f_C6 = open('./data/43.5C.' + suffix, 'rb')
f_C7 = open('./data/45C.' + suffix, 'rb')

# Output: Gene Knockout fluxes under conditions files
# geneId_f = '../temperatures/' + geneId + '.txt'
#gk_C1 = {} 
#gk_C2 = {} 
#gk_C3 = {} 
gk_C4 = {} 
gk_C5 = {} 
gk_C6 = {} 
gk_C7 = {} 

#for line in f_C1:
#    row_C1 = line.rstrip().split('\t')
#    gk_C1[row_C1[0]] = '16C' + '\t' + '\t'.join(row_C1[1:len(row_C1)]) 
#f_C1.close()
#
#for line in f_C2:
#    row_C2 = line.rstrip().split('\t')
#    gk_C2[row_C2[0]] = '18C' + '\t' + '\t'.join(row_C2[1:len(row_C2)]) 
#f_C2.close()
#
#for line in f_C3:
#    row_C3 = line.rstrip().split('\t')
#    gk_C3[row_C3[0]] = '20C' + '\t' + '\t'.join(row_C3[1:len(row_C3)]) 
#f_C3.close()

for line in f_C4:
    row_C4 = line.rstrip().split('\t')
    gk_C4[row_C4[0]] = '40C' + '\t' + '\t'.join(row_C4[1:len(row_C4)]) 
f_C4.close()

for line in f_C5:
    row_C5 = line.rstrip().split('\t')
    gk_C5[row_C5[0]] = '42C' + '\t' + '\t'.join(row_C5[1:len(row_C5)]) 
f_C5.close()

for line in f_C6:
    row_C6 = line.rstrip().split('\t')
    gk_C6[row_C6[0]] = '43.5C' + '\t' + '\t'.join(row_C6[1:len(row_C6)]) 
f_C6.close()

for line in f_C7:
    row_C7 = line.rstrip().split('\t')
    gk_C7[row_C7[0]] = '45C' + '\t' + '\t'.join(row_C7[1:len(row_C7)]) 
f_C7.close()

geneIds = []
#geneIds.extend([k for k in gk_C1])
#geneIds.extend([k for k in gk_C2])
#geneIds.extend([k for k in gk_C3])
geneIds.extend([k for k in gk_C4])
geneIds.extend([k for k in gk_C5])
geneIds.extend([k for k in gk_C6])
geneIds.extend([k for k in gk_C7])

geneIds = list(set(geneIds))

for geneId in geneIds:

    out_f = open(outfolder + geneId + '.txt', 'w')

    #if geneId in gk_C1:
    #    print(gk_C1[geneId], file=out_f)
    #else:
    #    print('16C', file=out_f)

    #if geneId in gk_C2:
    #    print(gk_C2[geneId], file=out_f)
    #else:
    #    print('18C', file=out_f)

    #if geneId in gk_C3:
    #    print(gk_C3[geneId], file=out_f)
    #else:
    #    print('20C', file=out_f)

    if geneId in gk_C4:
        print(gk_C4[geneId], file=out_f)
    else:
        print('40C', file=out_f)

    if geneId in gk_C5:
        print(gk_C5[geneId], file=out_f)
    else:
        print('42C', file=out_f)

    if geneId in gk_C6:
        print(gk_C6[geneId], file=out_f)
    else:
        print('43.5C', file=out_f)

    if geneId in gk_C7:
        print(gk_C7[geneId], file=out_f)
    else:
        print('45C', file=out_f)

    out_f.close()
