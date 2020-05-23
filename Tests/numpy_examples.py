"""
These are some simple little examples to show you how to use NumPy effectively
"""

import numpy as np, time, math, scipy.sparse as sp

################################################################################################################################
#
#                                               Utilities
#
# ignore these
class Timer:
    """
    A simple timer to test our methods.
    We'll use it like
    ```
        with Timer(testName):
            testCode
    ```
    And it'll print out how long our test took after testCode is done
    """

    def __init__(self, name):
        self.name = name
        self._start = None
        self._end = None
    def print_time(self, elapsed):
        if elapsed > 60:
            elapsed_mins = np.floor(elapsed / 60)
            elapsed_seconds = elapsed % 60
            elapsed_seconds_int = int(elapsed_seconds)
            elapsed_milli = elapsed_seconds-elapsed_seconds_int
            elapsed_str = "{:0>2}:{:0>2}.{}".format(elapsed_mins, elapsed_seconds_int, elapsed_milli)
        else:
            elapsed_str = "{}s".format(elapsed)
        print("Test {} took {}".format(self.name, elapsed_str))
    def __enter__(self):
        self._start = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = time.time()
        self.print_time(self._end - self._start)

def python_arange(min, max, step):
    span = max - min
    steps = span / step
    return [min + step * i for i in range(int(steps))]

def python_tile(grid, n):
    return [ list(grid) for i in range(n) ]

def python_mesh(grid_1, grid_2):
    g1 = [ list(grid_1) for i in range(len(grid_2)) ]
    g2 = [ [grid_2[i] for j in range(len(grid_1))] for i in range(len(grid_2))]
    return (g1, g2)

def format_python_array(array, n=0):
    if isinstance(array[0], list):
        rep="[\n" + "\n".join([format_python_array(a, n+1) for a in array]) + "\n]"
    else:
        rep = str(array)
    return (" "*n)+rep

block_delim = "\n" + "-"*50 + "\n"

################################################################################################################################
#
#                                               Examples
#
def test_looping():
    print("test_looping:")
    grid_python = python_arange(-10, 10, .01)
    grid_numpy = np.arange(-10, 10, .01)
    print("len(x) = {}".format(len(grid_python)))
    with Timer("Python"):
        loopy_python = [ x**2 for x in grid_python ]
    with Timer("NumPy"):
        loopy_numpy = grid_numpy**2
    print("sum python: {}".format(sum(loopy_python)))
    print("sum numpy: {}".format(sum(loopy_numpy)), end=block_delim)

def test_slicing():
    print("test_slicing:")
    grid_1D = python_arange(-1, 1, .1)
    grid_2D_python = python_tile(grid_1D, 10)
    grid_2D_numpy = np.tile(grid_1D, (10, 1))
    print("grid_dimensions = ({}, {})".format(len(grid_2D_python), len(grid_1D)))
    with Timer("Python"):
        slice_p = [ g[3:7] for g in grid_2D_python[2:5] ]
    with Timer("NumPy"):
        slice_n = grid_2D_numpy[2:5, 3:7]
    print("slice python:\n{}".format(format_python_array(slice_p)))
    print("slice numpy:\n{}".format(slice_n), end=block_delim)

def test_filling():
    print("test_filling:")
    grid_1D = python_arange(-1, 1, .5)
    grid_2D_python = python_tile(grid_1D, 5)
    grid_2D_numpy = np.tile(grid_1D, (5, 1))
    with Timer("Python"):
        for g in grid_2D_python[2:5]:
            g[1:3] = [0]*(3-1)
    with Timer("NumPy"):
        grid_2D_numpy[2:5, 1:3] = 0
    print("grid python:\n{}".format(format_python_array(grid_2D_python)))
    print("grid numpy:\n{}".format(grid_2D_numpy), end=block_delim)

def test_mesh():
    print("test_mesh:")
    grid_1 = python_arange(-1, 1, .01)
    grid_2 = python_arange(-2, 0, .01)
    with Timer("Python"):
        mesh_p = python_mesh(grid_1, grid_2)
    with Timer("NumPy"):
        mesh_n = np.meshgrid(grid_1, grid_2)
    print("shape python:\n{}x{}".format(len(mesh_p[0]), len(mesh_p[0][1])))
    print("shape numpy:\n{}x{}".format(*mesh_n[0].shape), end=block_delim)

def test_find_element():
    print("test_find_element:")
    grid_python = python_arange(-10, 10, .01)
    grid_numpy = np.arange(-10, 10, .01)
    print("finding where x < 5")
    with Timer("Python"):
        i = 0
        for i in range(len(grid_python)):
            if grid_python[i] >=5:
                break
        pos_p = range(i)
    with Timer("NumPy"):
        pos_n = np.argwhere(grid_numpy < 5)
    print("range python:\n{}".format(len(pos_p)))
    print("range numpy:\n{}".format(len(pos_n)), end=block_delim)

def test_generate_random_dist():
    print("test_generate_random_dist:")
    print("No Python Implementation")
    mean = 1; stddev = .5; n = 10000;
    print("mean = {} stddev = {} | {} numbers generated".format(mean, stddev, n))
    with Timer("NumPy"):
        nums = np.random.normal(loc=mean, scale=stddev, size=(n,))
    print("mean: {}, stddev: {}".format(np.average(nums), np.std(nums)), end=block_delim)

def test_generate_rotation_matrices():
    print("test_generate_rotation_matrices:")
    print("No Python Implementation")
    print("""Rotation is about Z-axis:
    [[ cos(q) -sin(q) 0]
     [ sin(q)  cos(q) 0]
     [     0       0  1]]""")
    mean = np.pi; stddev = .5; n = 10000
    with Timer("NumPy"):
        nums = np.random.normal(loc=mean, scale=stddev, size=(n,))
        rots = np.zeros((n, 3, 3))
        sins = np.sin(nums)
        coss = np.cos(nums)
        rots[:, 0, 0] = coss; rots[:, 0, 1] = -sins
        rots[:, 1, 0] = sins; rots[:, 1, 1] = coss
        rots[:, 2, 2] = 1
    print("single rotation:\n{}".format(rots[0]), end=block_delim)

def test_rotate_vector():
    print("test_rotate_vector:")
    print("No Python Implementation")
    vec_len = 1.5
    vec = np.array([0, vec_len, 0])
    angle = np.pi/3
    rot = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])
    with Timer("NumPy"):
        rot_vec = np.dot(rot, vec)
    print("rotated vector: {} rotated norm: {}".format(rot_vec, np.linalg.norm(rot_vec)), end=block_delim)

def test_finite_difference():
    print("test_finite_difference:")
    second_deriv_weights = [1, -2, 1]
    order = 2
    grid_python = python_arange(-10, 10, .001)
    grid_numpy = np.arange(-10, 10, .001)
    sin_vals_python = [math.sin(x) for x in grid_python]
    sin_vals_numpy = np.sin(grid_numpy)
    with Timer("Python"):
        npts = len(grid_python)
        h = grid_python[1] - grid_python[0]
        weights = np.array(second_deriv_weights) / (h ** order)
        vals_python = [ sum(a*b for a,b in zip(weights, sin_vals_python[i-1:i+2])) for i in range(1, npts-1) ]
    with Timer("NumPy"):
        npts = len(grid_numpy)
        h = grid_numpy[1] - grid_numpy[0]
        weights = np.array(second_deriv_weights) / (h**order)
        fdm = sp.diags(weights, offsets=[0, 1, 2], shape=(npts-2, npts))
        vals_numpy = fdm.dot(sin_vals_numpy)

    normed_error_python = sum((a+b)**2 for a,b in zip(sin_vals_python[1:-1], vals_python))
    normed_error_numpy = np.linalg.norm(sin_vals_numpy[1:-1] + vals_numpy)

    print("normed error python: {}\nnormed error numpy: {}".format(normed_error_python, normed_error_numpy), end=block_delim)


################################################################################################################################
#
#                                               Exercises
#
def exercise_2D_HO_In_A_Box():
    """
        Define a potential on a grid over the region {(x, y) in [ [-2, 2], [-5, 5] ]} that satisfies the following properties:
            It's defined as x**2 + y**2 on the region {(x, y) in [ [-1, 1], [-1, 1] ]} and 200 outside
        Don't do this in pure python at all. This is just a NumPy example.
    """
    raise NotImplemented



def exercise_bond_length_distribution():
    """
        Generate 5000 random structures for a water molecule with the following properties:
            The OH bond-lengths are normally distributed and centered about 1.0 with a standard deviation of .3
            The HOH angles are normally distributed and centered about 90 degrees with a standard deviation of 20
        Then calculate the mean and standard deviation of the HH distance distribution
        Don't do this in pure python at all. This is just a NumPy example.
    """

    raise NotImplemented

def exercise_2D_mixed_first_derivative():
    """
        Calculate the mixed first derivative of the function sin(x)*cos(y) via finite difference:
            This means taking the first derivative of the function in one coordinate and then
            feeding that into the second function to take its derivatives
        Don't do this in pure python at all. This is just a NumPy example.
    """
    first_deriv_weights = [1, -2, 1]

    raise NotImplemented



if __name__ == "__main__":
    test_examples = True
    if test_examples:
        test_looping()
        test_slicing()
        test_filling()
        test_mesh()
        test_find_element()
        test_generate_random_dist()
        test_generate_rotation_matrices()
        test_rotate_vector()
        test_finite_difference()
    test_exercises = False
    if test_exercises:
        exercise_2D_HO_In_A_Box()
        exercise_bond_length_distribution()
        exercise_2D_mixed_first_derivative()
