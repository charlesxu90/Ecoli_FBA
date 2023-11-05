import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd
from urllib2 import urlopen
import numpy as np
import sys

infile = sys.argv[1]
cond = sys.argv[2]

var_mut = np.loadtxt(infile, delimiter=',')
#var_mut = var_mut[1:10, 1:10]
# Plot it out
fig, ax = plt.subplots()
heatmap = ax.pcolor(var_mut, cmap=plt.cm.Accent, alpha=0.8)
cb_ax = fig.add_axes([0.95, 0.19, 0.0333, 0.71])
fig.colorbar(heatmap, cax=cb_ax)
plt.title('Flux variances distribution')

# Format
fig = plt.gcf()
fig.set_size_inches(50, 30)
#
## turn off the frame
ax.set_frame_on(False)
#
## put the major ticks at the middle of each cell
#ax.set_yticks(np.arange(len(var_mut)) + 0.5, minor=False)
print(len(var_mut))
print(len(var_mut[0]))
#ax.set_xticks(np.arange(len(var_mut[0])) + 0.5, minor=False)
#
## want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()
#
## Set the labels
#label_f = open('./labels.txt', 'r')

#labels = label_f.read().split('\n')
#
#ax.set_xticklabels(labels, minor=False)
#ax.set_yticklabels(labels, minor=False)
#
## rotate the
plt.xticks(rotation=90)
#
ax.grid(False)
#
## Turn off all the ticks
ax = plt.gca()
#
for t in ax.xaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False
    for t in ax.yaxis.get_major_ticks():
        t.tick1On = False
        t.tick2On = False

#plt.show()
plt.savefig(cond + '_var.jpg', transparent=True, bbox_inches='tight', pad_inches=0)
