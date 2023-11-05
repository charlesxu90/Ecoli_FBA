from __future__ import print_function
import cobra
#import numpy as np
import sys
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################
solver = 'glpk'     # change to 'gurobi' or 'cplex'
####1. read sbml model
sbml_file = './msb201165-s3.xml'
#sbml_file = 'ecoli_core_model.xml'
cobra_model = cobra.io.read_sbml_model(sbml_file, old_sbml='true')

#Best practice to zero all objective coefficients
[setattr(x, 'objective_coefficient', 0.) for x in cobra_model.reactions]

####2. Modify module to suit BW25113
arai = cobra_model.reactions.ARAI
arai.lower_bound = arai.upper_bound = 0
rbk_l1 = cobra_model.reactions.RBK_L1
rbk_l1.lower_bound = rbk_l1.upper_bound = 0
rmpa = cobra_model.reactions.RMPA
rmpa.lower_bound = rmpa.upper_bound = 0
lyxi = cobra_model.reactions.LYXI
lyxi.lower_bound = lyxi.upper_bound = 0
rmi = cobra_model.reactions.RMI
rmi.lower_bound = rmi.upper_bound = 0
rmk = cobra_model.reactions.RMK
rmk.lower_bound = rmk.upper_bound = 0
lacz = cobra_model.reactions.LACZ
lacz.lower_bound = lacz.upper_bound = 0

## Add gap reactions
#
#

####3. Set constraints for LB media/culture
glc = cobra_model.reactions.EX_glc_LPAREN_e_RPAREN_
glc.lower_bound = 0

ins = cobra_model.reactions.EX_ins_LPAREN_e_RPAREN_
ins.lower_bound = -0.1
hxan = cobra_model.reactions.EX_hxan_LPAREN_e_RPAREN_
hxan.lower_bound = -0.1
h2o = cobra_model.reactions.EX_h2o_LPAREN_e_RPAREN_
h2o.lower_bound = -1000
o2 = cobra_model.reactions.EX_o2_LPAREN_e_RPAREN_
o2.lower_bound = -1000
co2 = cobra_model.reactions.EX_co2_LPAREN_e_RPAREN_
co2.lower_bound = -1000
nh4 = cobra_model.reactions.EX_nh4_LPAREN_e_RPAREN_
nh4.lower_bound = -1000
so4 = cobra_model.reactions.EX_so4_LPAREN_e_RPAREN_
so4.lower_bound = -1000
ca2 = cobra_model.reactions.EX_ca2_LPAREN_e_RPAREN_
ca2.lower_bound = -1000
h = cobra_model.reactions.EX_h_LPAREN_e_RPAREN_
h.lower_bound = -1000
k = cobra_model.reactions.EX_k_LPAREN_e_RPAREN_
k.lower_bound = -1000
mg2 = cobra_model.reactions.EX_mg2_LPAREN_e_RPAREN_
mg2.lower_bound = -1000
na1 = cobra_model.reactions.EX_na1_LPAREN_e_RPAREN_
na1.lower_bound = -1000
fe3 = cobra_model.reactions.EX_fe3_LPAREN_e_RPAREN_
fe3.lower_bound = -1000
nac = cobra_model.reactions.EX_nac_LPAREN_e_RPAREN_
nac.lower_bound = -1000
thym = cobra_model.reactions.EX_thym_LPAREN_e_RPAREN_
thym.lower_bound = -1000
ade = cobra_model.reactions.EX_ade_LPAREN_e_RPAREN_
ade.lower_bound = -1000
zn2 = cobra_model.reactions.EX_zn2_LPAREN_e_RPAREN_
zn2.lower_bound = -1000
cd2_L = cobra_model.reactions.EX_cd2_LPAREN_e_RPAREN_
cd2_L.lower_bound = -1000
glyc = cobra_model.reactions.EX_glyc_LPAREN_e_RPAREN_
glyc.lower_bound = -0.014

phe_L = cobra_model.reactions.EX_phe_DASH_L_LPAREN_e_RPAREN_
phe_L.lower_bound = -0.1
cys_L = cobra_model.reactions.EX_cys_DASH_L_LPAREN_e_RPAREN_
cys_L.lower_bound = 0
ile_L = cobra_model.reactions.EX_ile_DASH_L_LPAREN_e_RPAREN_
ile_L.lower_bound = -0.089
thr_L = cobra_model.reactions.EX_thr_DASH_L_LPAREN_e_RPAREN_
thr_L.lower_bound = -0.288
val_L = cobra_model.reactions.EX_val_DASH_L_LPAREN_e_RPAREN_
val_L.lower_bound = -0.071
pro_L = cobra_model.reactions.EX_pro_DASH_L_LPAREN_e_RPAREN_
pro_L.lower_bound = -0.1
his_L = cobra_model.reactions.EX_his_DASH_L_LPAREN_e_RPAREN_
his_L.lower_bound = -1.642
leu_L = cobra_model.reactions.EX_leu_DASH_L_LPAREN_e_RPAREN_
leu_L.lower_bound = -0.1
ura = cobra_model.reactions.EX_ura_LPAREN_e_RPAREN_
ura.lower_bound = -1000
tyr_L = cobra_model.reactions.EX_tyr_DASH_L_LPAREN_e_RPAREN_
tyr_L.lower_bound = -0.035
trp_L = cobra_model.reactions.EX_trp_DASH_L_LPAREN_e_RPAREN_
trp_L.lower_bound = 0
met_L = cobra_model.reactions.EX_met_DASH_L_LPAREN_e_RPAREN_
met_L.lower_bound = -0.1
ser_L = cobra_model.reactions.EX_ser_DASH_L_LPAREN_e_RPAREN_
ser_L.lower_bound = -1.722
arg_L = cobra_model.reactions.EX_arg_DASH_L_LPAREN_e_RPAREN_
arg_L.lower_bound = -1.17
asp_L = cobra_model.reactions.EX_asp_DASH_L_LPAREN_e_RPAREN_
asp_L.lower_bound = -0.041
lys_L = cobra_model.reactions.EX_lys_DASH_L_LPAREN_e_RPAREN_
lys_L.lower_bound = -0.1
ala_L = cobra_model.reactions.EX_ala_DASH_L_LPAREN_e_RPAREN_
ala_L.lower_bound = -0.369
gln_L = cobra_model.reactions.EX_gln_DASH_L_LPAREN_e_RPAREN_
gln_L.lower_bound = -0.445
glu_L = cobra_model.reactions.EX_glu_DASH_L_LPAREN_e_RPAREN_
glu_L.lower_bound = 0
leu_L = cobra_model.reactions.EX_leu_DASH_L_LPAREN_e_RPAREN_
leu_L.lower_bound = -0.235
met_D = cobra_model.reactions.EX_met_DASH_D_LPAREN_e_RPAREN_
met_D.lower_bound = -0.084
met_L = cobra_model.reactions.EX_met_DASH_L_LPAREN_e_RPAREN_
met_L.lower_bound = -0.084
tre = cobra_model.reactions.EX_tre_LPAREN_e_RPAREN_
tre.lower_bound = -0.6

####4. Gene knockout
#ADHE b1241 knockout
#1. ACALD (b0351 or b1241)
acald = cobra_model.reactions.ACALD
acald.upper_bound = 1/2 * acald.upper_bound

#2. ALCD2x (b1478 or b1241 or b0356)
alcd2x = cobra_model.reactions.ALCD2x
alcd2x.upper_bound = 1/3 * alcd2x.upper_bound

####5. Set the objective function
obj_rxn = cobra_model.reactions.Ec_biomass_iJO1366_WT_53p95M
obj_rxn.objective_coefficient = 1
cobra_model.optimize()

fva_file = open("FVA_adhe.txt", "w")
print(cobra_model.solution.f, file=fva_file)

obj_rxn.upper_bound = obj_rxn.lower_bound = cobra_model.solution.f
FVA_result = cobra.flux_analysis.flux_variability_analysis(
    cobra_model, fraction_of_optimum=1.0,
    number_of_processes=30)
rxns_list = cobra_model.reactions
for r in rxns_list:
    print (r.id, FVA_result[r.id]["maximum"],
           FVA_result[r.id]["minimum"], file=fva_file, sep='\t')

fva_file.close()
