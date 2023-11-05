##################################
# Author: xiaopeng xu
# Email: charlesxu90@gmail.com
# Usage: python ./cluster_plt_var.py ./heat_mtt_var.dat heat 
##################################

import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram

infile = sys.argv[1]
cond = sys.argv[2]

var_rxn = np.loadtxt(infile, delimiter=',')
print(len(var_rxn))  #1248
print(len(var_rxn[0]))  #2583
#var_rxn = var_rxn[1:100, 1:2000]

#mtt_label_f = open('./labels.txt', 'r')
#mtt_labels = mtt_label_f.read().split('\n')

fig = plt.figure(figsize=(18,24))

# Compute and plot first dendrogram
# Dendrogram for mutants
ax1 = fig.add_axes([0.05,0.1,0.2,0.6])
mtt_dist = pdist(var_rxn)
mtt_link = linkage(mtt_dist, 'single')
mtt_dg = dendrogram(mtt_link, orientation='right') #, labels=mtt_labels)
ax1.set_xticks([])
ax1.set_yticks([])

# Compute and plot second dendrogram
# Dendrogram for rxns
ax2 = fig.add_axes([0.3,0.71,0.6,0.2])
rxn_dist = pdist(var_rxn.transpose())
rxn_link = linkage(rxn_dist, 'single')
rxn_dg= dendrogram(rxn_link)
ax2.set_xticks([])
ax2.set_yticks([])

# Compute and plot the heatmap
axmatrix = fig.add_axes([0.3, 0.1, 0.6, 0.6])
idx1 = mtt_dg['leaves']
idx2 = rxn_dg['leaves']

rxn_var = var_rxn[idx1, :]
rxn_var = rxn_var[:, idx2]

#heatmap = ax.pcolor(var_rxn, cmap=plt.cm.Accent, alpha=0.8)
im = axmatrix.matshow(rxn_var, aspect='auto', origin='lower', cmap=plt.cm.YlGnBu)
axmatrix.set_xticks([])
axmatrix.set_yticks([])

axcolor = fig.add_axes([0.91, 0.1, 0.02, 0.6])
plt.colorbar(im, cax=axcolor)
plt.title('Flux variances distribution')

plt.savefig(cond + '_var.svg', transparent=True)#, bbox_inches='tight', pad_inches=0)
