from __future__ import print_function
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')

import cobra
import suitCondition
import numpy as np
#import hashStruct
import clnySize2GrowthRate
import gene2React
from copy import deepcopy
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################

# main process
#solver = 'glpk'     # change to 'gurobi' or 'cplex'
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
obj_rxn = cobra_model.reactions.Ec_biomass_iJO1366_WT_53p95M
obj_rxn.objective_coefficient = 1

print("4. read colony size file ...", file=sys.stderr)
cmin = [40.0]
colonysize = clnySize2GrowthRate.clnysize('../data/Temperature.tsv', cmin)

print("5, fba and fva analysis ...", file=sys.stderr)
Temps = ['16C', '18C', '20C', '40C', '42C', '43.5C', '45C']
# Optimize for each gene knockout
for geneId in Gene_Reacts:
    clone_model = deepcopy(cobra_model)
    for rxnId in Gene_Reacts[geneId]:
        rxn = clone_model.reactions.get_by_id(rxnId)
        if (Gene_Reacts[geneId][rxnId] == 0.0):
            rxn.upper_bound = rxn.lower_bound = 0.01
        else:
            rxn.upper_bound *= Gene_Reacts[geneId][rxnId]
            rxn.lower_bound *= Gene_Reacts[geneId][rxnId]
    try:
        clone_model.optimize()
    except ValueError:
        print("Gene " + geneId + ": error in optimizing!\n", file=sys.stdout)
        continue

    genecolsz = colonysize[geneId]
    # B * (Cmin + C) = GRmin(0)
    # B * (Cmax + C) = GRmax
    cmax = 0
    try:
        cmax = np.nanmax(genecolsz)
    except TypeError:
        print("All non colony size for gene " + geneId)
        continue
    C = -cmin[0]
    B = 0
    if clone_model.solution.f is not None:
        B = clone_model.solution.f / (cmax + C)
    else:
        print("No optimal growth for gene " + geneId + "\n", file=sys.stdout)
        continue
    growrate = [B * (np.float64(value) + C)
                if ~np.isnan(np.float64(value))
                else np.nan for value in genecolsz[1:len(genecolsz)]]

    tidx = 0
    print("Gene " + geneId + ": conducting fva:", file=sys.stdout)
    for gr in growrate:
        obj_rxn.upper_bound = obj_rxn.lower_bound = gr
        try:
            fva_ret = cobra.flux_analysis.flux_variability_analysis(
                clone_model, fraction_of_optimum=1.0,
                number_of_processes=30)
        except ValueError:
            print("\t ValueError while fva of " + Temps[tidx], file=sys.stdout)
            tidx += 1
            continue

        fva_file = open('../result/' + Temps[tidx] + '.txt', "a+")
        #print("\tOptGR: " + str(clone_model.solution.f) + "\tGolony GR: " +
        #      str(gr) + "\n", file=fva_file)
        rxns_list = clone_model.reactions
        line = [geneId]
        for rxn in rxns_list:
            line.append(format(fva_ret[rxn.id]["maximum"], '.2f'))
        fva_file.write('\t'.join(map(str, line)))
        fva_file.write("\n")
        fva_file.close()
        tidx += 1

    print("\n", file=sys.stdout)

#End of file
