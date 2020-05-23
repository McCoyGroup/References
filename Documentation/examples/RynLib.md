
The first thing we have to do is actually install the package and build it out. All changes live on GitHub, so we'll start by cloning the repository

```ignorelang
git clone https://github.com/McCoyGroup/RynLib.git RynLib
```

### Installing

`RynLib` is distributed as a containerized application through [DockerHub](https://hub.docker.com/repository/docker/mccoygroup/rynlib)

We'll use this to install RynLib onto our local machines or HPCs. 

You can find some more details [here](Installing.md).

### The rynlib CLI

As a containerized application intended for use in an HPC environment, `RynLib` is mostly run as a command-line tool. At a later date, this might be distributed in a `module`-like way, but for now these tools are stored in `RynLib/setup/env.sh`, which you'll load in via the [`source`](https://linuxize.com/post/bash-source-command/) command (or its alias `.`)

```shell script
. RynLib/setup/env.sh
```

This will define the bash function `rynlib` which should be able to determine your HPC environment and work accordingly. 
More documentation on this can be found [here](CommandLineInterface.md).

### Building

We currently distribute RynLib building off of Ubuntu and CentOS, with OpenMPI and MPICH as the MPI implementations.
If you want to build `RynLib` with a different underlying OS or different OS, you can can look at `RynLib/setup/build` and the various `Dockerfile` setups we have there.

### Config Files

Most of the parts of the package (i.e. the simulations, potentials, and importance samplers) are set up using configuration files. 
There is a standardized configuration format for these files, which is a weird JSON-like python file. 
It's simple enough that I'm disinclined to change it, unless someone has a very strong opinion.

You can find more info [here](ConfigFiles.md)

## MPI

Working with MPI can also be a little subtle when running on an HPC. 
You'll need to make sure that the MPI inside the container matches the MPI you load outside. 

## Potentials

One of the big benefits of RynLib is simplifying the process of using compiled potentials. 
Many potentials have already been made accessible, but it's still worth knowing how the system works.

Potentials are generally stored in `/config/potentials` and you load them using the `PotentialManager` class in `PlzNumbers`.
Once loaded, a potential can be called just like any other callable object in python.

More info is [here](Potentials.md)

## Setting up a Simulation

This will feel much like setting up a potential, but maybe a little bit simpler. 
We'll pass a directory (`SRC`) that contains a `config.py` file to set up the simulation as well as any other data that we might need to load in, e.g. a set of initial walkers.

```ignorelang
rynlib sim add NAME SRC
```

## Setting up Importance Sampling

An implementation of importance sampling is baked into the package, but this requires a user-side function to evaluate the trial wavefunction.
To make the config files as stateless as possible and to make it possible to use the same trial wavefunction over different simulation instances (think using 3000 vs 10000 walkers on the same system) we've added this as another object type that you can add to the container, via

```ignorelang
rynlib sim add_sampler NAME SRC
```

where the `SRC` directory stores any underlying data needed by the sampler and contains a `config.py` file that provides the configuration options.
The main configuration option for this is

```python
"""
:param module: the file to load that provides the trial wavefunction
:type module: str
"""
```

where _module_ will be a plain `.py` file that has a function in it called `trial_wavefunction` defined like 

```python
def trial_wavefunction(coords, atoms, *parameters):
    """
    :param coords: the WalkerSet that holds the configurations (might be many configurations at once!)
    """
    ...
    return psi
```

## Writing an SBATCH file

A core use case for all of this is High-Performance Computing environments. Both NeRSC and the local University of Washington cluster use the SLURM scheduler for jobs, so here are usage instructions for using this with SLURM

### Docker

Docker shouldn't be used on an HPC system

### Singularity

```ignorelang
#--SBATCH ... blah blah blah
#--SBATCH --nnodes=<number of nodes>
#--SBATCH ... blah blah blah
#--SBATCH ... blah blah blah

# <number of cores> will be close to 28 * <number of nodes>
module load gcc_19-ompi_3.1.4 # or whatever MPI module is available--must be 3.1.4 or in line with what is inside the container

RYNLIB_PATH=<path-to-the-RynLib-folder>
. $RYNLIB_PATH/setup/env.sh
mpirun -n <number of cores> rynlib sim run <name of simulation>
```

### Shifter

```ignorelang
#--SBATCH ... blah blah blah
#--SBATCH --nnodes=<number of nodes>
#--SBATCH ... blah blah blah
#--SBATCH ... blah blah blah

RYNLIB_PATH=<path-to-the-RynLib-folder>
#RYNLIB_ENTOS_PATH=... if we're using entos
. $RYNLIB_PATH/setup/env.sh
# <number of cores> will be close to 28 * <number of nodes>
srun -n <number of cores> rynlib sim run <name of simulation>
```