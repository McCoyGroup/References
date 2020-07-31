# Config Files

The standard config layout looks like

```python

# Preamble -- anything you need to get loaded
...

# Config dict

config = dict(
    param1=val,
    param2=val2,
    ...
)
```

This gets loaded in as a python module. 
To make this dynamically editable, all of the values in the `config` dict should be serializeable in a plain text format (think strings, lists of numbers, tuples, etc.). 
This could be relaxed in the future, but for now this just makes life way easier.

Every piece of the system (i.e. the main interface, the potentials, the simulations, the importance samplers) has a `config.py` file that you can edit to change up how it works.

If this were a properly static format, it'd be easily editable via the CLI and I'd be using JSON, but then I'd have to figure out how to define patterns like `["O", "H", "H"] * 3` or `["O"] * 6 + ["H"] * (2*6)` in an easily digestible way with JSON. 
I opted not to do that.

In general, try to keep things static, but a little bit of dynamic interaction (e.g. that multiplication from before), won't be the end of the world.

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/RynLib/ConfigFiles.md)