from Peeves.TestUtils import *
from unittest import TestCase
from McUtils.Coordinerds import *
from McUtils.Numputils import *
import sys, numpy as np

class TransformationTests(TestCase):

    def setUp(self):
        super().setUp()
        self.initialize_data()
        self.load()

    @property
    def loaded(self):
        return hasattr(self, "cases")

    def load(self, n=10):
        if not self.loaded:
            self.cases = n
            self.transforms = DataGenerator.mats(n)
            self.shifts = DataGenerator.vecs(n)
            self.mats = affine_matrix(self.transforms, self.shifts)

    initialize_data = ConverterTest.initialize_data

    #region CoordinateTests

    @validationTest
    def test_AffineMatDim(self):
        self.assertEqual(self.mats.shape, (self.cases, 4, 4))

    @debugTest
    def test_TranslationTransform(self):
        t = CoordinateTransform(TranslationTransform(np.array([-1, -2, -2])))
        point = np.array([1, 5, 2])
        self.assertEquals((0, 3, 0), tuple(t(point)))

    @debugTest
    def test_TranslationTransformMany(self):
        t = CoordinateTransform(TranslationTransform(np.array([-1, -2, -2])))
        point = np.array([1, 5, 2])
        point = np.broadcast_to(point[np.newaxis], (10, 3))
        wat = t(point)
        self.assertEquals((0, 3, 0), tuple(wat[0]))

    @debugTest
    def test_RotationTransform(self):
        t = CoordinateTransform(RotationTransform(np.pi/2))
        point = np.array([1, 1, 0])
        self.assertTrue(np.allclose(t.transformation_function.transform, [[0, -1, 0], [1, 0, 0], [0, 0, 1]]))
        self.assertTrue(np.allclose((-1, 1, 0), t(point)))

    @debugTest
    def test_RotationTranslationTransform(self):
        translation = TranslationTransform(np.array([-1, -2, -2]))
        rotation = RotationTransform(np.pi / 2)
        t = CoordinateTransform(rotation, translation)
        point = np.array([2, 3, 2])
        a = t.transformation_function #type: AffineTransform
        self.assertTrue(np.allclose(CoordinateTransform(rotation)(CoordinateTransform(translation)(point)), t(point)))

    @validationTest
    def test_AffineMatMul(self):
        vecs = DataGenerator.vecs(self.cases)
        vec_prod = affine_multiply(self.mats, vecs)
        vec_prod2 = np.array([a @ b for a, b in zip(self.mats, one_pad_vecs(vecs))])[:, :3]
        self.assertAlmostEqual(np.sum(vec_prod - vec_prod2), 0.)

    @validationTest
    def test_AffineMats(self):
        vecs = DataGenerator.vecs(self.cases)
        vec_prod = affine_multiply(self.mats, vecs)
        affine_inv = np.asarray([np.linalg.inv(m) for m in self.mats])
        vecs2 = affine_multiply(affine_inv, vec_prod)
        self.assertAlmostEqual(np.sum(vecs - vecs2), 0.)
    #endregion