##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
# Usage: python ./cluster_plt_var.py ./heat_mtt_var.dat heat 
##################################

import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

infile = sys.argv[1]
cond = sys.argv[2]

var_rxn = np.loadtxt(infile, delimiter='\t', usecols=range(1,2584))
#labels = var_rxn[0,:]
#var_rxn = var_rxn[range(1, 2584),:]
#print(labels)
print(len(var_rxn))  #7
print(len(var_rxn[0]))  #2583
#var_rxn = var_rxn[1:100, 1:2000]
########################################################
# Remove reactions which have zero fluxes in all conditions
#zero_check = np.zeros(len(var_rxn))
#idx = []
#for i in range(0, len(var_rxn[0])):
#    if not np.array_equal(var_rxn[:, i], zero_check):
#        idx.append(i)
#print(len(idx))
#var_rxn = var_rxn[:, idx]
########################################################
var_rxn.clip(-1000, 1000)

########################################################

fig = plt.figure(figsize=(8,24))

## Compute and plot the heatmap
axmatrix = fig.add_axes([0.10, 0.1, 0.5, 0.8])
im = axmatrix.matshow(var_rxn.transpose(), aspect='auto', origin='lower', vmax=1000, vmin=-1000, cmap=plt.cm.bwr)
axmatrix.set_xticks([])
axmatrix.set_yticks([])

axcolor = fig.add_axes([0.72, 0.1, 0.05, 0.8])
cb = plt.colorbar(im, cax=axcolor)
cb.ax.tick_params(labelsize=22)
#plt.title('Flux distribution')


plt.savefig(cond + '_flux.svg', transparent=True)#, bbox_inches='tight', pad_inches=0)
