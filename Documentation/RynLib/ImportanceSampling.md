# Importance Simpling

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