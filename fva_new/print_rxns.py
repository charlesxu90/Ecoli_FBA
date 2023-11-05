from __future__ import print_function
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')

import cobra
import suitCondition
import numpy as np
import gene2React
import getGrowthRate
import sys
from copy import deepcopy
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################

# main process
print("1. read sbml model ...\n", file=sys.stderr)
sbml_file = '../data/msb201165-s3.xml'
cobra_model = cobra.io.read_sbml_model(sbml_file, old_sbml='true')

print("2. Modify module to suit BW25113 and culture ...\n", file=sys.stderr)
cobra_model = suitCondition.suit_bw25113(cobra_model)
#cobra_model = suitCondition.gap_filling(cobra_model)
cobra_model = suitCondition.LB_media(cobra_model)

rxns_list = cobra_model.reactions
rxn_f = open('rxns_in_order.tsv', 'w')
rxn_ids = []

for rxn in rxns_list:
    rxn_ids.append(rxn.id)

print("\t".join(rxn_ids), file=rxn_f)
rxn_f.close()

#End of file
