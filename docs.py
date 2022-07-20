from Peeves.Doc import *
import os, sys

root = os.path.dirname(os.path.dirname(__file__))
target = os.path.join(root, "Documentation")
sys.path.insert(0, root)
doc_config = {
    "packages": [
        {
            "id": "McUtils",
            'tests_root': os.path.join(os.path.dirname(root), "McUtils", "ci", "tests")
        },
        {
            "id": "Psience",
            'tests_root': os.path.join(os.path.dirname(root), "Psience", "ci", "tests")
        },
        {
            "id": "Peeves",
            'tests_root': os.path.join(os.path.dirname(root), "Peeves", "ci", "tests")
        },
        {
            "id": "RynLib",
            'tests_root': os.path.join(os.path.dirname(root), "RynLib", "ci", "tests")
        }
    ],
    "root": root,
    "target": target,
    "readme": os.path.join(root, "README.md")
}
# DocBuilder(**doc_config).build()
