#!/bin/bash -l
#SBATCH --partition=workq
#SBATCH --time=01:00:00
#SBATCH --nodes=1
#SBATCH --mem=120g
module load singularity

singularity run  /astro/mwasci/tgalvin/gleamx_testing_small.img python make_cube.py sgrA_weighted_stack

if [[ -e cube.fits ]]
then
#    rm sgrA_weighted_stack-????.fits
    mv cube.fits sgrA_cube.fits
    exit 0
else
    exit 1
fi
