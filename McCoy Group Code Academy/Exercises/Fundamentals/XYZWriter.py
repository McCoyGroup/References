"""
Goal: To read and write a *.xyz file type
Fundamentals: None specifically. 
Related Exercises: See https://stackoverflow.com/c/mccoygroup/questions/81 
"""

## Imports: put all import statments here
import numpy as np 

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
]

## Functions: put all the functions we're defining here

# First we are going to start out with a simple implementation of a read_xyz type function. This function is usable and a good starting point,
# but, it has some small hiccups. 
def read_xyz(file_name, atom_str):
    """reads an xyz file, only extracts coordinates, does not worry about comments
    BIG NOTE: This solution only works if:
    a) There is *something* in the comments, i.e. it's not just '\n'
    b) The atom characters that appear in the lines that have cartesian coordinates do not appear in the comments
    ex b) if a coordinate (cd) line is "H x y z", then the comment should/can not be "Have a nice day"
        :param file_name: string name of the xyz file to be written
        :param atom_str: string of atoms in order of the standard coordinates
    """
    num_atoms = len(atom_str)
    cd_list = []  # create an empty list to append your coordinate values to
    with open(file_name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_stripped = line.strip()  #get rid of whitespace
            if line_stripped == str(num_atoms):
                cds = np.zeros((num_atoms, 3))  #new coordinate
                ct = 0
            elif any(atm in line_stripped for atm in atom_str):
                cd_str = line_stripped.split()[1:]
                cds[ct] = [float(xyorz) for xyorz in cd_str]
                ct += 1
            elif line_stripped == "":
                cd_list.append(cds)
    return np.array(cd_list)  # return a proper numpy array instead of a list so that it is easier to work with (and easier to save in an npy or npz)

# Try running this function a few times before writing anything of your own. Do you understand how it works? Do you see how a & b in the notes could cause problems?
# When you are ready, try filling out this function. 
# In this implementation we are going to focus on counting lines and the pattern of the xyz file instead of reading for specific characters. 
def read_xyz_with_numbers(file_name, num_atoms):
    """reads an xyz file, only extracts coordinates, does not worry about comments
    This is a better implementation because it uses the count structure of a .xyz file to extract the cds.
        :param file_name: string name of the xyz file to be written
        :param num_atoms: the number of atoms in your system. (how many atoms per geometry?)
    """
    # A little hint to get you started, Set up variables that know the size of the various parts of your xyz.
    block = num_atoms + 3  # every coordinate block has the header (1) +  comments (1) + num atoms (x) + newline (1)
    chunk = np.arange(block)  # Here we set chunk to be the indices of block (an array 0 -> len(block))
    atm_chunk = chunk[2:-1]
    cd_list = []
    with open(file_name, 'r') as f:
    ...
    return np.array(cd_list)


def write_xyz(file_name, cds, atom_str):
    """writes an xyz file from some saved coordinates.
        :param file_name: string name of the xyz file to be written
        :param cds: list of coordinates
        :param atom_str: string of atoms in order of the standard coordinates
        :returns saves an xyz file of file_name """
    # Think about how you would do this if cds was one array of coordinates or many different geometries (i.e. a 2D or 3D array). 
    # A hint to get you started:  
    with open(file_name, 'w') as f:
        # Now, think about the structure of the xyz file. You will probably need two loops
        # One to loop through the different geometries (You will want this so the code is flexible with one or multiple geometeries)
        # and a second to loop through the atoms in the geometry. 
        ...
    # Does this function need to return anything? How are you monitoring where the file is written?

## Run Script: put the script we'd want to run from the command line here

if __name__ == '__main__':
    # For practice we will start with the test_data.xyz file in the Data folder. If you didn;t download the exercises zip, make sure you have this test data
    # and change the path accordingly, or just download the zip. 
    
    # This test data is 100 different geometeries of the protonated water trimer, H+(H2O)3
    read_coords = read_xyz(file_name="Data/XYZWriter_trimer_structures.xyz",
                        atom_str=["O","H","H","O","H","H","O","H","H"])
    
    # A tidbit for debugging, Here is the third geometry. (Also you can use this to test your write_xyz function)
    third_geom = np.array([
        [-1.96773e-2, -0.673875,    1.51887   ],
        [-2.74829e-3, -1.11168,     0.62399   ],
        [ 0.645775,   -1.08455,     2.00786   ],
        [ 3.95382e-3, -0.910543,   -1.30846   ],
        [ 9.08469e-3, -7.83345e-3, -1.26388   ],
        [ 0.578137,   -1.18991,    -1.99281   ],
        [ 6.03729e-3,  1.63937,    -0.204656  ],
        [-3.35615e-3,  1.0795,      0.604935  ],
        [-0.627287,    2.22295,    -4.96801e-2]
    ])
        
        # Uncomment the following lines when you have completed the functions and are ready to test them 
        # read_coords_numerical = read_xyz_with_numbers(file_name='Data/test_data.xyz', num_atoms=10)
        # write_xyz(file_name="Data/test_data.xyz", cds=third_geom, atom_str=["O","O","O","H","H","H","H","H","H","H"])
