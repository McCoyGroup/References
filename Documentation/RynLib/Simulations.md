# Simulations

The core use case of RynLib is to provide a convenient, scalable simulation environment for diffusion Monte Carlo.
To make that possible, all of the rest of this stuff was built out.

Dealing with simulations will (hopefully) feel very reminiscent of dealing with the potentials and importance samplers, though.

## Getting a Simulation Into a Container

The first thing we need to do is get a simulation set up that we can actually run, the command for this is

```shell
rynlib sim add NAME SRC
```

where _SRC_ is a directory accessible to the container, in which we have a `config.py` file and an initialization data the simulation might need.

For most new simulations, all we need is the `config.py` which will look like

```python
config = dict(
    description="...",              # a brief description of the simulation to help remember what it's doing
    potential=dict(
        name="...",                 # the name of the simulation
        parameters=...              # the parameters to passed in to the potential
    ),
    # # If we're using importance sampling, we turn this on
    # importance_sampler=dict( 
    #     name="...",
    #     parameters=...
    # ),
    walker_set=dict(
        atoms=[...],
        initial_walker=[...],      # can also be the path to a file containing an initial set of walkers to sample from
        #initial_weights=...,       # can be either a constant or a file with an initial set of weights that go with the walkers
        walkers_per_core=...
    ),
    time_step=...,                 # the time_step for the DMC simulation
    steps_per_propagation=...,     # the steps to propagate before branching (for efficiency)
    num_time_steps=...,            # the total number of timesteps
    checkpoint_every=...,          # how often to checkpoint the simulation
    equilibration_steps=...,       # the number of steps to consider 'equilibration'
    descendent_weight_every=...,   # how often to descendent weight
    descendent_weighting_steps=... # how many steps to propagate when descendent weighting
)
```

If we are initializing the walkers from an initial population, we note that the path to the initial walker file should look like `"data/name_of_file.npy`, as the `SRC` directory gets copied wholesale into the simulation's `"data"` directory.

The `potential` specified must be a potential that's already been installed, i.e. a name in the output of

```shell 
rylib pot list
```

## Running a Simulation

Once we have a simulation installed in the container, we can run it. The command for this is 

```shell 
rynlib sim run NAME
```

Usually, this will be done in an `sbatch` script or similar, as detailed [here](SubmittingWithSBatch.md).

### Restarting a Simulation

Commonly, we'll run out of time for a job before our simulation is done. 
If that's the case, we'll want to restart the simulation.

For safety, we'll probably also want to copy our original simulation, so we'll do

```shell 
rynlib sim copy NAME NAME_backup
rynlib sim restart NAME
```

then if that worked, we can remove the copy with `sim remove NAME_backup`


## Output

Simulations spit out a bunch of data, each simulation will provide an `energies.npy` file, a `log.txt` file, (if descendent weighting is on) descendent weights, and (if checkpointing is on) walkers in a `checkpoints` folder.

Of these, the only one that isn't obvious how to parse (the rest are `.npy` or `.npz` files) is the `log.txt` file. 
Each log has a header block that looks like

```ignorelang
RynLib DMC SIMULATION: NAME
DESCRIPTION

verbosity: ...
potential: Potential(...)
imp_samp: ImportanceSampler(...)
mpi_manager: MPIManagerObject(...)
num_walkers: ...
atoms: [...]
masses: [...]
sigmas: [...]
```

where the most relevant startup info is (hopefully) there.

For completeness, right below this the entire `config.py` is copied in.

After this, we have blocks that report on each propagation step that the simulation does (note that this usually involves multiple time steps)

```ignorelang
Starting step ...
Moving coordinates ... steps
    took ...s
Computing potential energy
    took ...s
Updating walker weights
    Energy: Min ... | Max ... | Mean ...
    Weight: Min ... | Max ... | Mean ...
    ...
Branching
Walkers being removed: ...
    Threshold: ...
    Energy: Max ... | Min ... | Mean ...
    Weight: Max ... | Min ... | Mean ...
Done branching:
    Energy: Max ... | Min ... | Mean ...
    Weight: Max ... | Min ... | Mean ...
  took ...s
Applying descendent weighting
DESCENDENT_WEIGHTING STATUS
CHECKPOINT_STATUS
Average Energy: ...
Zero-point Energy: ...
Runtime: ...s
```

this reports 
* how long it took to move the walkers (can be non-neglibile for large simulations)
* how long the potential call too, what the energies were like when updating the weights
* what changed with branching
* whether or not we're mid-descendent weighting
* whether or not we checkpoint
* some stats on the current energy
* the overall runtime

The log file isn't intended to be used as a serious data source, but rather as a way to check in on your simulation as it runs to make sure that everything is going smoothly.