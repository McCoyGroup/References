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