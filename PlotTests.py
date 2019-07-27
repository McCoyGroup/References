
from Peeves.TestUtils import *
from unittest import TestCase
from McUtils.Plots import *
import sys, os, numpy as np

class PlotsTests(TestCase):

    @classmethod
    def tearDownClass(cls):
        import matplotlib.pyplot as plt
        # plt.show()

    @validationTest
    def test_Scatter(self):
        pts = np.random.rand(50, 2)
        plot = ScatterPlot(*pts.T)

    @validationTest
    def test_Plot(self):
        pts = np.random.rand(50)
        sins = np.sin(pts)
        plot = ScatterPlot(pts, sins)

    @validationTest
    def test_ListContourPlot(self):
        pts = np.pi*np.random.rand(150, 2)
        sins = np.sin(pts[:, 0])
        coses = np.cos(pts[:, 1])
        ptss = np.concatenate((pts, np.reshape(sins*coses, sins.shape + (1,))), axis=1)
        plot = ListContourPlot(ptss)

    @validationTest
    def test_ListTriPlot3D(self):
        pts = np.pi*np.random.rand(150, 2)
        sins = np.sin(pts[:, 0])
        coses = np.cos(pts[:, 1])
        ptss = np.concatenate((pts, np.reshape(sins*coses, sins.shape + (1,))), axis=1)
        plot = ListTriPlot3D(ptss)

    @validationTest
    def test_ListTriDensityPlot(self):
        pts = np.pi*np.random.rand(150, 2)
        sins = np.sin(pts[:, 0])
        coses = np.cos(pts[:, 1])
        ptss = np.concatenate((pts, np.reshape(sins*coses, sins.shape + (1,))), axis=1)
        plot = ListTriContourPlot(ptss)

    @validationTest
    def test_ListTriContourPlot(self):
        pts = np.pi*np.random.rand(150, 2)
        sins = np.sin(pts[:, 0])
        coses = np.cos(pts[:, 1])
        ptss = np.concatenate((pts, np.reshape(sins*coses, sins.shape + (1,))), axis=1)
        plot = ListTriContourPlot(ptss)
        plot.add_colorbar()

    @validationTest
    def test_Plot3D(self):
        import matplotlib.cm as colormaps

        f = lambda pt: np.sin(pt[0]) + np.cos(pt[1])
        plot = Plot3D(f, np.arange(0, 2*np.pi, .1), np.arange(0, 2*np.pi, .1),
                      plot_style = {
                          "cmap" : colormaps.get_cmap('viridis')
                      },
                      axes_labels = ['dogs', 'cats',
                                     Graphics.styled('rats', color='red')
                                     ],
                      plot_label = 'my super cool 3D plot',
                      plot_range = [(-5, 5)]*3,
                      plot_legend = 'i lik turtle',
                      colorbar = True
                      )

    @debugTest
    def test_Animation(self):
        def get_data(*args):
            pts = np.pi*np.random.normal(scale = .25, size=(10550, 2))
            sins = np.sin(pts[:, 0])
            coses = np.cos(pts[:, 1])
            ptss = np.concatenate((pts, np.reshape(sins*coses, sins.shape + (1,))), axis=1)
            return (ptss, )
        plot = ListTriContourPlot(*get_data(),
                                  animate = get_data,
                                  plot_range = [
                                      [-np.pi, np.pi],
                                      [-np.pi, np.pi]
                                  ]
                                  )
        # plot.show()


    # @debugTest
    # def test_Plot3D_adaptive(self):
    #     f = lambda pt: np.sin(pt[0]) + np.cos(pt[1])
    #     plot = Plot3D(f, [0, 2*np.pi], [0, 2*np.pi])
    #     plot.show()

