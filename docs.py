from Peeves.Doc import *

__pkgs__ = [
    "McUtils",
    "Psience",
    "Peeves",
    "PyDVR",
    "PyVPT",
    "RynDMC"
]

import os
DocWalker(__pkgs__, os.path.join(os.path.dirname(__file__), "docs")).write_docs()