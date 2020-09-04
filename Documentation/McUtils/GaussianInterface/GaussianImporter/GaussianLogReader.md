## <a id="McUtils.GaussianInterface.GaussianImporter.GaussianLogReader">GaussianLogReader</a>
Implements a stream based reader for a Gaussian .log file... a bit messy

### Properties and Methods
```python
registered_components: OrderedDict
default_keys: tuple
default_ordering: dict
job_default_keys: dict
```
<a id="McUtils.GaussianInterface.GaussianImporter.GaussianLogReader.parse">&nbsp;</a>
```python
parse(self, keys=None, num=None, reset=False): 
```
The main function we'll actually use. Parses bits out of a .log file.
- `keys`: `str or list(str)`
    >the keys we'd like to read from the log file
- `num`: `int or None`
    >for keys with multiple entries, the number of entries to pull
- `:returns`: `_`
    >No description...

<a id="McUtils.GaussianInterface.GaussianImporter.GaussianLogReader.get_default_keys">&nbsp;</a>
```python
get_default_keys(self): 
```

### Examples
We're working on improving this documentation, but in the meantime, here are the unit tests we use

```python
from McUtils.GaussianInterface import GaussianLogReader

def test_GetLogInfo(self):
    with GaussianLogReader(TestManager.test_data("tbhp_030.log")) as reader:
        parse = reader.parse("Header")
    self.assertIn("P", parse["Header"].job)

def test_DefaultLogParse(self):
    with GaussianLogReader(TestManager.test_data("tbhp_030.log")) as reader:
        parse = reader.parse()
    self.assertLess(parse["OptimizedScanEnergies"][1][0], -308)

def test_GetDipoles(self):
    with GaussianLogReader(self.test_log_water) as reader:
        parse = reader.parse("DipoleMoments")
    dips = parse["DipoleMoments"]
    self.assertIsInstance(dips, np.ndarray)
    self.assertEquals(dips.shape, (251, 3))

def test_GaussianLoad(self):
    with GaussianLogReader(self.test_log_water) as reader:
        parse = reader.parse("InputZMatrix")
    zmat = parse["InputZMatrix"]
    self.assertIsInstance(zmat, str)

def test_GaussianAllCartesians(self):
    with GaussianLogReader(self.test_log_water) as reader:
        parse = reader.parse("CartesianCoordinates")
    carts = parse["CartesianCoordinates"]
    self.assertIsInstance(carts[1], np.ndarray)
    self.assertEquals(carts[1].shape, (502, 3, 3))

def test_GaussianCartesians(self):
    with GaussianLogReader(self.test_log_water) as reader:
        parse = reader.parse("CartesianCoordinates", num=15)
    carts = parse["CartesianCoordinates"]
    self.assertIsInstance(carts[1], np.ndarray)
    self.assertEquals(carts[1].shape, (15, 3, 3))

def test_GaussianStandardCartesians(self):
    with GaussianLogReader(self.test_log_water) as reader:
        parse = reader.parse("StandardCartesianCoordinates", num=15)
    carts = parse["StandardCartesianCoordinates"]
    self.assertIsInstance(carts[1], np.ndarray)
    self.assertEquals(carts[1].shape, (15, 3, 3))

def test_GaussianZMatrixCartesians(self):
    with GaussianLogReader(self.test_log_water) as reader:
        parse = reader.parse("ZMatCartesianCoordinates", num=15)
    carts = parse["ZMatCartesianCoordinates"]
    self.assertIsInstance(carts[1], np.ndarray)
    self.assertEquals(carts[1].shape, (15, 3, 3))

def test_GZMatCoords(self):
    with GaussianLogReader(self.test_log_water) as reader:
        parse = reader.parse("ZMatrices", num = 3)
    zmats = parse["ZMatrices"]
    # print(zmats, file=sys.stderr)
    self.assertIsInstance(zmats[0][1][0], str)
    self.assertIsInstance(zmats[1], np.ndarray)
    self.assertEquals(zmats[1].shape, (3, 3))
    self.assertEquals(zmats[2].shape, (3, 3, 3))

def test_ScanEnergies(self):
    with GaussianLogReader(self.test_log_tet) as reader:
        parse = reader.parse("ScanEnergies", num=3)
    engs = parse["ScanEnergies"]
    self.assertIsInstance(engs, dict)
    self.assertIsInstance(engs["values"], np.ndarray)
    self.assertIsInstance(engs["coords"], np.ndarray)
    self.assertEquals(engs["coords"].shape, (5,))
    self.assertEquals(engs["values"].shape, (30, 5))

def test_GZMatCoordsBiggie(self):
    num_pulled = 5
    num_entries = 8
    with GaussianLogReader(self.test_log_h2) as reader:
        parse = reader.parse("ZMatrices", num = num_pulled)
    zmats = parse["ZMatrices"]
    # print(zmats, file=sys.stderr)
    self.assertIsInstance(zmats[1], np.ndarray)
    self.assertEquals(zmats[1].shape, (num_entries, 3))
    self.assertEquals(zmats[2].shape, (num_pulled, num_entries, 3))

def test_OptScanEnergies(self):
    with GaussianLogReader(self.test_log_opt) as reader:
        parse = reader.parse("OptimizedScanEnergies")
    e, c = parse["OptimizedScanEnergies"]
    self.assertIsInstance(e, np.ndarray)
    self.assertEquals(e.shape, (10,))
    self.assertEquals(len(c.keys()), 14)
    self.assertEquals(list(c.values())[0].shape, (10,))

def test_OptDips(self):
    with GaussianLogReader(self.test_log_tet_rel) as reader:
        parse = reader.parse(["OptimizedScanEnergies", "OptimizedDipoleMoments"])
    c = np.array(parse["OptimizedDipoleMoments"])
    self.assertIsInstance(c, np.ndarray)
    self.assertEquals(c.shape, (30,3))

def test_XMatrix(self):
    file=TestManager.test_data('qooh1.log')
    with GaussianLogReader(file) as reader:
        parse = reader.parse("XMatrix")
    X = np.array(parse["XMatrix"])

    self.assertIsInstance(X, np.ndarray)
    self.assertEquals(X.shape, (39, 39))
    self.assertEquals(X[0, 10], -0.126703)
    self.assertEquals(X[33, 26], -0.642702E-1)

```

___

[Edit Examples on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/McUtils/GaussianInterface/GaussianImporter/GaussianLogReader.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/McUtils/GaussianInterface/GaussianImporter/GaussianLogReader.md)