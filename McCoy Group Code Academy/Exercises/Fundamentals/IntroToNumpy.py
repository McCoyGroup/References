import numpy as np
"""
Goal: This fundamental should get you acquanited with numpy functions and their bad, pythonic equivarange(lents
"""

## Imports: put all import statments here

import numpy as np

## Exports: put all the names things we might want to use in other scripts here

__all__ = ["elementwise_multiply","bond_length"]

## Functions: put all the functions we're defining here
def _py_multiply_2d(ar1,ar2):
    """
    :param ar1: a 2D numpy array
    :type ar1: np.ndarray
    :param ar2: a 2D numpy array
    :type ar2: np.ndarray
    :return: the values of the elementwise multiplication of two numpy arrays
    :rtype: np.array
    This is bad: it is hard coded to take in a 2D array
    """
    shape_of_ars = ar1.shape
    res = np.zeros(shape_of_ars)
    for i in range(shape_of_ars[0]):
        for j in range(shape_of_ars[1]):
            res[i,j] = ar1[i,j]*ar2[i,j]
    return res

def elementwise_multiply(ar1,ar2):
    """
    :param ar1: a 3D numpy array
    :type ar1: np.ndarray
    :param ar2: a 3D numpy array
    :type ar2: np.ndarray
    :return: the values of the elementwise multiplication of two numpy arrays
    :rtype: np.array
    This is bad: it is hard coded to take in a 3D array
    """
    #hint, look at elementwise addition in NumPy101:
    # https://mccoygroup.github.io/References/McCoy%20Group%20Code%20Academy/NumPy/numpy101.html
    #this can be done in one line.
    ...
    return mult_result

def _py_bond_length(cds,atom1,atom2):
    """
    :param cds: a 3D numpy array (num geoms, num atoms, (x,y,z))
    :type cds: np.ndarray
    :param atom1: an array index to specify 1 of 2 atoms we want to take the bond length of
    :type atom1: int
    :param atom2: an array index to specify 1 of 2 atoms we want to take the bond length of
    :type atom2: int
    :return: the values of the elementwise multiplication of two numpy arrays
        :rtype: np.array
    This calculates, for every geometry you give it, the bond length between two user-specified atoms
    """
    b_lengths = [] #empty list
    for geom in cds:
        vector = geom[atom1]-geom[atom2] #vector subtraction of 1x3 numpy arrays
        # b_length = np.sqrt(vector[0]**2+vector[1]**2+vector[2]**2) #take norm of vector *the hard way*
        b_length = np.linalg.norm(vector)  # take norm of vector *the easier way*, but still with looping
        b_lengths.append(b_length)
    return np.array(b_lengths) #change list to numpy array

def bond_length(cds,atom1,atom2):
    """
    :param cds: a 3D numpy array (num geoms, num atoms, (x,y,z))
    :type cds: np.ndarray
    :param atom1: an array index to specify 1 of 2 atoms we want to take the bond length of
    :type atom1: int
    :param atom2: an array index to specify 1 of 2 atoms we want to take the bond length of
    :type atom2: int
    :return: the values of the elementwise multiplication of two numpy arrays
    :rtype: np.array
    This calculates, for every geometry you give it, the bond length between two user-specified atoms
    Remember, no looping!!!!
    """
    # HINT: check out np.linalg.norm and its *axis* argument.
    ...
    return b_lengths


def get_els_gt5(ar):
    """
    :param cds: any size numpy array
    :type cds: np.ndarray
    :return: the values of the the array that are greater than 5
    :rtype: np.array
    """
    #there are a number of ways to do this without looping. Check out
    # https://www.w3resource.com/python-exercises/numpy/python-numpy-exercise-88.php
    #In addition to that, there is np.where, and np.argwhere, and "masking" numpy arrays
    ...
    return els

def _py_get_els_gt5(ar):
    """
    :param cds: any size numpy array
    :type cds: np.ndarray
    :return: the values of the the array that are greater than 5
    :rtype: np.array
    """
    res = []
    for element in np.nditer(ar): #np.nditer iterates over everything, regardless of number of dimensions
        if element > 5:
            res.append(element)
    return np.array(res)


## Run Script: put the script we'd want to run from the command line here
if __name__ == '__main__':
    #elementwise multiplication
    ar_1 = np.arange(12.).reshape((4,3)) #elements are 0 through 11 in a 4x3 matrix
    ar_2 = np.arange(12.,24.).reshape((4,3)) #elements are 12 through 23 in a 4x3 matrix
    mult_res_py = _py_multiply_3d(ar_1,ar_2)
    mult_res_np = elementwise_multiply(ar_1,ar_2)
    print(np.allclose(mult_res_np, mult_res_py)) #check if you implemented elementwise mult correctly.

    #working with molecules - bond lengths
    #water_geoms is a 3x3x3 (num geoms, num atoms (H,H,O), xyz)
    water_geoms = np.array([[[-2.2375041486157063, -0.1055383624257177, -0.5805514872124862],
                    [-0.7524792640063526, 2.3880785488604990, -0.5639483476990418],
                    [-0.2872036826767270, 0.5368534590941352, -0.7002290803849639]],

                   [[0.7694397177456009, -0.3163963935277288, -0.2034847599462577],
                    [-1.7680382475165304, -0.3767332695439299, 0.3376713628636553],
                    [-0.1510990203100878, 1.1213845147348493, 0.1724396027306939]],

                   [[-0.2720218013417344, -0.1774024745677997, -1.8170261242618779],
                    [-1.8352695108992323, 0.8657015181759908, 0.1522649792829701],
                    [-0.1938843229465466, 0.7628330645015524, -0.1562759876940720]]])

    #These functions take in two indices that correspond to atom numbers (H and O for 0 and 2)
    bond_length_py = _py_bond_length(water_geoms,atom1=0,atom2=2)
    bond_length_np = bond_length(water_geoms,atom1=0,atom2=2)
    print(np.allclose(bond_length_np,bond_length_py)) #check if you implemented bond_length_np correctly

    #Getting subsections of arrays, like return all elements greater than 5
    x = np.arange(10).reshape(5,2) # a 5x2 matrix with elements 0 through 9
    g5_np = get_els_gt5(x)
    g5_py = _py_get_els_gt5(x)
    print(np.allclose(g5_np,g5_py))  # check if you implemented correctly
