## <a id="McUtils.Data.ConstantsData.UnitsDataHandler">UnitsDataHandler</a>


### Properties and Methods
```python
prefix_map: OrderedDict
postfix_map: OrderedDict
```
```python
__init__(self): 
```

```python
load(self): 
```

```python
find_conversion(self, unit, target): 
```
Attempts to find a conversion between two sets of units. Currently only implemented for "plain" units.
- `unit`: `Any`
    >No description...
- `target`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

```python
add_conversion(self, unit, target, value): 
```

```python
convert(self, unit, target): 
```
Converts base unit into target using the scraped NIST data
- `unit`: `Any`
    >No description...
- `target`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

### Examples
