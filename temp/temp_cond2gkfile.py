from __future__ import print_function
import csv
import sys
import gene2React
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
f_16C = open('./fva_data/16C.' + suffix, 'rb')
f_18C = open('./fva_data/18C.' + suffix, 'rb')
f_20C = open('./fva_data/20C.' + suffix, 'rb')
f_40C = open('./fva_data/40C.' + suffix, 'rb')
f_42C = open('./fva_data/42C.' + suffix, 'rb')
f_435C = open('./fva_data/43.5C.' + suffix, 'rb')
f_45C = open('./fva_data/45C.' + suffix, 'rb')

# Output: Gene Knockout fluxes under conditions files
# geneId_f = '../temperatures/' + geneId + '.txt'
Gene_Reacts = gene2React.gene2react()
match_16C = True
match_18C = True
match_20C = True
match_40C = True
match_42C = True
match_435C = True
match_45C = True

for geneId in Gene_Reacts:
    out_f = open(outfolder + geneId + '.txt', 'w')

    if match_16C == True:
        line = f_16C.readline().strip()
        row_16C = line.split('\t')
    if row_16C[0] == geneId:
        print('16C' + '\t' + '\t'.join(row_16C[1:len(row_16C)]), file=out_f)
        match_16C = True
    else:
        print('16C', file=out_f)
        match_16C = False

    if match_18C == True:
        line = f_18C.readline().strip()
        row_18C = line.split('\t')
    if row_18C[0] == geneId:
        print('18C' + '\t' + '\t'.join(row_18C[1:len(row_18C)]), file=out_f)
        match_18C = True
    else:
        print('18C', file=out_f)
        match_18C = False

    if match_20C == True:
        line = f_20C.readline().strip()
        row_20C = line.split('\t')
    if row_20C[0] == geneId:
        print('20C' + '\t' + '\t'.join(row_20C[1:len(row_20C)]), file=out_f)
        match_20C = True
    else:
        print('20C', file=out_f)
        match_20C = False

    if match_40C == True:
        line = f_40C.readline().strip()
        row_40C = line.split('\t')
    if row_40C[0] == geneId:
        print('40C' + '\t' + '\t'.join(row_40C[1:len(row_40C)]), file=out_f)
        match_40C = True
    else:
        print('40C', file=out_f)
        match_40C = False

    if match_42C == True:
        line = f_42C.readline().strip()
        row_42C = line.split('\t')
    if row_42C[0] == geneId:
        print('42C' + '\t' + '\t'.join(row_42C[1:len(row_42C)]), file=out_f)
        match_42C = True
    else:
        print('42C', file=out_f)
        match_42C = False

    if match_435C == True:
        line = f_435C.readline().strip()
        row_435C = line.split('\t')
    if row_435C[0] == geneId:
        print('43.5C' + '\t' + '\t'.join(row_435C[1:len(row_435C)]), file=out_f)
        match_435C = True
    else:
        print('43.5C', file=out_f)
        match_435C = False

    if match_45C == True:
        line = f_45C.readline().strip()
        row_45C = line.split('\t')
    if row_45C[0] == geneId:
        print('45C' + '\t' + '\t'.join(row_45C[1:len(row_45C)]), file=out_f)
        match_45C = True
    else:
        print('45C', file=out_f)
        match_45C = False


    out_f.close()
