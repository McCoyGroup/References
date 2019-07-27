from McUtils.GaussianInterface import GaussianJob
import os
from sys import exit

rMin =  .255831
rMax = 1.255831
rSteps = 15
rStepSize = (rMax - rMin) / rSteps

RMin = .460716
RMax = 3.460716
RSteps = 60
RStepSize = (RMax - RMin) / RSteps

steps_per_file = 1
steps_2_per_file = 30

for which_do in ("parallel", "perpendicular"):
    if which_do == "parallel":
        write_dir = os.path.expanduser("~/Documents/UW/Research/H5+/scans/" + which_do)
        mol_spec = [
            ["H", "X", "H", "H", "X", "X", "H", "H"],
            [
                [1, "d1"],
                [2, "R1", 1, 90.],
                [2, "d1", 3, 90., 1, 180.],
                [3, "xD", 2, 90., 1, 0.],
                [3, "R2", 5, 90., 2, 180.],
                [6, "d2", 3, 90., 5, 0.],
                [6, "d2", 3, 90., 5, 180.]
            ]
        ]
    elif which_do == "perpendicular":
        write_dir = os.path.expanduser("~/Documents/UW/Research/H5+/scans/" + which_do)
        mol_spec = [
            ["H", "X", "H", "H", "X", "X", "H", "H"],
            [
                [], # need this empty one up front...?
                [1, "d1"],
                [2, "R1", 1, 90.],
                [2, "d1", 3, 90., 1, 180.],
                [3, "xD", 2, 90., 1, 0.],
                [3, "R2", 5, 90., 2, 180.],
                [6, "d2", 3, 90., 5, 90.],
                [6, "d2", 3, 90., 5, -90.]
            ]
        ]
    else:
        raise Exception("whoops")



    for low in range(1, RSteps + (0 if steps_per_file > 1 else 1), steps_per_file):
        for low2 in range(1, RSteps, steps_2_per_file):

            stoop = steps_per_file - 1
            high = low + stoop

            stoop2 = steps_2_per_file -1
            high2 = low2 + stoop2
            name = "h5_{}_{}-{}_{}-{}_TZ".format(which_do, low, high, low2, high2)

            RStepMin = RMin + (low-1)*RStepSize
            RStepMin2 = RMin + (low2-1)*RStepSize
            gaussianSucksCutoff = gsc = 2.85

            sys = GaussianJob.System(
                charge=1,
                molecule=mol_spec,
                vars=[
                    GaussianJob.System.Variable("d1", rMin, rSteps - 1, rStepSize),
                    GaussianJob.System.Variable("d2", rMin, rSteps - 1, rStepSize),
                    GaussianJob.System.Variable("R1", RStepMin, stoop, RStepSize),
                    GaussianJob.System.Variable("R2", RStepMin2, stoop2, RStepSize),
                    GaussianJob.System.Constant("xD", 10)
                ]
            )

            GaussianJob(
                name,
                description="h5 {} points {} to {} and {} to {}".format(which_do, low, high, low2, high2),
                file=os.path.join(write_dir, name +".gjf"),
                config= GaussianJob.Config(
                    NProc = 28,
                    Mem = '100000MB',
                    Chk = None
                ),
                job= GaussianJob.Job(
                    'Scan',
                    basis_set="MP2/aug-cc-pvtz",
                    Density="Current",
                    NoSymm=True
                ),
                system = sys,
                template = "TemplateTerse.gjf"
            ).write()

exit(0)