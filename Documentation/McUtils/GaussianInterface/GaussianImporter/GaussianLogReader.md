## <a id="McUtils.GaussianInterface.GaussianImporter.GaussianLogReader">GaussianLogReader</a>
Implements a stream based reader for a Gaussian .log file... a bit messy

### Properties and Methods
```python
registered_components: dict
default_keys: tuple
default_ordering: dict
```
```python
parse(self, keys=None, num=None): 
```
The main function we'll actually use. Parses bits out of a .log file.
- `keys`: `str or list(str)`
    >the keys we'd like to read from the log file
- `num`: `int or None`
    >for keys with multiple entries, the number of entries to pull
- `:returns`: `_`
    >No description...

### Examples
