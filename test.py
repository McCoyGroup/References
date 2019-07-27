"""Misc tests for my misc packages
Each package can package its own tests I figure?
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Peeves.TestUtils import TestManager
test_dir = os.path.dirname(__file__)
test_root = os.path.dirname(test_dir)
test_pkg = os.path.basename(test_dir)
TestManager.test_root = test_root
TestManager.test_pkg = test_pkg
TestManager.run()