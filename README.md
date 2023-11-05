# E.coli FBA

Analyze E. coli code and heat response with FBA

## 1. Install cobrapy and associated packages.
```shell
sudo apt-get install libglpk-dev
sudo pip install cobra --pre
sudo pip install python-libsbml
sudo pip install numpy,scipy
```
Note: Many other packages need to be installed to use python libsbml.

## 2. Modify the model to fit for E. coli BW225113
Include reactions: ARAI, RBK_L1, RMPA, LYXI, RMI, RMK, and LACZ.
Gap filling: 
```python
python read_ecoli2011.py
```

## 3. Set constraints for LB media/culture
Following:http://2013.igem.org/Team:KU_Leuven/Project/Glucosemodel/MeS/Modelling-FBA
```
python read_ecoli2011.py
```

## 4. Gene Knockout
Based on data from Phenotypic Landscape of a Bacterial Cell, mmc2.xlsx
E. coli gene mapping is downloaded from supplementary file of
```text
Riley, et al. Escherichia coli k-12: a cooperatively developed annotation snapshot2005. NAR, 34(1):1–9, 2006
```
Mapping genes to reactions, change constraints based on protein abundance data from PaxDb.
```shell
python Gene2React.py
```
## 5. Flux balance analysis
```shell
python ./fba/Ecoli_FBA.py
```

## 6. Map fitness to growth rates
```shell
python ./fva/colonySize2GrowthRate.py 
```

## 7. Flux variability analysis
```shell
python ./fva/Ecoli_FVA.py
```

## 8. Draw graphs
```shell
./sample_heatmap/plot.sh # Draw heatmaps for sample mutants

./temp/var_analysis.py  # Draw histogram for mutants using mean of flux variances
./temp/plot_10bins.py # Draw 10 bin bar chart.

./temp/cold_10bins/cold_10bin.sh #check essentiality and dispensability in each 10 bins
./temp/cold_10bins/disp_var_max.py # used to find maximum variance reactions

./temp/cold_10bins/pathways/cytoscape_data.py # prepare data for cytoscape
./temp/cold_10bins/pathways/top100_rxn_max.py # Find top100 reaction ids for mutants, draw heatmaps for reactions
```

