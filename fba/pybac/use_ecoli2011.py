from __future__ import print_function
import sys
sys.path.append('/usr/lib/python2.7/dist-packages')

import cobra
import suit_condition
#import numpy as np
import hash_struct
import colSz2GRate
import gene2React
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################

####1. read sbml model
sbml_file = './data/msb201165-s3.xml'
#sbml_file = 'ecoli_core_model.xml'
cobra_model = cobra.io.read_sbml_model(sbml_file, old_sbml='true')

####2. Modify module to suit BW25113
cobra_model = suit_condition.suit_bw25113(cobra_model)
cobra_model = suit_condition.gap_filling(cobra_model)   # Not Complete Yet

####3. Set constraints for LB media/culture
cobra_model = suit_condition.LB_media(cobra_model)

####4. Gene knockout
# Set constraints of reactions, which relates to knockout genes
gene2gid = hash_struct.AutoVivification()
Gene_Reacts = hash_struct.AutoVivification()    # Create a Hash data struct
gene2gid = gene2React.gene2geneID()
Gene_Reacts = gene2React.geneID2react(gene2gid)

####5. Infer Growth Rate from Colony Size data

Growth_Rates = colSz2GRate.csize2grate('./data/Temperature.tsv')

####6. Set the objective function
#Optimal Growth Rate for WT: 8.5712968149
[setattr(x, 'objective_coefficient', 0.) for x in cobra_model.reactions]
obj_rxn = cobra_model.reactions.Ec_biomass_iJO1366_WT_53p95M
TempRT = ['16C', '18C', '20C', '40C', '42C', '43.5C', '45C']

####7. Flux variance analysis of all knockout genes
counter = 1
for geneId in Gene_Reacts:
    if counter <= 1:
        counter = counter + 1
    else:
        break

    for rxnId in Gene_Reacts[geneId]:
        rxn = cobra_model.reactions.get_by_id(rxnId)
        rxn.upper_bound = Gene_Reacts[geneId][rxnId] * rxn.upper_bound
        if (rxn.lower_bound < 0):
            rxn.lower_bound = Gene_Reacts[geneId][rxnId] * rxn.lower_bound

    try:
        Growth_Rates[geneId]
    except NameError:
        continue
    else:
        index = 0
        #print(type(Growth_Rates[geneId][1]), file=sys.stdout)
        #print(Growth_Rates[geneId], file=sys.stdout)
        for growthRate in Growth_Rates[geneId]:
            obj_rxn.upper_bound = obj_rxn.lower_bound = growthRate
            try:
                FVA_rst = cobra.flux_analysis.flux_variability_analysis(
                    cobra_model, fraction_of_optimum=1.0,
                    number_of_processes=30)
            except ValueError:
                print ("Error while flux_variability_analysis of " + geneId
                       + TempRT[index] + "\n", file=sys.stdout)
                index = index + 1
                continue
            else:
                fva_file = open('./result/' + geneId +
                                TempRT[index] + '.txt', "w+")
                print('Reaction', 'Max flux', 'Min flux',
                      'Reactants', 'Products', file=fva_file, sep='\t')
                #print(cobra_model.solution.f)#, file=fva_file)
                rxns_list = cobra_model.reactions
                for rxn in rxns_list:

                    reactants = ''
                    if(len(rxn.reactants) == 0):
                        reactants = '-'
                    else:
                        for i in range(1, len(rxn.reactants)):
                            reactants += str(rxn.reactants[i - 1])

                    products = ''
                    if(len(rxn.products) == 0):
                        products = '-'
                    else:
                        for i in range(1, len(rxn.products)):
                            products += str(rxn.products[i - 1])

                    print (rxn.id, format(FVA_rst[rxn.id]["maximum"], '.2f'),
                           format(FVA_rst[rxn.id]["minimum"], '.2f'),
                           reactants, products,
                           file=fva_file, sep='\t')
                fva_file.close()
                index = index + 1
#End of file
