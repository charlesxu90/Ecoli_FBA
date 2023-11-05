python var_analysis_10bins.py var_low_low.tsv low
mkdir low_10bins
mv p*_low.txt low_10bins/
python var_analysis_10bins.py var_high_high.tsv high
mkdir high_10bins
mv p*_high.txt high_10bins/
