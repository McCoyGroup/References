""" Goal: To serve as a template for writing your own example scripts
"""

## Imports: put all import statments here

import numpy as np, scipy.sparse as sp
from matplotlib.pyplot import subplots

## Exports: put all the names things we might want to use in other scripts here

__all__ = [
    "SampleObject",
    "sample_function"
]

## Objects: put all the classes we're defining here
# A class is way that a program can represent an object, like a Molecule or an Animal.
# There's a convention in python that functions are lower-case and words are separated by underscores,
#  while classes and objects have capital letters and are in camel-case (where words are all started in upper case).
# Classes are useful as ways to ease the mental burden on the programmer, as having a conceptual hierarchy in place
#  makes it easier to remember what's going on and what an object should do.
# Using them is highly recommended, but for the kinds of things we do you can totally get away with just chaining
#  functions together one-by-one.

class SampleObject:
    """
    This is a sample object to show best practices for making objects.
    We're gonna pretend it has a _setting_ (maybe on/off) and a _mode_ (maybe slow/medium/fast)
    """
    def __init__(self, setting, mode='fast'):
        """
        Sets up the object,
        :param setting:
        :type setting: bool
        :param mode:
        :type mode: str
        """
        self.setting = setting
        self.mode = mode

    def toggle(self):
        """
        Toggles the internal setting
        """
        self.setting = not self.setting

    @property
    def is_on(self):
        """
        Tells us if we're on or not
        :return:
        :rtype: bool
        """
        return

    def do_a_thing(self, data):
        """
        Does a thing to some data based on whether we're on/off and slow/medium/fast.
        You can modify this to do your thing, if you want
        :param data:
        :type data:
        :return:
        :rtype:
        """
        if self.is_on:
            if self.mode == 'fast':
                ...
            elif self.mode == 'slow':
                ...
            elif self.mode == 'medium':
                ...
            else:
                # raise some kind of Exception to tell people that you don't know what to do
                raise ValueError(...)
        else:
            # we're not even turned on so don't do anything to the data
            return data


## Functions: put all the functions we're defining here
# In python, a standard thing is to have 90% of the work done by a class or set of classes
#  and then have a 'convenience' function that just sets up a one-time-use class and calls
#  its methods.
# This is slower than using the classes directly, but if you don't need the performance it can be
#  more convenient.

def sample_function(data, mode='fast'):
    """
    Just sets up a SampleObject and calls its `do_a_thing` method
    :param data:
    :type data:
    :param mode:
    :type mode: str
    :return:
    :rtype:
    """
    setting = True
    return SampleObject(setting, mode=mode).do_a_thing(data)

## Run Script: put the script we'd want to run from the command line here
# Every time a python file loads it has a `__name__` variable set.
# If the file is called from the command line, this variable is set ot the string `"__main__"`.
# A classic thing, then, is to provide a block at the bottom of your file that's wrapped in the idiom
# `if __name__ == '__main__':` which provides some commands to run if the file is called from the command line

if __name__ == '__main__':
    # We're gonna define a run script here, where just call `sample_function` on whatever
    #   arguments were passed to the command line.
    # These arguments are always in `sys.argv` and the first argument is always the file name.
    from sys import argv

    res = sample_function(argv[1:])
    print("Got {} from the script {}".format(res, argv[0]))