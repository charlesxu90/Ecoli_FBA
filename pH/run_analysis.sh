### 1.  convert condition files into mutant files under certain 
###     condition group

#python temp_cold_cond2gkfile.py max cold_data/ 
#python temp_heat_cond2gkfile.py max heat_data/

### remove SPA/Allele/Linked tagged genes.

#mkdir -p ./cold_data/essential/ && \
#mv ./cold_data/*-\ SPA.txt cold_data/essential
#mv ./cold_data/*-\ Allele.txt cold_data/essential
#mv ./cold_data/*-\ Linked.txt cold_data/essential
#rm -rf ./cold_data/essential/ 
#
#mkdir -p ./heat_data/essential/ && \
#mv ./heat_data/*-\ SPA.txt heat_data/essential
#mv ./heat_data/*-\ Allele.txt heat_data/essential
#mv ./heat_data/*-\ Linked.txt heat_data/essential
#rm -rf ./heat_data/essential/

### 2. Calculate the flux variances under certain condition group

#ls cold_data/| wc -l
#python ./var_gene_cold.py max cold_data/ 1184
#ls heat_data/| wc -l
#python ./var_gene_heat.py max heat_data/ 1184

### 3. Plot histogram for variances under certian condition group

python var_analysis.py ./var_heat_max.tsv heat
python var_analysis.py ./var_cold_max.tsv cold

### 4. Check genes in different ranges
#python ./var_analysis_10bins.py ./var_heat_max.tsv heat
#python ./var_analysis_10bins.py ./var_cold_max.tsv cold

#mkdir -p heat_10bins
#mkdir -p cold_10bins
#mv p*0_cold.txt cold_10bins
#mv p*0_heat.txt heat_10bins
# then copy cold_10bin.sh file to cold_10bins directory.
# and copy heat_10bin.sh file to heat_10bins directory.
#cp cold_10bin/cold_10bin.sh cold_10bins/ 
#cp heat_10bin/heat_10bin.sh heat_10bins/ 

### 5. Plot 10 bin bar chart
python plot_10bins.py ./cold_10bins_ess.tsv cold
python plot_10bins.py ./heat_10bins_ess.tsv heat

### 6. Calculate p-value for 10bin chart
Rscript ./pval_high_pH.R 
Rscript ./pval_low_pH.R 

