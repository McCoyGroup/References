"""
Goal: To read and write a *.xyz file type
Fundamentals: None specifically. 
Related Exercises: See https://stackoverflow.com/c/mccoygroup/questions/81 
"""

## Imports: put all import statments here

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
]

def read_xyz(file_name):
    """reads an xyz file ... """
    # Think about how you would do this if crds was one array of coordinates of many different geometries. 
    # A hint to get you started:  
    with open(file_name, 'r') as f:
        ...


def write_xyz(file_name, crds, atom_str):
    """writes an xyz file from some save coordinates.
        :param file_name: string name of the xyz file to be written
        :param crds: list of coordinates
        :param atom_str: string of atoms in order of the standard coordinates
        :returns saves an xyz file of file_name """
    # Think about how you would do this if crds was one array of coordinates of many different geometries. 
    # A hint to get you started:  
    with open(file_name, 'w') as f:
        ...
            

## Run Script: put the script we'd want to run from the command line here

if __name__ == '__main__':
    ...
