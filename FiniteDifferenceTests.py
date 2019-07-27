
from Peeves.TestUtils import *
from McUtils.Zachary import *
from McUtils.Zachary.ZachLib import *
from McUtils.Plots import *
from unittest import TestCase
import sys

class FiniteDifferenceTests(TestCase):

    # @debugTest
    # def test_finite_difference_2d(self):
    #     grid_1 = 4*np.math.pi / 100 * np.arange(100) + 2*np.math.pi
    #     grid = np.meshgrid(grid_1, grid_1)
    #     self.assertAlmostEqual(1, 0)#round(np.linalg.norm(dtest - sin_d3_vals), 4), 0)

    @validationTest
    def test_finite_difference(self):
        sin_grid = np.linspace(0, 2*np.pi, 200)
        sin_vals = np.sin(sin_grid)
        sin_d3_vals = -np.cos(sin_grid)
        for ord in range(2, 10):
           dtest = finite_difference(sin_grid, sin_vals, 3, ord)
           cum_err = np.linalg.norm(dtest - sin_d3_vals)
           # print("Error {}.{}:".format(3, ord), cum_err, file=sys.stderr)
           self.assertLess(cum_err, .001)
        sin_d2_vals = -np.sin(sin_grid)
        for ord in range(2, 10):
            dtest_2 = finite_difference(sin_grid, sin_vals, 2, ord)
            cum_err = np.linalg.norm(dtest_2 - sin_d2_vals)
            # print("Error {}.{}:".format(2, ord), cum_err, file=sys.stderr)
            self.assertLess(cum_err, .001)

    @validationTest
    def test_FD2D(self):

        verbose = False

        x_grid = np.linspace(0, 2*np.pi, 200)
        y_grid = np.linspace(0, 2*np.pi, 100)
        sin_x_vals = np.sin(x_grid); sin_y_vals =  np.sin(y_grid)
        cos_x_vals = np.cos(x_grid); cos_y_vals =  np.cos(y_grid)
        vals_2D = np.outer(sin_x_vals, sin_y_vals)
        grid_2D = np.array(np.meshgrid(x_grid, y_grid)).T
        # try 1st and 1st derivs
        vals_2D_2 = np.outer(cos_x_vals, cos_y_vals)
        cum_errs = []
        for ord in range(4, 10, 2) if verbose else range(4, 5):
            fd_res_2 = finite_difference(grid_2D, vals_2D, (1, 1), (ord, ord))
            cum_err = np.linalg.norm(fd_res_2 - vals_2D_2) / len(grid_2D.flatten())
            if verbose:
                print("Error {}x{}.{}:".format(1, 1, ord), cum_err, file=sys.stderr)
                print("Max Dev: ", np.max(np.abs(fd_res_2 - vals_2D_2)), file=sys.stderr)
            cum_errs.append(cum_err)
            if not verbose:
                self.assertLess(cum_err, .001)
        if verbose:
            for cum_err in cum_errs:
                self.assertLess(cum_err, .001)

        # Plot3D(*grid_2D.transpose(2, 0, 1), vals_2D).show()

        # 1,2 mixed deriv
        vals_2D_2 = -np.outer(cos_x_vals, sin_y_vals)
        cum_errs = []
        for ord in range(4, 10, 2) if verbose else range(4, 5):
            fd_res_2 = finite_difference(grid_2D, vals_2D, (1, 2), (ord, ord))
            cum_err = np.linalg.norm(fd_res_2 - vals_2D_2) / len(grid_2D.flatten())
            if verbose:
                print("Error {}x{}.{}:".format(1, 2, ord), cum_err, file=sys.stderr)
                print("Max Dev: ", np.max(np.abs(fd_res_2 - vals_2D_2)), file=sys.stderr)
            cum_errs.append(cum_err)
            if not verbose:
                self.assertLess(cum_err, .005)

        if verbose:
            for cum_err in cum_errs:
                self.assertLess(cum_err, .005)

        # gg = GraphicsGrid(nrows=1, ncols=2, graphics_class=Graphics3D,
        #                   image_size = [800, 400],
        #                   fig_kw = {'figsize': (15, 5)}
        #                   )
        # Plot3D(*grid_2D.transpose(2, 0, 1),
        #        fd_res_2,
        #        plot_style={"cmap":"viridis"},
        #        figure = gg[0, 0],
        #        axes_labels = ['x', 'y', 'z']
        #        )
        # Plot3D(*grid_2D.transpose(2, 0, 1), vals_2D_2,
        #        plot_style={"cmap":"viridis"},
        #        figure = gg[0, 1],
        #        axes_labels = ['x', 'y', 'z']
        #        )
        # gg.show()

        cum_errs = []
        for ord in range(4, 10, 2) if verbose else range(4, 5): # even orders seem to work best?
            fd_res = finite_difference(grid_2D, vals_2D, (2, 2), (ord, ord))
            cum_err = np.linalg.norm(vals_2D - fd_res) / len(grid_2D.flatten())
            if verbose:
                print("Error {}x{}.{}:".format(2, 2, ord), cum_err, file=sys.stderr)
                print("Max Dev: ", np.max(np.abs(vals_2D - fd_res)), file=sys.stderr)
            cum_errs.append(cum_err)
            if not verbose:
                self.assertLess(cum_err, .001)
        if verbose:
            for cum_err in cum_errs:
                self.assertLess(cum_err, .001)

        # Plot3D(*grid_2D.T, vals_2D).show()

        # try 3rd and 3rd derivs
        vals_2D_2 = np.outer(cos_x_vals, cos_y_vals)
        cum_errs = []
        for ord in range(4, 10, 2) if verbose else range(4, 5):
            fd_res_2 = finite_difference(grid_2D, vals_2D, (3, 3), (ord, ord))
            cum_err = np.linalg.norm(fd_res_2 - vals_2D_2) / len(grid_2D.flatten())
            if verbose:
                print("Error {}x{}.{}:".format(3, 3, ord), cum_err, file=sys.stderr)
                print("Max Dev: ", np.max(np.abs(fd_res_2 - vals_2D_2)), file=sys.stderr)
            cum_errs.append(cum_err)
            if not verbose:
                self.assertLess(cum_err, .001)
        if verbose:
            for cum_err in cum_errs:
                self.assertLess(cum_err, .001)

        # try 2nd and 3rd derivs
        vals_2D_2 = np.outer(sin_x_vals, cos_y_vals)
        cum_errs = []
        for ord in range(6, 7):
            fd_res_2 = finite_difference(grid_2D, vals_2D, (2, 3), (ord, ord))
            cum_err = np.linalg.norm(fd_res_2 - vals_2D_2) / len(grid_2D.flatten())
            if verbose:
                print("Error {}x{}.{}:".format(2, 3, ord), cum_err, file=sys.stderr)
                print("Max Dev: ", np.max(np.abs(fd_res_2 - vals_2D_2)), file=sys.stderr)
            cum_errs.append(cum_err)
            if not verbose:
                self.assertLess(cum_err, .001)
        if verbose:
            for cum_err in cum_errs:
                self.assertLess(cum_err, .001)

    @validationTest
    def test_FD2D_multi(self):

        verbose = False

        x_grid = np.linspace(0, 2*np.pi, 200)
        y_grid = np.linspace(0, 2*np.pi, 100)
        sin_x_vals = np.sin(x_grid); sin_y_vals =  np.sin(y_grid)
        cos_x_vals = np.cos(x_grid); cos_y_vals =  np.cos(y_grid)
        vals_2D = np.outer(sin_x_vals, sin_y_vals)
        grid_2D = np.array(np.meshgrid(x_grid, y_grid)).T
        # try 1st and 1st derivs
        vals_2D_2 = np.outer(cos_x_vals, cos_y_vals)
        cum_errs = []
        for ord in range(4, 10, 2) if verbose else range(4, 5):
            fd_res_2_many = finite_difference(
                np.broadcast_to(grid_2D, (15, ) + grid_2D.shape),
                np.broadcast_to(vals_2D, (15, ) + vals_2D.shape),
                (1, 1),
                (ord, ord),
                axis = 1
            )
            for fd_res_2 in fd_res_2_many:
                cum_err = np.linalg.norm(fd_res_2 - vals_2D_2) / len(grid_2D.flatten())
                if verbose:
                    print("Error {}x{}.{}:".format(1, 1, ord), cum_err, file=sys.stderr)
                    print("Max Dev: ", np.max(np.abs(fd_res_2 - vals_2D_2)), file=sys.stderr)
                cum_errs.append(cum_err)
                if not verbose:
                    self.assertLess(cum_err, .001)

        gg = GraphicsGrid(nrows=1, ncols=2, graphics_class=Graphics3D,
                          image_size = [800, 400],
                          fig_kw = {'figsize': (15, 5)}
                          )
        Plot3D(*grid_2D.transpose(2, 0, 1),
               fd_res_2_many[0],
               plot_style={"cmap":"viridis"},
               figure = gg[0, 0],
               axes_labels = ['x', 'y', 'z']
               )
        Plot3D(*grid_2D.transpose(2, 0, 1), vals_2D_2,
               plot_style={"cmap":"viridis"},
               figure = gg[0, 1],
               axes_labels = ['x', 'y', 'z']
               )
        gg.show()

        if verbose:
            for cum_err in cum_errs:
                self.assertLess(cum_err, .001)

    @validationTest
    def test_stirs(self):
        stir = StirlingS1(8)
        ans = np.array([
            [1,  0,    0,     0,     0,   0,    0,  0],
            [0,  1,    0,     0,     0,   0,    0,  0],
            [0, -1,    1,     0,     0,   0,    0,  0],
            [0,  2,   -3,     1,     0,   0,    0,  0],
            [0, -6,    11,   -6,     1,   0,    0,  0],
            [0,  24,  -50,    35,   -10,  1,    0,  0],
            [0, -120,  274,  -225,   85, -15,   1,  0],
            [0,  720, -1764,  1624, -735, 175, -21, 1]
        ])
        # print(stir, file=sys.stderr)
        self.assertAlmostEqual(np.round(np.linalg.norm(stir-ans), 6), 0.)
    @validationTest
    def test_bin_gs(self):
        gbin = GammaBinomial(7/2, 8)
        ans = np.array([1., 3.5, 4.375, 2.1875, 0.273438, -0.0273438, 0.00683594, -0.00244141])
        # print(gbin, file=sys.stderr)
        self.assertAlmostEqual(np.round(np.linalg.norm(gbin-ans), 5), 0.)
    # @timeitTest(number=500)
    # def test_bin_speed_old(self):
    #    FiniteDifferenceFunction._old_Bin(55)
    # @timeitTest(number=500)
    # def test_bin_speed_new(self):
    #     Binomial(55)
    @validationTest
    def test_bins(self):
        gbin = Binomial(8)
        ans = np.array([
            [1, 0, 0,  0,  0,  0,  0, 0],
            [1, 1, 0,  0,  0,  0,  0, 0],
            [1, 2, 1,  0,  0,  0,  0, 0],
            [1, 3, 3,  1,  0,  0,  0, 0],
            [1, 4, 6,  4,  1,  0,  0, 0],
            [1, 5, 10, 10, 5,  1,  0, 0],
            [1, 6, 15, 20, 15, 6,  1, 0],
            [1, 7, 21, 35, 35, 21, 7, 1]
        ])
        # print(gbin, file=sys.stderr)
        self.assertAlmostEqual(np.sum(gbin-ans), 0.)
    @validationTest
    def test_facs(self):
        facs = Factorial(8)
        ans = np.array([1, 1, 2, 6, 24, 120, 720, 5040])
        # print(facs, file=sys.stderr)
        self.assertAlmostEqual(np.linalg.norm(facs-ans), 0.)
    @validationTest
    def test_fd_weights(self):
        coeffs = FiniteDifferenceFunction._even_grid_coeffs(3, 7/2, 7)
        ans = [ -0.0192708, 0.259896, -2.02969, 4.92448, -4.92448, 2.02969, -0.259896, 0.0192708 ]
        coeffs2 = FiniteDifferenceFunction._even_grid_coeffs(3, 0, 7)
        ans2 = [
            -8.058333333333334, 42.53333333333333, -98.225,
            129.66666666666666, -106.04166666666667, 53.6,
            -15.408333333333333, 1.9333333333333333
        ]
        # print(coeffs2, file=sys.stderr)
        r1 = np.round(np.linalg.norm(coeffs-ans), 5)
        r2 = np.round(np.linalg.norm(coeffs2-ans2), 10)
        self.assertAlmostEqual(r1 + r2, 0.)
    @validationTest
    def test_uneven_weights(self):
        import numpy as np
        weights = FiniteDifferenceFunction._uneven_spaced_weights
        uweights =  [
            weights(2, 0, np.array([-2, -1, 0, 1, 2])),
            weights(1, 0, np.array([-3/2, -1/2, 1/2, 3/2])),
            weights(1, 1, np.array([-3, -2, -1, 0, 1]))
            #weights(3, 1/2, np.array([0, 1/3, 1, 2, 7/2, 6]))
            ]
        eweights = FiniteDifferenceFunction._even_grid_coeffs
        targ_weights = [
            eweights(2, 2,   4),
            eweights(1, 3/2, 3),
            eweights(1, 4,   4)
            #[13/10, -5832/1105, 42/5, -177/20, 288/65, -1/1340] # turns out these are wrong...I tested my weights
            # in Mathematica and they actually work great
        ]
        passed = True
        for e, w in zip(targ_weights, uweights):
            norm = np.linalg.norm(e-w[-1])
            if norm > .000001:
                passed = False
                for x in (norm, e, w[-1]):
                    print(x, file=sys.stderr)
        self.assertIs(passed, True)

    @validationTest
    def test_FDDeriv(self):
        ggrid = GraphicsGrid(nrows=1, ncols=2)

        fdf = FiniteDifferenceDerivative(np.sin, stencil = 3)
        grid = np.linspace(0, 2*np.pi, 50)
        diff_fun = fdf.derivatives(grid)
        Plot(grid, diff_fun.array, figure=ggrid[0, 0])

        # a, b = diff_fun.stencil_shapes[0]
        # g2 = .01 * np.arange(-(a-1), b+1)
        # gg = np.meshgrid(g2, grid)
        # DensityPlot(*gg, diff_fun.compute_derivatives(pull_center = False), figure=ggrid[0, 1])

        # ggrid.show()

    @validationTest
    def test_FDDeriv2(self):
        def test(gps):
            x = gps[..., 0]
            y = gps[..., 1]

            return x * np.sin(y)

        fdf = FiniteDifferenceDerivative(test, order=2, function_shape=((2, ), 1), stencil = 5)
        npts = 25
        grid = np.linspace(0, 2*np.pi, npts)
        grid2D = np.meshgrid(grid, grid)
        gps = np.array(grid2D).T
        diff_fun = fdf.derivatives(gps)

        self.assertEquals(diff_fun[0, 0].shape, (npts, npts, 1, 1))

        # gg =  GraphicsGrid(nrows=2, ncols=4, graphics_class=Graphics3D, fig_kw={'figsize':(15, 8)})

        # for i in range(2):
        #     for j in range(2):
        #         Plot3D(
        #             *grid2D,
        #             np.round(diff_fun[i, j].reshape(npts, npts), 5),
        #             plot_style={
        #                 "cmap" : "viridis"
        #             },
        #             axes_labels = ['x', 'y', 'z'],
        #             figure= gg[i, j]
        #         )
        #         num_x = (1 if i == 0 else 0) + (1 if j == 0 else 0) # can be done with mod but too tired to thing
        #         num_y = (0 if i == 0 else 1) + (0 if j == 0 else 1) # can be done with mod but too tired to thing
        #         Plot3D(
        #             *grid2D,
        #             #test(gps),
        #             np.round(finite_difference(gps, test(gps), (num_x, num_y), (5, 5)), 5),
        #             plot_style={
        #                 "cmap" : "viridis"
        #             },
        #             axes_labels = ['x', 'y', 'z'],
        #             figure=gg[i, 2+j]
        #         )
        # gg.show()

    @validationTest
    def test_FDDeriv22(self):
        def test(gps):
            x = gps[..., 0]
            y = gps[..., 1]

            zpairs = np.array([np.cos(x)*np.cos(y), np.sin(x)*np.sin(y)]).transpose(1, 2, 0)
            return zpairs

        fdf = FiniteDifferenceDerivative(test, order=2, function_shape=((2, ), (2, )), stencil = 5)
        npts = 25
        grid = np.linspace(0, 2*np.pi, npts)
        grid2D = np.meshgrid(grid, grid)
        gps = np.array(grid2D).T
        diff_fun = fdf.derivatives(gps)

        self.assertEquals(diff_fun[0].shape, (npts, npts, 1, 2, 2))
        self.assertEquals(diff_fun[0, 0].shape, (npts, npts, 1, 1, 2))
        self.assertEquals(diff_fun[0, 0, 1].shape, (npts, npts, 1, ))

        # gg = GraphicsGrid(nrows=1, ncols=2, graphics_class=Graphics3D, fig_kw={'figsize':(15, 8)})
        # for i in range(2):
        #     Plot3D(
        #         *grid2D,
        #         np.round(diff_fun[0, 1, i].reshape(npts, npts), 5),
        #         plot_style={
        #             "cmap" : "viridis"
        #         },
        #         axes_labels = ['x', 'y', 'z'],
        #         figure=gg[0, i]
        #     )
        #
        # gg.show()
