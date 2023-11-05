#!/bin/sh
#
#SBATCH --job-name=FBA_test
#SBATCH --time=60:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --partition=snapdragon-default
#
# Display all variables set by slurm
env | grep "^SLURM" | sort
#
# Print hostname job executed on.

/cbrc/software/anaconda/v2.1.0.app/bin/python ./useEcoli201131.py >FBA_test$(hostname -s)$$.txt
echo
echo "My hostname is: $(hostname -s)"
echo
