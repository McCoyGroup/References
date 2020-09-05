## <a id="RynLib.DoMyCode.Simulation.SimulationParameters">SimulationParameters</a>
A parameters class that manages the data for a DMC simulation

### Properties and Methods
<a id="RynLib.DoMyCode.Simulation.SimulationParameters.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, **params): 
```
Sets up all the necessary simulation data to run a DMC
- `name`: `str`
    >name to be used when storing file data
- `description`: `str`
    >long description which isn't used for anything
- `walker_set`: `WalkerSet | dict`
    >the WalkerSet object that handles all the pure walker activities in the simulation
- `time_step`: `float`
    >the size of the timestep to use throughout the calculation
- `steps_per_propagation`: `int`
    >the number of steps to move over before branching in a propagate call
- `num_time_steps`: `int`
    >the total number of time steps the simulation should run for (initially)
- `alpha`: `float`
    >used in finding the branching correction to the reference potential
- `potential`: `function or callable`
    >the function that will take a set of atoms and sets of configurations and spit back out potential value
- `descendent_weighting`: `(int, int)`
    >the number of steps before descendent weighting and the number of steps to go before saving
- `log_file`: `str or stream or other file-like-object`
    >the file to write log stuff to
- `output_folder`: `str`
    >the folder to write all data stuff to
- `equilibration`: `int or callable`
    >the number of timesteps or method to determine equilibration
- `write_wavefunctions`: `bool`
    >whether or not to write wavefunctions to file after descedent weighting
- `checkpoint_at`: `int or None`
    >the number of timesteps to progress before checkpointing (None means never)
- `verbosity`: `int`
    >the verbosity level for log printing
- `zpe_averages`: `int`
    >the number of steps to average the ZPE over
- `dummied`: `bool`
    >whether or not to just use for potential calls (exists for hooking into MPI and parallel methods)
- `world_rank`: `int`
    >the world_rank of the processor in an MPI call

<a id="RynLib.DoMyCode.Simulation.SimulationParameters.serialize" class="docs-object-method">&nbsp;</a>
```python
serialize(self, simulation, file, mode=None): 
```

### Examples


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/RynLib/DoMyCode/Simulation/SimulationParameters.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/RynLib/DoMyCode/Simulation/SimulationParameters.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/RynLib/DoMyCode/Simulation/SimulationParameters.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/RynLib/DoMyCode/Simulation/SimulationParameters.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/RynLib/edit/master/DoMyCode/Simulation.py?message=Update%20Docs)