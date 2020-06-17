
from Peeves.TestUtils import *
from unittest import TestCase
from McUtils.Coordinerds import *
from McUtils.Plots import ArrayPlot, TensorPlot
from McUtils.Numputils import *
import sys, numpy as np

class ConverterTest(TestCase):

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

    def initialize_data(self):
        self.n = 10
        self.test_zmats = CoordinateSet(DataGenerator.zmats(self.n, 15), system=ZMatrixCoordinates)
        self.test_carts = CoordinateSet(DataGenerator.multicoords(self.n, 10))
        self.test_structure = [
            [ 0.0,                    0.0,                   0.0                ],
            [ 0.5312106220949451,     0.0,                   0.0                ],
            [ 5.4908987527698905e-2,  0.5746865893353914,    0.0                ],
            [-6.188515885294378e-2,  -2.4189926062338385e-2, 0.4721688095375285 ],
            [ 1.53308938205413e-2,    0.3833690190410768,    0.23086294551212294],
            [ 0.1310095622893345,     0.30435650497612,      0.5316931774973834 ]
        ]
        self.dihed_test_structure = np.array([
            [0.0, 0.0, 0.0 ],
            [-0.8247121421923925, -0.629530611338456, 1.775332267901544 ],
            [0.1318851447521099, 2.088940054609643, 0.0],
            [1.786540362044548, -1.386051328559878, 0.0],
            [2.233806981137821, 0.3567096955165336, 0.0],
            [-0.8247121421923925, -0.629530611338456, -1.775332267901544]
        ])
        self.zm_conv_test_structure = np.array([
            [1.0, 0.0, 1.0],
            [-0.8247121421923925, -0.629530611338456, 1.775332267901544],
            [0.1318851447521099, 2.088940054609643, 0.0],
            [1.786540362044548, -1.386051328559878, 0.0],
            [2.233806981137821, 0.3567096955165336, 0.0],
            [-0.8247121421923925, -0.629530611338456, -1.775332267901544]
        ])

    @validationTest
    def test_GetDihedrals(self):
        from McUtils.Coordinerds.CoordinateTransformations.TransformationUtilities.VectorOps import pts_dihedrals as calc_dihed

        orig = self.dihed_test_structure

        dihed = calc_dihed(orig[3:5], orig[2:4], orig[1:3], orig[0:2])
        self.assertEquals(round(dihed[0], 6), round(.591539, 6))
    @validationTest
    def test_CoordinateSet(self):
        import numpy as np
        coord_set = CoordinateSet(DataGenerator.coords(500))
        self.assertIsInstance(coord_set, np.ndarray)
    @validationTest
    def test_Loader(self):
        loaded = CoordinateSystemConverters.get_converter(CartesianCoordinates3D, ZMatrixCoordinates)
        self.assertIsInstance(loaded, CoordinateSystemConverter)
    @validationTest
    def test_CartesianToZMatrix(self):
        coord_set = CoordinateSet(DataGenerator.coords(10))
        coord_set = coord_set.convert(ZMatrixCoordinates, use_rad = False)
        self.assertEqual(coord_set.shape, (9, 6))
    @validationTest
    def test_CartesianToZMatrixMulti(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(10, 10))
        coord_set = coord_set.convert(ZMatrixCoordinates, use_rad = False)
        self.assertEqual(coord_set.shape, (10, 9, 6))

    @validationTest
    def test_CartesianToZMatrixAndBack(self):
        cs1 = coord_set = CoordinateSet([self.zm_conv_test_structure]*4)
        coord_set = coord_set.convert(ZMatrixCoordinates)
        coord_set = coord_set.convert(CartesianCoordinates3D)
        cs2 = coord_set
        # print(np.round(cs2[0], 3))
        self.assertEqual(round(np.linalg.norm(cs2 - cs1), 8), 0.)

    @validationTest
    def test_ExpansionCoordinates(self):
        np.random.seed(0)
        coord_set = CoordinateSet([self.test_structure] * 2)
        expansion_1 = np.random.rand(len(self.test_structure)*3, len(self.test_structure)*3)
        expansion_1 = (expansion_1 / np.broadcast_to(np.linalg.norm(expansion_1, axis=0), expansion_1.shape))
        cs1 = CoordinateSystem("CartesianExpanded",
                               basis=CartesianCoordinates3D,
                               matrix=expansion_1
                               )
        expansion_2 = np.random.rand((len(self.test_structure) - 1) * 3, (len(self.test_structure) - 1) * 3)
        expansion_2 = (expansion_2 / np.broadcast_to(np.linalg.norm(expansion_2, axis=0), expansion_2.shape))
        cs2 = CoordinateSystem("ZMatrixExpanded",
                               basis=ZMatrixCoordinates,
                               matrix=expansion_2
                               )
        coord_set2 = coord_set.convert(cs1)
        coord_set2 = coord_set2.convert(cs2)
        coord_set2 = coord_set2.convert(CartesianCoordinates3D)
        self.assertEqual(round(np.linalg.norm(coord_set2 - coord_set), 8), 0.)
    @validationTest
    def test_ZMatrixToCartesian(self):
        # print(self.test_zmats.coords[0, 0], file=sys.stderr)
        coords = self.test_zmats.convert(CartesianCoordinates3D, use_rad = False)
        self.assertEqual(coords.shape, (self.n, 16, 3))
    @validationTest
    def test_NumpyLikeTest(self):
        # print(self.test_zmats.coords[0, 0], file=sys.stderr)
        coords = self.test_zmats.convert(CartesianCoordinates3D, use_rad = False)
        self.assertAlmostEqual(np.linalg.norm(coords - coords), 0.)
    # @timeitTest(number=2500)
    # def test_CartToZTiming(self):
    #     coord_set = self.test_carts
    #     coord_set = coord_set.convert(ZMatrixCoordinates, use_rad = False)
    #     self.assertEqual(coord_set.shape, (self.n, 9, 6))
    # @timeitTest(number=2500)
    # def test_ZMatrixToCartesianTiming(self):
    #     coords = self.test_zmats.convert(CartesianCoordinates3D, use_rad = False)
    #     self.assertEqual(coords.shape, (self.n, 16, 3))

    #region Jacobians
    @validationTest
    def test_CartesianToZMatrixJacobian(self):
        coord_set = CoordinateSet(DataGenerator.coords(10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, stencil = 3)
        # print(np.round(jacob, 2), file = sys.stderr)
        # ArrayPlot(jacob.reshape(10*3, (10-1)*3), colorbar=True).show()
        self.assertEquals(jacob.shape, (10*3, 10 - 1, 3)) # we always lose one atom

    @validationTest
    def test_CartesianToZMatrixMultiJacobian(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(10, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, stencil = 5)
        # ArrayPlot(jacob[0], colorbar=True).show()
        self.assertEquals(jacob.shape, (10*3, 10, 10 - 1, 3 )) # we always lose one atom

    @validationTest
    def test_CH5ZMatJacobian(self):
        coord_set = CoordinateSet([
            [
                [ 0.000000000000000,    0.000000000000000,  0.000000000000000],
                [ 0.1318851447521099,   2.088940054609643,  0.000000000000000],
                [ 1.786540362044548,   -1.386051328559878,  0.000000000000000],
                [ 2.233806981137821,    0.3567096955165336, 0.000000000000000],
                [-0.8247121421923925, -0.6295306113384560, -1.775332267901544],
                [-0.8247121421923925, -0.6295306113384560,  1.775332267901544]
            ]
            ]*100,
            system=CartesianCoordinates3D
        )

        zmat_system = ZMatrixCoordinateSystem(
            ordering=[
                [ 0,  0, -1, -1],
                [ 1,  0,  1, -1],
                [ 2,  0,  1,  2],
                [ 3,  0,  1,  2],
                [ 4,  0,  1,  2],
                [ 5,  0,  1,  2]
            ]
        )
        # zmcs = coord_set.convert(ZMatrixCoordinates, ordering=zmat_ordering)

        jacob = coord_set.jacobian(
            zmat_system,
            stencil=5,
            prep=lambda coord, disps, zmcs: (disps, zmcs[..., :, 1])
        )
        self.assertEquals(jacob.shape, (np.product(coord_set.shape[1:]), 100, 5)) # I requested 5 bond lengths

    @validationTest
    def test_CartesianToZMatrixMultiJacobian2(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(10, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, 2, stencil = 5)
        # TensorPlot(jacob[0],
        #            ticks_style = [
        #                dict(
        #                    bottom = False,
        #                    top = False,
        #                    labelbottom = False
        #                ),
        #                dict(
        #                    right = False,
        #                    left = False,
        #                    labelleft = False
        #                )
        #            ]
        #            ).show()
        self.assertEquals(jacob.shape, (10, 10*3, 10*3, 10 * 3 - 3 )) # we always lose one atom

    @timeitTest(number=1)
    def test_CartesianToZMatrixMultiJacobian1(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(1, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, stencil = 5)
        # ArrayPlot(jacob[0], colorbar=True).show()
        self.assertEquals(jacob.shape, (1, 10*3, 10 * 3 - 3 )) # we always lose one atom
    @timeitTest(number=1)
    def test_CartesianToZMatrixMultiJacobian10(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(10, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, stencil = 5)
        # ArrayPlot(jacob[0], colorbar=True).show()
        self.assertEquals(jacob.shape, (10, 10*3, 10 * 3 - 3 )) # we always lose one atom
    @timeitTest(number=1)
    def test_CartesianToZMatrixMultiJacobian2Timing10(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(10, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, 2, stencil = 5)
        # ArrayPlot(jacob[0], colorbar=True).show()
        self.assertEquals(jacob.shape, (10, 10*3, 10*3, 10 * 3 - 3 )) # we always lose one atom
    @timeitTest(number=1)
    def test_CartesianToZMatrixMultiJacobian3Timing1(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(1, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, 3, stencil = 5)
        # ArrayPlot(jacob[0], colorbar=True).show()
        self.assertEquals(jacob.shape, (1, 10*3, 10*3, 10*3, 10 * 3 - 3 )) # we always lose one atom
    @timeitTest(number=1)
    def test_CartesianToZMatrixMultiJacobian3Timing10(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(10, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, 3, stencil = 5)
        # ArrayPlot(jacob[0], colorbar=True).show()
        self.assertEquals(jacob.shape, (10, 10*3, 10*3, 10*3, 10 * 3 - 3 )) # we always lose one atom

    @validationTest
    def test_CartesianToZMatrixMultiJacobian3(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(10, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, 3, stencil=5)
        # ArrayPlot(jacob[0], colorbar=True).show()
        self.assertEquals(jacob.shape, (10, 10 * 3, 10 * 3, 10 * 3, 10 * 3 - 3))  # we always lose one atom

    @validationTest
    def test_CartesianToZMatrixMultiJacobianTargeted(self):
        coord_set = CoordinateSet(DataGenerator.multicoords(10, 10))
        jacob = coord_set.jacobian(ZMatrixCoordinates, stencil=5, coordinates=[[1, 2, 3], None])
        # ArrayPlot(jacob[0], colorbar=True).show()
        self.assertEquals(jacob.shape, (10, 3, 10 * 3 - 3))  # we always lose one atom

    #endregion

    #region CoordinateSystemTests

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
                [1 / np.sqrt(6), np.sqrt(2 / 3), 1 / np.sqrt(6)],
                [1 / np.sqrt(3), -(1 / np.sqrt(3)), 1 / np.sqrt(3)],
                [1 / np.sqrt(2), 0, -(1 / np.sqrt(2))]
            ]
        ))
        system = CoordinateSystem(
            basis=CartesianCoordinates3D,
            matrix=expansion
        )
        disp = system.displacement(.1)
        self.assertEquals(disp.shape, (3,))

    #endregion

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
