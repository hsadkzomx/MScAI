#!/bin/sh

# submitting a batch job is done by running this submit.sh from the Kay login node, eg:
#
# ssh username@kay.ichec.ie
# cd /ichec/home/users/username/
# sbatch submit.sh

# The #SBATCH directives must be commented out as below - don't uncomment them. see docs.
#SBATCH --time=0:10:00
#SBATCH --nodes=1
#SBATCH --partition=CourseDevQ
#SBATCH --reservation=MScAI
#SBATCH --account=course
#SBATCH --mail-user=your.email@nuigalway.ie
#SBATCH --mail-type=BEGIN,END

module load taskfarm # set up the environment
#module load conda/2   # see docs
#source activate myenv # see docs
cd $SLURM_SUBMIT_DIR # this is the directory you're in when you run this $ submit.sh
taskfarm taskfarm.sh # we have to supply the file taskfarm.sh: see docs
