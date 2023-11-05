#!/bin/sh
#
#SBATCH --job-name=fva_conditionsac
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=snapdragon-default
#
# Display all variables set by slurm
env | grep "^SLURM" | sort
#
# Print hostname job executed on.

perl ./monitor.pl -i ./fva_conditionsac -u 1.0 >fva_conditionsac$(hostname -s)$$.txt
echo
echo "My hostname is: $(hostname -s)"
echo
