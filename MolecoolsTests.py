
from Peeves.TestUtils import *
from unittest import TestCase
from Psience.Molecools import Molecule, NormalModeCoordiantes
from McUtils.GaussianInterface import GaussianFChkReader
from McUtils.Plots import ArrayPlot

class MolecoolsTests(TestCase):

    test_log_water = TestManager.test_data("water_OH_scan.log")
    test_log_freq = TestManager.test_data("water_freq.log")
    test_fchk = TestManager.test_data("water_freq.fchk")
    test_log_h2 = TestManager.test_data("outer_H2_scan_new.log")

    @validationTest
    def test_ImportMolecule(self):

        n = 3 # water
        m = Molecule.from_file(self.test_fchk)
        self.assertEquals(m.atoms, ("O", "H", "H"))

    @validationTest
    def test_NormalModes(self):
        n = 3 # water
        with GaussianFChkReader(self.test_fchk) as reader:
            parse = reader.parse(("ForceConstants", "AtomicMasses"))
        fcs = parse["ForceConstants"].array
        masses = parse["AtomicMasses"]

        nms = NormalModeCoordiantes.from_force_constants(fcs, masses)
        # ArrayPlot(nms.matrix).show()
        self.assertEquals(nms.matrix.shape, (3*n, 3*n))

    @debugTest
    def test_Plotting(self):
        from McUtils.Plots import Graphics3D

        g = Graphics3D(
            image_size=[1500, 1500],
            plot_range=[[-10, 10]]*3,
            backend="VTK"
            )
        h5 = Molecule.from_file(
            self.test_log_h2,
            # self.test_fchk,
            # bonds = [
            #     [0, 1, 1],
            #     [0, 2, 1]
            # ]
        )
        h5.plot(
            figure=g
            # mode='3D',
            # bond_style= { "circle_points": 24 },
            # atom_style= { "sphere_points": 24 }
        )
        m = Molecule.from_file(
            self.test_fchk,
            bonds = [
                [0, 1, 1],
                [0, 2, 1]
            ]
        )
        m.plot(
            figure=g
            # mode='3D',
            # bond_style= { "circle_points": 24 },
            # atom_style= { "sphere_points": 24 }
            )
        g.show()

    @validationTest
    def test_VisualizeNormalModes(self):

        from Psience.Molecools.Vibrations import VibrationalModes, NormalModeCoordiantes
        from McUtils.Plots import GraphicsGrid, Graphics3D


        n = 3 # water
        m = Molecule.from_file(self.test_fchk,
                               bonds = [
                                   [0, 1, 1],
                                   [0, 2, 1]
                               ]
                               )

        with GaussianFChkReader(self.test_fchk) as reader:
            parse = reader.parse(("VibrationalModes", "VibrationalData"))
        modes = parse["VibrationalModes"]

        nms = m.normal_modes

        realvibs = VibrationalModes(m, basis=NormalModeCoordiantes(modes, freqs=parse["VibrationalData"]["Frequencies"]))

        nmodes = 1
        mode_start = -3
        g = GraphicsGrid(nrows=1, ncols=nmodes, graphics_class=Graphics3D,
                         plot_range = [[-2, 2], [-2, 2], [-2, 2]],
                         fig_kw = dict(figsize = (17, 5))
                         )
        # for i in range(nmodes):
        #     nms.visualize(step_size=.1, figure = g[0, i], which=mode_start + i,
        #                   anim_opts= dict(interval = 10)
        #                   )

        for i in range(nmodes):
            realvibs.visualize(step_size=2, figure = g[0, i], which= i,
                               anim_opts= dict(interval = 10)
                               )

        # g.show()
