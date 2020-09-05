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
<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.read_header" class="docs-object-method">&nbsp;</a>
```python
read_header(self): 
```
Reads the header and skips the stream to where we want to be
- `:returns`: `str`
    >the header

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.get_next_block_params" class="docs-object-method">&nbsp;</a>
```python
get_next_block_params(self): 
```
Pulls the tag of the next block, the type, the number of bytes it'll be,
        and if it's a single-line block it'll also spit back the block itself
- `:returns`: `dict`
    >No description...

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.get_block" class="docs-object-method">&nbsp;</a>
```python
get_block(self, name=None, dtype=None, byte_count=None, value=None): 
```
Pulls the next block by first pulling the block tag
- `:returns`: `_`
    >No description...

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.skip_block" class="docs-object-method">&nbsp;</a>
```python
skip_block(self, name=None, dtype=None, byte_count=None, value=None): 
```
Skips the next block
- `:returns`: `_`
    >No description...

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianFChkReader.parse" class="docs-object-method">&nbsp;</a>
```python
parse(self, keys=None): 
```

### Examples
```python

def test_Fchk(self):
    with GaussianFChkReader(self.test_fchk) as reader:
        parse = reader.parse()
    key = next(iter(parse.keys()))
    self.assertIsInstance(key, str)


def test_ForceConstants(self):
    n = 3 # water
    with GaussianFChkReader(self.test_fchk) as reader:
        parse = reader.parse("ForceConstants")
    fcs = parse["ForceConstants"]
    self.assertEquals(fcs.n, n)
    self.assertEquals(fcs.array.shape, (3*n, 3*n))


def test_ForceThirdDerivatives(self):
    n = 3 # water
    with GaussianFChkReader(self.test_fchk) as reader:
        parse = reader.parse("ForceDerivatives")
    fcs = parse["ForceDerivatives"]
    tds = fcs.third_deriv_array
    self.assertEquals(fcs.n, n)
    self.assertEquals(tds.shape, ((3*n-6), (3*n), 3*n))
    a = tds[0]
    self.assertTrue(
        np.allclose(tds[0], tds[0].T, rtol=1e-08, atol=1e-08)
    )
    self.assertTrue(
        np.allclose(tds[1], tds[1].T, rtol=1e-08, atol=1e-08)
    )
    self.assertTrue(
        np.allclose(tds[2], tds[2].T, rtol=1e-08, atol=1e-08)
    )


def test_ForceFourthDerivatives(self):
    n = 3 # water
    with GaussianFChkReader(self.test_fchk) as reader:
        parse = reader.parse("ForceDerivatives")
    fcs = parse["ForceDerivatives"]
    tds = fcs.fourth_deriv_array
    self.assertEquals(fcs.n, n)
    self.assertEquals(tds.shape, ((3*n-6), (3*n-6), (3*n), 3*n)) # it's a SparseTensor now
    slice_0 = tds[0, 0].toarray()
    slice_1 = tds[1, 1].toarray()
    slice_2 = tds[2, 2].toarray()
    self.assertTrue(
        np.allclose(slice_0, slice_0.T, rtol=1e-08, atol=1e-08)
    )
    self.assertTrue(
        np.allclose(slice_1, slice_1.T, rtol=1e-08, atol=1e-08)
    )
    self.assertTrue(
        np.allclose(slice_2, slice_2.T, rtol=1e-08, atol=1e-08)
    )


def test_FchkMasses(self):
    n = 3 # water
    with GaussianFChkReader(self.test_fchk) as reader:
        parse = reader.parse("AtomicMasses")
    masses = parse["AtomicMasses"]
    self.assertEquals(len(masses), n)
```

___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/GaussianInterface/GaussianImporter/GaussianFChkReader.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/GaussianInterface/GaussianImporter/GaussianFChkReader.md) <br/>
[Edit Docstrings on GitHub](https://github.com/McCoyGroup/McUtils/edit/master/GaussianInterface/GaussianImporter.py?message=Update%20Docs)