# Working with the Entos Potential

## Configuring the Wrapper

There are two special potentials in RynLib. One is the test `HarmonicOscillator` potential. The other is [`entos`](https://www.entos.info/). 

The version of Entos that Rynlib uses isn't publicly available, so if you _aren't_ on the project that `RynLib` was invented to help solve, then there's probably no way for you to use Entos inside RynLib.

If you _are_ on the project, for licensing and versioning reasons, Entos isn't bundled in a RynLib container, but it's been made easy to use.

We have to first configure the wrapper around `libentos.so`, by running

```bash
rynlib pot configure-entos
```

and then by setting the `RYNLIB_ENTOS_PATH` variable to point to a version of Entos that was pulled out of its original docker container via `extract_entos`.

## Using Entos

Once wrapped and made available, entos can be called like any other potential, with a slight subtlety. 
The version of Entos we work with is for testing the behaviour of MOB-ML post-HF models. 
So we have a flag `hf_only` in the code that we need to set. Since I don't yet support key-word arguments in `PlzNumbers` this means we end up passing a mysterious `False` to say that we _don't_ want only HF.

```python
pm = PotentialManager()
entos = pm.load_potential("entos")
entos(coordinates, atoms, False)
```