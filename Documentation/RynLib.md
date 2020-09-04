# <a id="RynLib">RynLib</a>
    
This started out as a quick layer between python and entos for running DMC

It's grown a bit...

### Overview

We provide an environment in which to run DMC with the potential of your choice with whatever little bells and whistles your little heart desires.

The system as designed has three segments to it, a general DMC package, a package for working with compiled potentials, and a package for managing MPI.
The DMC package makes use of the compiled potentials and the MPI manager, using them to distribute its walkers to the various available cores and evaluating the energies.

The presence of so many moving parts, however, means that there are lots of knobs and levers available to tweak.
Some of these, like the MPI, are set automatically, unless there's an override on the user side, but others, like the configuration of the potential, need user input.

Everything has been designed to run inside a container, which adds another layer of complexity.

The first thing we have to do is actually install the package and build it out. All changes live on GitHub, so we'll start by cloning the repository

```ignorelang
git clone https://github.com/McCoyGroup/RynLib.git RynLib
```

### Installing

`RynLib` is distributed as a containerized application through [DockerHub](https://hub.docker.com/repository/docker/mccoygroup/rynlib)

We'll use this to install RynLib onto our local machines or HPCs. 

You can find some more details [here](RynLib/Installing.md).

### The rynlib CLI

As a containerized application intended for use in an HPC environment, `RynLib` is mostly run as a command-line tool. At a later date, this might be distributed in a `module`-like way, but for now these tools are stored in `RynLib/setup/env.sh`, which you'll load in via the [`source`](https://linuxize.com/post/bash-source-command/) command (or its alias `.`)

```ignorelang
. RynLib/setup/env.sh
```

This will define the bash function `rynlib` which should be able to determine your HPC environment and work accordingly. 
More documentation on this can be found [here](RynLib/CommandLineInterface.md).

### Building

We currently distribute RynLib building off of Ubuntu and CentOS, with OpenMPI and MPICH as the MPI implementations.
If you want to build `RynLib` with a different underlying OS or different OS, you can can look at `RynLib/setup/build` and the various `Dockerfile` setups we have there.

### Config Files

Most of the parts of the package (i.e. the simulations, potentials, and importance samplers) are set up using configuration files. 
There is a standardized configuration format for these files, which is a weird JSON-like python file. 
It's simple enough that I'm disinclined to change it, unless someone has a very strong opinion.

You can find more info [here](RynLib/ConfigFiles.md)

## MPI

Working with MPI can also be a little subtle when running on an HPC. 
You'll need to make sure that the MPI inside the container matches the MPI you load outside. 

## Potentials

One of the big benefits of RynLib is simplifying the process of using compiled potentials. 
Many potentials have already been made accessible, but it's still worth knowing how the system works.

Potentials are generally stored in `/config/potentials` and you load them using the `PotentialManager` class in `PlzNumbers`.
Once loaded, a potential can be called just like any other callable object in python.

More info is [here](RynLib/Potentials.md)

## Simulations

Managing simulations is much simpler than managing potentials. 
To get a simulation set up, we just create a `config.py` file inside a directory and use

```ignorelang
rynlib sim add NAME SRC
```

and everything in that directory will get copied into the container's managed space.

Once we have our simulation added, we can start to work with it. Details on that are [here](RynLib/Simulations.md).

## Setting up Importance Sampling

An implementation of importance sampling is baked into the package, but this requires a user-side function to evaluate the trial wavefunction. Details are [here](RynLib/ImportanceSampling.md)

## Writing an SBATCH file

A core use case for all of this is High-Performance Computing environments. 
Both NeRSC and the local University of Washington cluster use the SLURM scheduler for jobs, so I can only detail how this works with `sbatch`, not sure about other schedulers.

Some sample scripts are [here](RynLib/SubmittingWithSBatch.md).

## Examples

We're collecting examples to provide concrete use cases. You can find them [here](RynLib/Examples).

### Modules

  - [Interface](RynLib/Interface.md)
  - [DoMyCode](RynLib/DoMyCode.md)
  - [Dumpi](RynLib/Dumpi.md)
  - [PlzNumbers](RynLib/PlzNumbers.md)
  - [RynUtils](RynLib/RynUtils.md)

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/RynLib.md)