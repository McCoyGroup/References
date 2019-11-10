## <a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader">GaussianFChkReader</a>
Implements a stream based reader for a Gaussian .fchk file. Pretty generall I think. Should be robust-ish.
    One place to change things up is convenient parsers for specific commonly pulled parts of the fchk

### Properties and Methods
```python
registered_components: dict
common_names: dict
to_common_name: dict
fchk_re_pattern: str
fchk_re: Pattern
```
<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.read_header">&nbsp;</a>
```python
read_header(self): 
```
Reads the header and skips the stream to where we want to be
- `:returns`: `str`
    >the header

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.get_next_block_params">&nbsp;</a>
```python
get_next_block_params(self): 
```
Pulls the tag of the next block, the type, the number of bytes it'll be,
        and if it's a single-line block it'll also spit back the block itself
- `:returns`: `dict`
    >No description...

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.get_block">&nbsp;</a>
```python
get_block(self, name=None, dtype=None, byte_count=None, value=None): 
```
Pulls the next block by first pulling the block tag
- `:returns`: `_`
    >No description...

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.skip_block">&nbsp;</a>
```python
skip_block(self, name=None, dtype=None, byte_count=None, value=None): 
```
Skips the next block
- `:returns`: `_`
    >No description...

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.parse">&nbsp;</a>
```python
parse(self, keys=None): 
```

### Examples
