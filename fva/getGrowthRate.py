from __future__ import print_function
import csv
import numpy as np
import hashStruct
import sys
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################
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
