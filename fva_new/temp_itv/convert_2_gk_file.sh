mkdir heat_gk_data; python heat_cond2gkfile.py itv heat_gk_data/
mkdir cold_gk_data; python cold_cond2gkfile.py itv cold_gk_data/
python var_gene_heat.py heat heat_gk_data/ 1103
python var_gene_cold.py cold cold_gk_data/ 1103
