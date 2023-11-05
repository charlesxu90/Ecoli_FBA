awk 'NR % 2== 0' cold_10bins/ess_disp_10bins.tsv >cold_10bins_ess.tsv
awk 'NR % 2== 0' heat_10bins/ess_disp_10bins.tsv >heat_10bins_ess.tsv
python plot_10bins.py heat_10bins_ess.tsv heat
python plot_10bins.py cold_10bins_ess.tsv cold
