
from Peeves.TestUtils import *
from unittest import TestCase
from McUtils.CPotentialLib import *

class RynDMCTests(TestCase):

    @validationTest
    def load_cap(self):
        import sys
        sys.path.insert(0, TestManager.test_data_dir)
        import constantPot as cp
        return cp.potential

    @validationTest
    def test_loadPot(self):
        self.assertEquals(type(self.load_cap()).__name__, "PyCapsule")

    @validationTest
    def test_CPot(self):
        walker = np.array([
            [0.9578400,0.0000000,0.0000000],
            [-0.2399535,0.9272970,0.0000000],
            [0.0000000,0.0000000,0.0000000]
        ])
        self.assertEquals(
            CPotential(self.load_cap())(["H", "H", "O"], walker),
            52.0
        )