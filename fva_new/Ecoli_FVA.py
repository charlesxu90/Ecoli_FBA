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

Condition = sys.argv[1]

# main process
print("1. read sbml model ...\n", file=sys.stderr)
sbml_file = '../data/msb201165-s3.xml'
cobra_model = cobra.io.read_sbml_model(sbml_file, old_sbml='true')

print("2. Modify module to suit BW25113 and culture ...\n", file=sys.stderr)
cobra_model = suitCondition.suit_bw25113(cobra_model)
#cobra_model = suitCondition.gap_filling(cobra_model)
cobra_model = suitCondition.LB_media(cobra_model)

print("3. Knockout gene to reactions ...\n", file=sys.stderr)
# Set constraints of reactions, which relates to knockout genes
Gene_Reacts = gene2React.gene2react()

[setattr(x, 'objective_coefficient', 0.) for x in cobra_model.reactions]

print("4. read growth rate file ...", file=sys.stderr)
GrowthRate = getGrowthRate.getGrowthRate()

print("5. fba and fva analysis ...", file=sys.stderr)
#Condition = '16C'
fva_max_f = open('./result/' + Condition + '.max', "w")
#fva_min_f = open('./result/' + Condition + '.min', "w")
#fva_itv_f = open('./result/' + Condition + '.itv', "w")

fva_err_f = open('./result/' + Condition + '.err', 'w')

for geneId in GrowthRate[Condition]:
    clone_model = deepcopy(cobra_model)
    obj_rxn = clone_model.reactions.Ec_biomass_iJO1366_WT_53p95M
    obj_rxn.objective_coefficient = 1
    for rxnId in Gene_Reacts[geneId]:
        rxn = clone_model.reactions.get_by_id(rxnId)
        if (abs(Gene_Reacts[geneId][rxnId]) < 1e-3):
            rxn.upper_bound = 0.1 if rxn.upper_bound > 0.1 else rxn.upper_bound
            rxn.lower_bound = -0.1 if rxn.lower_bound < -0.1 else rxn.lower_bound
        else:
            rxn.upper_bound *= Gene_Reacts[geneId][rxnId]
            rxn.lower_bound *= Gene_Reacts[geneId][rxnId]

    gr = GrowthRate[Condition][geneId]
    obj_rxn.upper_bound = obj_rxn.lower_bound = gr
    print(Condition + "\t" + geneId + "\t" + str(gr))
    try:
        fva_ret = cobra.flux_analysis.flux_variability_analysis(
            clone_model, fraction_of_optimum=1.0)
    except ValueError:
        print(geneId, file=fva_err_f)
        continue

    rxns_list = clone_model.reactions
    lmax = [geneId]
    #lmin = [geneId]
    #litv = [geneId]
    for rxn in rxns_list:
        lmax.append(format(fva_ret[rxn.id]["maximum"], '.2f'))
        #lmin.append(format(fva_ret[rxn.id]["minimum"], '.2f'))
        #litv.append(format(fva_ret[rxn.id]["maximum"] - fva_ret[rxn.id]["minimum"], '.2f'))
    print("\t".join(lmax), file=fva_max_f)
    #print("\t".join(lmin), file=fva_min_f)
    #print("\t".join(litv), file=fva_itv_f)
fva_max_f.close()
#fva_min_f.close()
#fva_itv_f.close()
fva_err_f.close()

#End of file
