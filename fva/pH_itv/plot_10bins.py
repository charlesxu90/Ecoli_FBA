##################################
# Author:   xiaopeng xu
# Email:    charlesxu90@gmail.com
# Usage:    python ./plot_10bins.py data.tsv cold
##################################
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

infile = sys.argv[1]
cond = sys.argv[2]

dat = np.loadtxt(infile, dtype=np.float, delimiter='\t')

dat = np.vstack([dat, dat[0,:]])

essential = dat[1:11, 0]
dispensable = dat[1:11, 1]
others = dat[1:11, 2] - dat[1:11, 0] - dat[1:11, 1]

fig, ax = plt.subplots()

n_groups = 10
index = np.arange(n_groups)

plt.figure(figsize=(16, 8))
bar_width = 0.4
#opacity = 0.4
freq_sum = essential + dispensable + others

rects1 = plt.bar(index, essential/freq_sum, bar_width,
        color='red')

rects2 = plt.bar(index, dispensable/freq_sum, bar_width,
        color='blue',
        bottom=essential/freq_sum)

rects3 = plt.bar(index, others/freq_sum, bar_width,
        color='pink',
        bottom=(essential+dispensable)/freq_sum)


#plt.xlabel('Group')
plt.ylabel('Fraction')
#plt.title('Gene Distribution under ' + cond + ' Condition')
plt.xticks(index + bar_width/2., ('G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10'))
plt.legend((rects1[0], rects2[0], rects3[0]), ('Essential', 'Dispensable', 'Others'))

font = {
#        'family' : 'normal',
#        'weight' : 'bold',
        'size'   : 34}

matplotlib.rc('font', **font)
#plt.tight_layout()
plt.savefig(cond + '_10bins.svg', dpi=100)
