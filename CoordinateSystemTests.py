
from Peeves.TestUtils import *
from unittest import TestCase
from Psience.Coordinerds import *
import sys

class CoordinateSystemTests(TestCase):

    @validationTest
    def test_ZMatrixStep(self):
        self.assertEquals(ZMatrixCoordinates.displacement(.1), .1)
    @validationTest
    def test_CartStep(self):
        self.assertEquals(CartesianCoordinates3D.displacement(.1), .1)
    @validationTest
    def test_CartExpanded(self):
        expansion = (np.array(
            [
                [1/np.sqrt(6), np.sqrt(2/3), 1/np.sqrt(6)],
                [1/np.sqrt(3), -(1/np.sqrt(3)), 1/np.sqrt(3)],
                [1/np.sqrt(2), 0, -(1/np.sqrt(2))]
        ]
        ))
        system = CoordinateSystem(
            basis=CartesianCoordinates3D,
            matrix=expansion
        )
        disp = system.displacement(.1)
        self.assertEquals(disp.shape, (3, ))
