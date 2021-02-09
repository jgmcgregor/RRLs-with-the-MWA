#!/bin/bash -l
#SBATCH --partition=workq
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --array=0-127

module load singularity

name=sgrA

i=$((SLURM_ARRAY_TASK_ID * 24))
j=$((i + 24))

# Sequence indices are inclusive
for chan in $(seq -f "%04g" $i $j)
do
    if [[ ! -e ${name}_weighted_stack-${chan}.fits ]] || [[ ! -s ${name}_weighted_stack-${chan}.fits ]]
    then
        echo $chan
        first=`ls ../12*/12????????_fine-${chan}-dirty.fits | head -1`
        singularity run /astro/mwasci/tgalvin/gleamx_testing_small.img SWarp -c ${name}_weight.swarp.template -IMAGEOUT_NAME ${name}_weighted_stack-${chan}.fits -WEIGHTOUT_NAME ${name}_weighted_stack-${chan}-weight.fits ../12*/12????????_fine-${chan}-dirty.fits
        freq=`singularity run /astro/mwasci/tgalvin/gleamx_testing_small.img pyhead.py -p CRVAL3 $first | awk '{print $3}'`
        singularity run /astro/mwasci/tgalvin/gleamx_testing_small.img pyhead.py -u FREQ $freq ${name}_weighted_stack-${chan}.fits
        rm ${name}_weighted_stack-${chan}-weight.fits
    fi
done
