This is the procedure of analyzing E. coli FBA using Python

#####====================================####
1. Install cobrapy and associated packages.
sudo apt-get install libglpk-dev
sudo pip install cobra --pre
sudo pip install python-libsbml
sudo pip install numpy,scipy
#Note: Many other packages need to be installed to use python libsbml.

#####====================================####
2. Modify the model to fit for E. coli BW225113
Include reactions: ARAI, RBK_L1, RMPA, LYXI, RMI, RMK, and LACZ.
Gap filling: 

read_ecoli2011.py
#####====================================####
3. Set constraints for LB media/culture
Following:http://2013.igem.org/Team:KU_Leuven/Project/Glucosemodel/MeS/Modelling-FBA

read_ecoli2011.py
#####====================================####
4. Gene Knockout
Based on data from Phenotypic Landscape of a Bacterial Cell, mmc2.xlsx
E. coli gene mapping is downloaded from: http://www.uniprot.org/docs/ecoli
Mapping genes to reactions with percentage.

Gene2React.py
#####====================================####
5. Colony Size simulation

1. Get colony size and growth rate correlation based on the data B(x+C) = gRate
2. Set growth rate corresponding to gRate, and find the flux distribution

colSz2GRate.py
#####====================================####
6. Flux variability analysis
First, find the maximum growth rate under Knockout situation.
Then, Set the growth rate as maximum, and do flux variability analysis.

use_ecoli2011.py

