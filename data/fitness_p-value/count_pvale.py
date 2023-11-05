from __future__ import print_function
import csv
import numpy as np
import sys
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################
# Usage: ./count_pvale.py 25 essential

count_f = sys.argv[1]
observe = int(sys.argv[2])
ess_disp = sys.argv[3] 

count_fd = open(count_f, 'rb')

ca_ess = [] # count array of conditional essential genes
ca_disp = [] # count array of conditional dispensable genes

count_csv = csv.reader(count_fd, delimiter='\t')

for row in count_csv:
    ca_ess.append(int(row[0]))
    ca_disp.append(int(row[1]))

count_fd.close()

print(ess_disp)
print(observe)
if ess_disp == 'essential':
    count = sum(i >= observe for i in ca_ess )
    print("p-value for conditional essential genes greater than " + str(observe) + " is: " + str(count/1000000.0))
if ess_disp == 'dispensable':
    count = sum(i >= observe for i in ca_disp )
    print("p-value for conditional dispensable genes greater than " + str(observe) + " is: " + str(count/1000000.0))

