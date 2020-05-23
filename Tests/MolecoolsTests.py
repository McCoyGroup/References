
from Peeves.TestUtils import *
from unittest import TestCase
from Psience.Molecools import Molecule, NormalModeCoordinates
from McUtils.GaussianInterface import GaussianFChkReader
from McUtils.Plots import *
from McUtils.Data import UnitsData
import numpy as np

class MolecoolsTests(TestCase):

    test_log_water = TestManager.test_data("water_OH_scan.log")
    test_log_freq = TestManager.test_data("water_freq.log")
    test_HOD = TestManager.test_data("HOD_freq.fchk")
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

        nms = NormalModeCoordinates.from_force_constants(fcs, masses)
        # ArrayPlot(nms.matrix).show()
        self.assertEquals(nms.matrix.shape, (3*n, 3*n))

    @validationTest
    def test_Plotting(self):

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
        # g.show()

    @validationTest
    def test_BondGuessing(self):
        m = Molecule.from_file(self.test_fchk)
        self.assertEquals(m.bonds, [[0, 1, 1], [0, 2, 1]])

    @debugTest
    def test_Frags(self):
        m = Molecule.from_file(self.test_fchk)
        self.assertEquals(len(m.prop("fragments")), 1)

    @debugTest
    def test_AutoZMat(self):
        m = Molecule.from_file(self.test_fchk)

    @validationTest
    def test_HODModes(self):
        # oops fucked up getting D out
        m = Molecule.from_file(self.test_HOD, bonds=[[0, 1, 1], [0, 2, 1]])
        modes = m.normal_modes
        self.assertEquals(m.atoms, ("O", "H", "D"))
        self.assertEquals(tuple(np.round(modes.freqs)), (1422.0, 2810.0, 3874.0))


    @validationTest
    def test_H2OModes(self):
        m = Molecule.from_file(self.test_fchk, bonds=[[0, 1, 1], [0, 2, 1]])
        modes = m.normal_modes
        self.assertEquals(m.atoms, ("O", "H", "H"))
        self.assertEquals(tuple(np.round(modes.freqs)), (1622.0, 3803.0, 3938.0))

    @inactiveTest
    def test_RenormalizeGaussianModes(self):


        with GaussianFChkReader(self.test_HOD) as gr:
            parse = gr.parse(["Coordinates", "Gradient", "AtomicMasses",
                              "ForceConstants", "ForceDerivatives", "VibrationalModes", "VibrationalData"])

        coords = UnitsData.convert("Angstroms", "AtomicUnitOfLength") * parse["Coordinates"]
        masses = UnitsData.convert("AtomicMassUnits", "AtomicUnitOfMass") * parse["AtomicMasses"]
        modes = parse["VibrationalModes"].T
        freqs = parse["VibrationalData"]["Frequencies"]
        fcs = parse["ForceConstants"].array
        sad = UnitsData.convert("Hartrees", "Wavenumbers") * np.sqrt(np.diag(np.dot(np.dot(modes.T, fcs), modes)))
        modes = modes * freqs/sad
        print( UnitsData.convert("Hartrees", "Wavenumbers") * np.sqrt(np.diag(np.dot(np.dot(modes.T, fcs), modes))))

        masses = np.broadcast_to(masses, (len(masses), 3)).T.flatten()
        # print(modes-np.linalg.pinv(modes).T)
        print(np.dot(np.dot(modes.T, np.diag(masses)), modes))

        modes_2 = Molecule.from_file(self.test_HOD).get_normal_modes(normalize=False)
        mm = modes_2._basis.matrix

        print(np.dot(np.dot(mm.T, np.diag(masses)), mm))
        print(UnitsData.convert("Hartrees", "Wavenumbers") * np.sqrt(np.diag(np.dot(np.dot(mm.T, fcs), mm))))
        # print(modes._basis.matrix.T.dot(m.force_constants).shape)

    @validationTest
    def test_VisualizeNormalModes(self):

        from Psience.Molecools.Vibrations import VibrationalModes, NormalModeCoordinates
        from McUtils.Plots import GraphicsGrid, Graphics3D

        m = Molecule.from_file(self.test_fchk, bonds = [[0, 1, 1], [0, 2, 1]])

        with GaussianFChkReader(self.test_fchk) as reader:
            parse = reader.parse(("VibrationalModes", "VibrationalData"))
        modes = parse["VibrationalModes"].T

        test_freqs = parse["VibrationalData"]["Frequencies"]

        nms = m.normal_modes
        realvibs = VibrationalModes(m, basis=NormalModeCoordinates(modes, freqs=test_freqs))

        plot_vibrations = False
        if plot_vibrations:
            nmodes = 1
            mode_start = 0
            g = GraphicsGrid(nrows=2, ncols=nmodes,
                             graphics_class=Graphics3D,
                             plot_range = [[-2, 2], [-2, 2], [-2, 2]],
                             fig_kw = dict(figsize = (17, 5)),
                             tighten = True
                             )

            for i in range(nmodes):
                nms.visualize(step_size=.1, figure = g[0, i], which=mode_start + i,
                              anim_opts= dict(interval = 10)
                              )

            for i in range(nmodes):
                realvibs.visualize(step_size=.1, figure = g[1, i], which= mode_start+i,
                                   anim_opts= dict(interval = 10)
                                   )

            g.show()

        self.assertEquals(tuple(round(a, 4) for a in nms.freqs), tuple(round(a, 4) for a in test_freqs))
