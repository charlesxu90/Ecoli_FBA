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

infile = sys.argv[1]

cov_rxn = np.loadtxt(infile, delimiter='\t', usecols=range(0, 1405))
#cov_rxn = cov_rxn[range(1, 2584),:]
#print(labels)
print(len(cov_rxn))  #7
print(len(cov_rxn[0]))  #2583
#cov_rxn = cov_rxn[1:100, 1:2000]

########################################################

fig = plt.figure(figsize=(18,16))

## Compute and plot the heatmap
axmatrix = fig.add_axes([0.10, 0.1, 0.70, 0.8])
im = axmatrix.matshow(cov_rxn.transpose(), aspect='auto', origin='lower', vmax=0, vmin=-10, cmap=plt.cm.Blues_r)
axmatrix.set_xticks([])
axmatrix.set_yticks([])

axcolor = fig.add_axes([0.82, 0.1, 0.05, 0.8])
cb = plt.colorbar(im, cax=axcolor)
cb.ax.tick_params(labelsize=22)
#plt.title('Flux distribution')

plt.savefig('cov_flux.svg', transparent=True)#, bbox_inches='tight', pad_inches=0)
