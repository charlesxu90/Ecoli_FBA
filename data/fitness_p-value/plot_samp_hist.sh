python ./plot_samp_hist.py ./rand_3sample/sampling_all.out && \
  mv ./bin_cond_disp_genes.svg ./bin_3c_cond_disp_genes.svg  && \
  mv ./bin_cond_ess_genes.svg ./bin_3c_cond_ess_genes.svg 

python ./plot_samp_hist.py ./rand_4sample/sampling_all.out && \
  mv ./bin_cond_disp_genes.svg ./bin_4c_cond_disp_genes.svg  && \
  mv ./bin_cond_ess_genes.svg ./bin_4c_cond_ess_genes.svg
