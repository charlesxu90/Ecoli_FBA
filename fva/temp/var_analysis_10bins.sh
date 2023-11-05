python var_analysis_10bins.py var_cold_cold.tsv cold
mkdir cold_10bins
mv p*_cold.txt cold_10bins/
python var_analysis_10bins.py var_heat_heat.tsv heat
mkdir heat_10bins
mv p*_heat.txt heat_10bins/
