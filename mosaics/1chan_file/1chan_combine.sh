#!/bin/bash -l
#SBATCH --partition=workq
#SBATCH --time=0:30:00
#SBATCH --nodes=1

# combines channel 1500 for all observations in a folder (use movein to select observations)

module load singularity

name=1d
chan=1500

# Sequence indices are inclusive
if [[ ! -e ${name}_weighted_stack-${chan}.fits ]] || [[ ! -s ${name}_weighted_stack-${chan}.fits ]]
then
    echo $chan
    first=`ls ../12*/12????????_fine-${chan}-dirty.fits | head -1`
    singularity run /astro/mwasci/tgalvin/gleamx_testing_small.img SWarp -c sgrA_weight.swarp.template -IMAGEOUT_NAME ${name}_weighted_stack-${chan}.fits -WEIGHTOUT_NAME ${name}_weighted_stack-${chan}-weight.fits ../12*/12????????_fine-${chan}-dirty.fits
    freq=`singularity run /astro/mwasci/tgalvin/gleamx_testing_small.img pyhead.py -p CRVAL3 $first | awk '{print $3}'`
    singularity run /astro/mwasci/tgalvin/gleamx_testing_small.img pyhead.py -u FREQ $freq ${name}_weighted_stack-${chan}.fits
    rm ${name}_weighted_stack-${chan}-weight.fits
fi
