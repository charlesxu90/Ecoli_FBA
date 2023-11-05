awk 'NR % 2== 0' low_10bins/ess_disp_10bins.tsv >low_10bins_ess.tsv
awk 'NR % 2== 0' high_10bins/ess_disp_10bins.tsv >high_10bins_ess.tsv
python plot_10bins.py high_10bins_ess.tsv high
python plot_10bins.py low_10bins_ess.tsv low
