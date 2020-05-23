
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
    def test_Plot(self):
        grid = np.linspace(0, 2*np.pi, 100)
        plot = Plot(grid, np.sin(grid))
        # plot.show()

    @validationTest
    def test_Scatter(self):
        pts = np.random.rand(50, 2)
        plot = ScatterPlot(*pts.T)

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
                                     Graphics.modified('rats', color='red')
                                     ],
                      plot_label = 'my super cool 3D plot',
                      plot_range = [(-5, 5)]*3,
                      plot_legend = 'i lik turtle',
                      colorbar = True
                      )

    @validationTest
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

    @validationTest
    def test_VTK(self):
        plot = Graphics3D(backend="VTK", image_size=[1500, 500])
        Sphere().plot(plot)
        # plot.show()

    # @debugTest
    # def test_Plot3D_adaptive(self):
    #     f = lambda pt: np.sin(pt[0]) + np.cos(pt[1])
    #     plot = Plot3D(f, [0, 2*np.pi], [0, 2*np.pi])
    #     plot.show()

    @validationTest
    def test_PlotDelayed(self):
        p = Plot(background = 'black')
        for i, c in enumerate(('red', 'white', 'blue')):
            p.plot(np.sin, [-2 + 4/3*i, -2 + 4/3*(i+1)], color = c)
        # p.show()

    @validationTest
    def test_Plot3DDelayed(self):
        p = Plot3D(background = 'black')
        for i, c in enumerate(('red', 'white', 'blue')):
            p.plot(
                lambda g: (
                    np.sin(g.T[0]) + np.cos(g.T[1])
                ),
                [-2 + 4/3*i, -2 + 4/3*(i+1)],
                [-2 + 4/3*i, -2 + 4/3*(i+1)],
                color = c)
        # p.show()

    @validationTest
    def test_GraphicsGrid(self):

        main = GraphicsGrid(ncols=3, nrows=1)
        grid = np.linspace(0, 2 * np.pi, 100)
        grid_2D = np.meshgrid(grid, grid)
        main[0, 0] = ContourPlot(grid_2D[1], grid_2D[0], np.sin(grid_2D[0]), figure=main[0, 0])
        main[0, 1] = ContourPlot(grid_2D[1], grid_2D[0], np.sin(grid_2D[0])*np.cos(grid_2D[1]), figure=main[0, 1])
        main[0, 2] = ContourPlot(grid_2D[1], grid_2D[0], np.cos(grid_2D[1]), figure=main[0, 2])
        main.colorbar = { "graphics" : main[0, 1].graphics } # the spec
        main[0, 1].axes_labels = ["dogs (arb.)", "cats (cc)"]
        # main.show()
        # fig_path = os.path.expanduser("~/Desktop/test.png")
        # main.figure.savefig(fig_path)
        # import subprocess
        # subprocess.call(["open", fig_path])