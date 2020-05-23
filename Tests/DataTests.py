
from Peeves.TestUtils import *
from unittest import TestCase
from McUtils.Data import *

class DataTests(TestCase):

    @validationTest
    def test_AtomData(self):
        self.assertIsInstance(AtomData["H"], dict)
        self.assertIsInstance(AtomData["Hydrogen"], dict)
        self.assertIsInstance(AtomData["Helium3"], dict)
        self.assertIs(AtomData["Hydrogen2"], AtomData["Deuterium"])
        self.assertIs(AtomData["H2"], AtomData["Deuterium"])
        self.assertIs(AtomData["H1"], AtomData["Hydrogen"])
        self.assertIs(AtomData[8], AtomData["Oxygen"])

    @validationTest
    def test_AtomMasses(self):
        self.assertLess(AtomData["Helium3", "Mass"], AtomData["T"]["Mass"]) # fun weird divergence

    @validationTest
    def test_Conversions(self):
        # print(AtomData["T"]["Mass"]-AtomData["Helium3", "Mass"], file=sys.stderr)
        self.assertGreater(UnitsData.data[("Hartrees", "InverseMeters")]["Value"], 21947463.13)
        self.assertLess(UnitsData.data[("Hartrees", "InverseMeters")]["Value"], 21947463.14)
        self.assertAlmostEqual(
            UnitsData.convert("Hartrees", "Wavenumbers"),
            UnitsData.convert("Hartrees", "InverseMeters") / 100
        )
        self.assertAlmostEqual(
            UnitsData.convert("Hartrees", "Wavenumbers"),
            UnitsData.convert("Centihartrees", "InverseMeters")
        )

    @validationTest
    def test_AtomicUnits(self):
        # print(UnitsData["AtomicUnitOfMass"])
        self.assertAlmostEqual(UnitsData.convert("AtomicMassUnits", "AtomicUnitOfMass"), 1822.888486217313)

    @debugTest
    def test_BondData(self):
        self.assertIsInstance(BondData["H"], dict)
        self.assertLess(BondData["H", "H", 1], 1)
        self.assertLess(BondData["H", "O", 1], 1)
        self.assertGreater(BondData["H", "C", 1], 1)