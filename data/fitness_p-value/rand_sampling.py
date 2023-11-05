from __future__ import print_function
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')

import numpy as np
import sys
import re
import random
import hashStruct
import csv
import time

##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################

nsample = int(sys.argv[1])
niter = int(sys.argv[2])
out_f = sys.argv[3]

start = time.time()
time.clock()

met_fit_fd = open('./met_fit_dat.txt', 'rb')
met_fit_csv = csv.reader(met_fit_fd, delimiter='\t')

met_fit = hashStruct.AutoVivification()

ncond = -1
for row in met_fit_csv:
    if ( ncond == -1 ):
        ncond = len(row) - 1
    met_fit[row[0]] = row[1:]

print("Reading file finished. Time " + str(time.time() - start))

out_fd = open(out_f, 'w')
it = 0
while(it < niter ):
    it = it + 1
    c_ess = 0
    c_disp = 0

    #print('nsample ' + str(nsample) + '\t' + 'ncond ' + str(ncond))
    sample_idx = random.sample(xrange(ncond), nsample)
    sample_idx.sort()
    #print(sample_idx)

    for key in met_fit:
        check_ess = True
        check_disp = True

        i = 0
        while (i < nsample):
            if (met_fit[key][sample_idx[i]] is '' or float(met_fit[key][sample_idx[i]]) > -1.0):
                check_ess = False
            if (met_fit[key][sample_idx[i]] is '' or float(met_fit[key][sample_idx[i]]) < 1.0):
                check_disp = False
            i = i + 1

        if check_ess is True:
            c_ess = c_ess + 1
        if check_disp is True:
            c_disp = c_disp + 1

        #print("key " + key)
    #print("Iteration: " + str(it) + ", essential " + str(c_ess) + ",  dispensable " + str(c_disp))
    print(str(c_ess) + '\t' + str(c_disp), file=out_fd)

print("Sampling finished. Time " + str(time.time() - start))

out_fd.close()
