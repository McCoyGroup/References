from Peeves.Doc import *
import os

__pkgs__ = [
    "McUtils",
    "Psience",
    "Peeves",
    "RynLib"
]

target = os.path.join(os.path.dirname(__file__), "Documentation")
DocWalker(__pkgs__,
          target,
          ignore_paths=['RynLib.md']
          ).write_docs()