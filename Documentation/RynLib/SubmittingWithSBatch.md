# Submitting Jobs

The basic idea no matter where one submits is to do something like this

```shell
module load <MPI> # must be inline with what is inside container
# load any other modules we need

RYNLIB_PATH=<path-to-the-RynLib-folder>
. $RYNLIB_PATH/setup/env.sh
# set RYNLIB_ENTOS_PATH if we're using entos
# set RYNLIB_IMAGE if we're not using the defaults
RUNTIME_FLAGS=... # can be like -L $PWD/RynLib if we're using a version of the RynLib source code in $PWD
rynlib=$(rynlib $RUNTIME_FLAGS -e) # we use -e echo the command that rynlib would run, since `mpirun` doesn't like not being passed an executable

# SET THINGS LIKE OMP_NUM_THREADS
# SPECIFY BIDING MODE FOR MPI JOBS

# Do any non-parallel setup, e.g. doing a sim archive of an old simulation + a sim add or a sim copy
JOB_NAME=...
SIMULATION_SOURCE=<path/to/folder>
$rynlib sim archive $JOB_NAME
$rynlib sim add $JOB_NAME $SIMULATION_SOURCE
...

# Do the core parallel job we want to run, commonly a sim run
NUM_MPI_JOBS=... # usually like 28 or 32 * number of nodes
mpirun -n $NUM_MPI_JOBS $rynlib sim run $JOB_NAME
```

### Singularity

If we're targeting Singularity/Hyak we want to load these modules

```shell
module load gcc_19-ompi_3.1.4
module load singularity
```

### Shifter

With Shifter we have a slight subtlety in that `sbatch` has been set up to take an `image` argument, e.g.

```shell
#--SBATCH image=<whatever/image/we're/using>
```

and I think on Shifter systems we can use `srun` instead of `mpirun`...