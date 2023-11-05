for i in ./fva_conditionsaa.sh; do `srun -c 30 -e $i.err3 bash $i >$i.out3 &`; done
