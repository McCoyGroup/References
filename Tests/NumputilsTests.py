
from Peeves.TestUtils import *
from McUtils.Numputils import *
from unittest import TestCase
import numpy as np

class NumputilsTests(TestCase):

    @debugTest
    def test_SparseArray(self):
        array = SparseArray([
            [
                [1, 0, 0],
                [0, 0, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 1],
                [0, 1, 0],
                [1, 0, 0]
            ],
            [
                [0, 1, 0],
                [1, 0, 1],
                [0, 0, 1]
            ],
            [
                [1, 1, 0],
                [1, 0, 1],
                [0, 1, 1]
            ]
        ])

        self.assertEquals(array.shape, (4, 3, 3))
        tp = array.transpose((1, 0, 2))
        self.assertEquals(tp.shape, (3, 4, 3))
        self.assertLess(np.linalg.norm((tp.todense()-array.todense().transpose((1, 0, 2))).flatten()), 1e-8)
        self.assertEquals(array[2, :, 2].shape, (3,))
        td = array.tensordot(array, axes=[1, 1])
        self.assertEquals(td.shape, (4, 3, 4, 3))
        self.assertEquals(array.tensordot(array, axes=[[1, 2], [1, 2]]).shape, (4, 4))