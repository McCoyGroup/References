## <a id="Psience.Molecools.Molecule.Molecule">Molecule</a>
General purpose 'Molecule' class where the 'Molecule' need not be a molecule at all

### Properties and Methods
```python
from_zmat: method
from_pybel: method
from_file: method
```
<a id="Psience.Molecools.Molecule.Molecule.__init__" class="docs-object-method">&nbsp;</a>
```python
__init__(self, atoms, coords, bonds=None, obmol=None, charge=None, name=None, zmatrix=None, dipole_surface=None, potential_surface=None, potential_derivatives=None, source_file=None, guess_bonds=True, **kw): 
```

- `atoms`: `Iterable[str]`
    >atoms specified by name, either full name or short
- `coords`: `np.ndarray`
    >coordinates for the molecule, assumed to be in Bohr by default
- `bonds`: `Iterable[Iterable[int]] | None`
    >bond specification for the molecule
- `obmol`: `Any`
    >OpenBabel molecule for doing conversions
- `charge`: `int | None`
    >Net charge on the molecule
- `name`: `str | None`
    >Name for the molecule
- `dipole_surface`: `DipoleSurface | None`
    >The dipole surface for the system
- `potential_surface`: `PotentialSurface | None`
    >The potential surface for the system
- `potential_derivatives`: `Iterable[np.ndarray] | None`
    >Derivatives of the potential surface
- `guess_bonds`: `bool`
    >Whether or not to guess the bonding arrangement when that would be used
- `source_file`: `str`
    >The data file the molecule was loaded from
- `kw`: `Any`
    >Other bound parameters that might be useful

<a id="Psience.Molecools.Molecule.Molecule.__repr__" class="docs-object-method">&nbsp;</a>
```python
__repr__(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.num_atoms" class="docs-object-method">&nbsp;</a>
```python
@property
num_atoms(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.atoms" class="docs-object-method">&nbsp;</a>
```python
@property
atoms(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.masses" class="docs-object-method">&nbsp;</a>
```python
@property
masses(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.bonds" class="docs-object-method">&nbsp;</a>
```python
@property
bonds(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.coords" class="docs-object-method">&nbsp;</a>
```python
@property
coords(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.sys" class="docs-object-method">&nbsp;</a>
```python
@property
sys(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.formula" class="docs-object-method">&nbsp;</a>
```python
@property
formula(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.multiconfig" class="docs-object-method">&nbsp;</a>
```python
@property
multiconfig(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.name" class="docs-object-method">&nbsp;</a>
```python
@property
name(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.force_constants" class="docs-object-method">&nbsp;</a>
```python
@property
force_constants(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.potential_derivatives" class="docs-object-method">&nbsp;</a>
```python
@property
potential_derivatives(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.potential_surface" class="docs-object-method">&nbsp;</a>
```python
@property
potential_surface(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.dipole_surface" class="docs-object-method">&nbsp;</a>
```python
@property
dipole_surface(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.center_of_mass" class="docs-object-method">&nbsp;</a>
```python
@property
center_of_mass(self): 
```

- `:returns`: `CoordinateSet`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.inertial_axes" class="docs-object-method">&nbsp;</a>
```python
@property
inertial_axes(self): 
```

- `:returns`: `CoordinateSet`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.internal_coordinates" class="docs-object-method">&nbsp;</a>
```python
@property
internal_coordinates(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.normal_modes" class="docs-object-method">&nbsp;</a>
```python
@property
normal_modes(self): 
```

- `:returns`: `VibrationalModes`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.take_submolecule" class="docs-object-method">&nbsp;</a>
```python
take_submolecule(self, spec): 
```
Takes a 'slice' of a molecule if working with Cartesian coords.
        If not, need to do some corner case handling for that.
- `spec`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.shape" class="docs-object-method">&nbsp;</a>
```python
@property
shape(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.__len__" class="docs-object-method">&nbsp;</a>
```python
__len__(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.__iter__" class="docs-object-method">&nbsp;</a>
```python
__iter__(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.__getitem__" class="docs-object-method">&nbsp;</a>
```python
__getitem__(self, item): 
```

<a id="Psience.Molecools.Molecule.Molecule.copy" class="docs-object-method">&nbsp;</a>
```python
copy(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.prop" class="docs-object-method">&nbsp;</a>
```python
prop(self, name, *args, **kwargs): 
```

<a id="Psience.Molecools.Molecule.Molecule.load_force_constants" class="docs-object-method">&nbsp;</a>
```python
load_force_constants(self, file=None): 
```
Loads force constants from a file (or from `source_file` if set)
- `file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.load_potential_derivatives" class="docs-object-method">&nbsp;</a>
```python
load_potential_derivatives(self, file=None): 
```
Loads potential derivatives from a file (or from `source_file` if set)
- `file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.load_normal_modes" class="docs-object-method">&nbsp;</a>
```python
load_normal_modes(self, file=None): 
```
Loads potential derivatives from a file (or from `source_file` if set)
- `file`: `Any`
    >No description...
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.load_potential_surface" class="docs-object-method">&nbsp;</a>
```python
load_potential_surface(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.load_dipole_surface" class="docs-object-method">&nbsp;</a>
```python
load_dipole_surface(self): 
```

<a id="Psience.Molecools.Molecule.Molecule.principle_axis_frame" class="docs-object-method">&nbsp;</a>
```python
principle_axis_frame(self, sel=None, inverse=False): 
```
Gets the principle axis frame(s) for the molecule
- `mol`: `Any`
    >No description...
- `sel`: `Any`
    >selection of atoms to use when getting the Eckart frame
- `inverse`: `bool`
    >whether to return the inverse of the rotations or not
- `:returns`: `MolecularTransformation | List[MolecularTransformation]`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.eckart_frame" class="docs-object-method">&nbsp;</a>
```python
eckart_frame(self, mol, sel=None, inverse=False): 
```
Gets the Eckart frame(s) for the molecule
- `mol`: `Any`
    >No description...
- `sel`: `Any`
    >selection of atoms to use when getting the Eckart frame
- `inverse`: `bool`
    >whether to return the inverse of the rotations or not
- `:returns`: `_`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.get_embedded_molecule" class="docs-object-method">&nbsp;</a>
```python
get_embedded_molecule(self, ref=None): 
```
Returns a Molecule embedded in an Eckart frame if ref is not None, otherwise returns
        a principle-axis embedded Molecule
- `:returns`: `Molecule`
    >No description...

<a id="Psience.Molecools.Molecule.Molecule.plot" class="docs-object-method">&nbsp;</a>
```python
plot(self, *geometries, figure=None, bond_radius=0.1, atom_radius_scaling=0.25, atom_style=None, bond_style=None, mode='fast', objects=False, **plot_ops): 
```

<a id="Psience.Molecools.Molecule.Molecule.get_normal_modes" class="docs-object-method">&nbsp;</a>
```python
get_normal_modes(self, **kwargs): 
```

### Examples
We're working on getting actual examples in place, here. For now, here are the unit tests we use, which will help give some flavor of what's possible

```python
test_log_water = TestManager.test_data("water_OH_scan.log")
test_log_freq = TestManager.test_data("water_freq.log")
test_HOD = TestManager.test_data("HOD_freq.fchk")
test_fchk = TestManager.test_data("water_freq.fchk")
test_log_h2 = TestManager.test_data("outer_H2_scan_new.log")

def test_ImportMolecule(self):

    n = 3 # water
    m = Molecule.from_file(self.test_fchk)
    self.assertEquals(m.atoms, ("O", "H", "H"))

def test_Eckart(self):
    scan_file = TestManager.test_data("tbhp_030.log")
    ref_file = TestManager.test_data("tbhp_180.fchk")

    scan = Molecule.from_file(scan_file)
    ref = Molecule.from_file(ref_file)
    sel = np.where(ref.masses > 3)[0]

    pax_rot = ref.principle_axis_frame(sel=sel) #type: MolecularTransformation
    rot_ref = pax_rot.apply(ref)

    #transf = scan.principle_axis_frame(sel=sel)
    transf = scan.eckart_frame(ref, sel=sel)
    tf_test = transf[0].transformation_function

    tf_mat = tf_test.transform
    self.assertTrue(np.allclose(tf_mat@tf_mat.T - np.eye(3), 0.))
    self.assertEquals(tf_test.transf.shape, (4, 4))

    for t, m in zip(transf, scan):
        new_mol = t(m)
        # rot_ref.guess_bonds = False
        # ref.guess_bonds = False
        # m.guess_bonds = False
        # new_mol.guess_bonds = False
        # m = m #type: Molecule
        # g1, a, b = ref.plot()
        # # ref.plot(figure=g1)
        # rot_ref.plot(figure=g1)
        # g, a, b = new_mol.plot()
        # rot_ref.plot(figure=g, atom_style=dict(color='black'))
        # g.show()
        fuckup = np.linalg.norm(new_mol.coords[sel] - rot_ref.coords[sel])
        self.assertLess(fuckup/len(sel), .1)

def test_EckartEmbedDipoles(self):
    scan_file = TestManager.test_data("tbhp_030.log")
    ref_file = TestManager.test_data("tbhp_180.fchk")

    scan = Molecule.from_file(scan_file)
    ref = Molecule.from_file(ref_file)
    sel = np.where(ref.masses>3)[0]
    pax_rot = ref.principle_axis_frame(sel=sel, inverse=True)  # type: MolecularTransformation
    rot_ref = pax_rot.apply(ref)

    transf = scan.eckart_frame(rot_ref, sel=sel)

    carts, dips = DipoleSurface.get_log_values(scan_file, keys=("StandardCartesianCoordinates", "OptimizedDipoleMoments"))
    rot_dips = np.array([ np.dot(t.transformation_function.transform, d) for t,d in zip(transf, dips) ])
    self.assertTrue(np.allclose(np.linalg.norm(dips, axis=1)-np.linalg.norm(rot_dips, axis=1), 0.))

    ### Visualize dipole surface
    dists = np.linalg.norm(carts[1:, 5] - carts[1:, 6], axis=1)
    Graphics.default_style['image_size'] = 575
    g = GraphicsGrid(nrows=1, ncols=2, padding=((.075, 0), (0, .45)))
    p = Plot(dists, rot_dips[:, 0], figure=g[0, 0])
    Plot(dists, rot_dips[:, 1], figure=p)
    Plot(dists, rot_dips[:, 2], figure=p)
    p2= Plot(dists, dips[:, 0], figure=g[0, 1])
    Plot(dists, dips[:, 1], figure=p2)
    Plot(dists, dips[:, 2], figure=p2)
    g.show()

def test_NormalModes(self):
    n = 3 # water
    with GaussianFChkReader(self.test_fchk) as reader:
        parse = reader.parse(("ForceConstants", "AtomicMasses"))
    fcs = parse["ForceConstants"].array
    masses = parse["AtomicMasses"]

    nms = MolecularNormalModes.from_force_constants(fcs, masses)
    # ArrayPlot(nms.matrix).show()
    self.assertEquals(nms.matrix.shape, (3*n, 3*n))
    
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

def test_BondGuessing(self):
    m = Molecule.from_file(self.test_fchk)
    self.assertEquals(m.bonds, [[0, 1, 1], [0, 2, 1]])

def test_Frags(self):
    m = Molecule.from_file(self.test_fchk)
    self.assertEquals(len(m.prop("fragments")), 1)

def test_HODModes(self):
    # oops fucked up getting D out
    m = Molecule.from_file(self.test_HOD, bonds=[[0, 1, 1], [0, 2, 1]])
    modes = m.normal_modes
    self.assertEquals(m.atoms, ("O", "H", "D"))
    self.assertEquals(tuple(np.round(modes.freqs)), (1422.0, 2810.0, 3874.0))

def test_H2OModes(self):
    m = Molecule.from_file(self.test_fchk, bonds=[[0, 1, 1], [0, 2, 1]])
    modes = m.normal_modes
    self.assertEquals(m.atoms, ("O", "H", "H"))
    self.assertEquals(tuple(np.round(modes.freqs)), (1622.0, 3803.0, 3938.0))

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

def test_VisualizeNormalModes(self):

    from Psience.Molecools.Vibrations import MolecularVibrations, MolecularNormalModes
    from McUtils.Plots import GraphicsGrid, Graphics3D

    m = Molecule.from_file(self.test_fchk, bonds = [[0, 1, 1], [0, 2, 1]])

    with GaussianFChkReader(self.test_fchk) as reader:
        parse = reader.parse(("VibrationalModes", "VibrationalData"))
    modes = parse["VibrationalModes"].T

    test_freqs = parse["VibrationalData"]["Frequencies"]

    nms = m.normal_modes
    realvibs = MolecularVibrations(m, basis=MolecularNormalModes(modes, freqs=test_freqs))

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
```


___

[Edit Examples](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/examples/Psience/Molecools/Molecule/Molecule.md) or 
[Create New Examples](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/examples/Psience/Molecools/Molecule/Molecule.md) <br/>
[Edit Template](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/templates/Psience/Molecools/Molecule/Molecule.md) or 
[Create New Template](https://github.com/McCoyGroup/References/new/gh-pages/?filename=Documentation/templates/Psience/Molecools/Molecule/Molecule.md) <br/>
[Edit Docstrings](https://github.com/McCoyGroup/Psience/edit/master/Molecools/Molecule.py?message=Update%20Docs)