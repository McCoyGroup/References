
from Peeves.TestUtils import *
from unittest import TestCase
from Psience.Coordinerds.CoordinateTransformations.TransformationUtilities import *
import sys

class CoordinateTests(TestCase):

    @property
    def loaded(self):
        return hasattr(self, "cases")
    def load(self, n=10):
        if not self.loaded:
            self.cases = n
            self.transforms = DataGenerator.mats(n)
            self.shifts = DataGenerator.vecs(n)
            self.mats = affine_matrix(self.transforms, self.shifts)
    def setUp(self):
        super().setUp()
        self.load()

    @validationTest
    def test_AffineMatDim(self):
        self.assertEqual(self.mats.shape, (self.cases, 4, 4))
    @validationTest
    def test_AffineMatMul(self):
        vecs = DataGenerator.vecs(self.cases)
        vec_prod = affine_multiply(self.mats, vecs)
        vec_prod2 = np.array([ a @ b for a, b in zip(self.mats, one_pad_vecs(vecs))])[:, :3]
        self.assertAlmostEqual(np.sum(vec_prod-vec_prod2), 0.)
    @validationTest
    def test_AffineMats(self):
        vecs = DataGenerator.vecs(self.cases)
        vec_prod = affine_multiply(self.mats, vecs)
        affine_inv = np.asarray([ np.linalg.inv(m) for m in self.mats ])
        vecs2 = affine_multiply(affine_inv, vec_prod)
        self.assertAlmostEqual(np.sum(vecs-vecs2), 0.)