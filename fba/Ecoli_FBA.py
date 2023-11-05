from __future__ import print_function
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')

import cobra
import suitCondition
import numpy as np
#import colonySize
import gene2React
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
# cobra_model = suitCondition.gap_filling(cobra_model)
cobra_model = suitCondition.LB_media(cobra_model)

print("3. Knockout gene to reactions ...\n", file=sys.stderr)
# Set constraints of reactions, which relates to knockout genes
Gene_Reacts = gene2React.gene2react()

[setattr(x, 'objective_coefficient', 0.) for x in cobra_model.reactions]

print("5. fba analysis ...\n", file=sys.stderr)
# Optimize for each gene Knockout
fba_err_f = open("./result/6.fba_err.txt", 'w')
fba_ret_f = open('./result/6.fba_result.txt', 'w')
print("GeneKnockout\tOptimalGrowthRate\n", file=fba_ret_f)
for geneId in Gene_Reacts:
    clone_model = deepcopy(cobra_model)
    obj_rxn = clone_model.reactions.Ec_biomass_iJO1366_WT_53p95M
    obj_rxn.objective_coefficient = 1
    for rxnId in Gene_Reacts[geneId]:
        rxn = clone_model.reactions.get_by_id(rxnId)
        if (abs(Gene_Reacts[geneId][rxnId]) <= 1e-4):
            rxn.upper_bound = 0.1 if rxn.upper_bound > 0.1 else rxn.upper_bound
            rxn.lower_bound = -0.1 if rxn.lower_bound < -0.1 else rxn.lower_bound
        else:
            rxn.upper_bound *= Gene_Reacts[geneId][rxnId]
            rxn.lower_bound *= Gene_Reacts[geneId][rxnId]
    try:
        clone_model.optimize()
    except ValueError:
        print(geneId, file=opt_err_f)
        continue

    print(geneId + '\t' + str(clone_model.solution.f), file=fba_ret_f)

fba_err_f.close()
fba_ret_f.close()

#End of file
