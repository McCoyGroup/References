
from Peeves.TestUtils import *
from unittest import TestCase
from McUtils.GaussianInterface import *
import sys, os

class GaussianInterfaceTests(TestCase):

    test_log_water = TestManager.test_data("water_OH_scan.log")
    test_log_freq = TestManager.test_data("water_freq.log")
    test_fchk = TestManager.test_data("water_freq.fchk")
    test_log_h2 = TestManager.test_data("outer_H2_scan_new.log")

    @validationTest
    def test_GetDipoles(self):
        with GaussianLogReader(self.test_log_water) as reader:
            parse = reader.parse("DipoleMoments")
        dips = parse["DipoleMoments"]
        self.assertIsInstance(dips, np.ndarray)

    @validationTest
    def test_GaussianLoad(self):
        with GaussianLogReader(self.test_log_water) as reader:
            parse = reader.parse("InputZMatrix")
        zmat = parse["InputZMatrix"]
        self.assertIsInstance(zmat, str)

    @validationTest
    def test_GaussianCartesians(self):
        with GaussianLogReader(self.test_log_water) as reader:
            parse = reader.parse("CartesianCoordinates", num = 15)
        carts = parse["CartesianCoordinates"]
        self.assertIsInstance(carts[1], np.ndarray)
        self.assertEquals(carts[1].shape, (15, 3, 3))

    @validationTest
    def test_GZMatCoords(self):
        with GaussianLogReader(self.test_log_water) as reader:
            parse = reader.parse("ZMatrices", num = 3)
        zmats = parse["ZMatrices"]
        # print(zmats, file=sys.stderr)
        self.assertIsInstance(zmats[1], np.ndarray)
        self.assertEquals(zmats[1].shape, (2, 3))
        self.assertEquals(zmats[2].shape, (3, 2, 3))

    @validationTest
    def test_GZMatCoordsBiggie(self):
        num_pulled = 5
        num_entries = 8
        with GaussianLogReader(self.test_log_h2) as reader:
            parse = reader.parse("ZMatrices", num = num_pulled)
        zmats = parse["ZMatrices"]
        # print(zmats, file=sys.stderr)
        self.assertIsInstance(zmats[1], np.ndarray)
        self.assertEquals(zmats[1].shape, (num_entries-1, 3))
        self.assertEquals(zmats[2].shape, (num_pulled, num_entries-1, 3))

    @validationTest
    def test_Fchk(self):
        with GaussianFChkReader(self.test_fchk) as reader:
            parse = reader.parse()
        key = next(iter(parse.keys()))
        self.assertIsInstance(key, str)

    @validationTest
    def test_ForceConstants(self):
        n = 3 # water
        with GaussianFChkReader(self.test_fchk) as reader:
            parse = reader.parse("ForceConstants")
        fcs = parse["ForceConstants"]
        self.assertEquals(fcs.n, n)
        self.assertEquals(fcs.array.shape, (3*n, 3*n))

    @validationTest
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
            np.allclose(a, a.T, rtol=1e-08, atol=1e-08)
            )

    @validationTest
    def test_ForceFourthDerivatives(self):
        n = 3 # water
        with GaussianFChkReader(self.test_fchk) as reader:
            parse = reader.parse("ForceDerivatives")
        fcs = parse["ForceDerivatives"]
        tds = fcs.fourth_deriv_array
        self.assertEquals(fcs.n, n)
        self.assertEquals(tds.shape, ((3*n-6), (3*n), 3*n))
        a = tds[0]
        self.assertTrue(
            np.allclose(a, a.T, rtol=1e-08, atol=1e-08)
        )

    @validationTest
    def test_FchkMasses(self):
        n = 3 # water
        with GaussianFChkReader(self.test_fchk) as reader:
            parse = reader.parse("AtomicMasses")
        masses = parse["AtomicMasses"]
        self.assertEquals(len(masses), n)

    @validationTest
    def test_GaussianJobWriter(self):
        job = GaussianJob(
            "water scan",
            description="Simple water scan",
            config= GaussianJob.Config(
                NProc = 4,
                Mem = '1000MB'
            ),
            job= GaussianJob.Job(
                'Scan'
            ),
            system = GaussianJob.System(
                charge=0,
                molecule=[
                    ["O", "H", "H"],
                    [
                        [0, 0, 0],
                        [.987, 0, 0],
                        [0, .987, 0]
                    ]
                ],
                vars=[
                    GaussianJob.System.Variable("y1", 0., 10., .1),
                    GaussianJob.System.Constant("x1", 10)
                ]

            )
        )
        # print(job.write(), file=sys.stderr)
        self.assertIsInstance(job.format(), str)
