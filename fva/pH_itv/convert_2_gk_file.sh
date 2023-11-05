mkdir low_gk_data; python low_cond2gkfile.py itv low_gk_data/
mkdir high_gk_data; python high_cond2gkfile.py itv high_gk_data/
python var_gene_low.py low low_gk_data/ 1258
python var_gene_high.py high high_gk_data/ 1258
