import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Pizza's = 4, eters = 3")
test_output(oefening_path, "2 stukken", "4", "3")

print("Pizza's = 11, eters = 15")
test_output(oefening_path, "13 stukken", "11", "15")

print("Pizza's = 2, eters = 4")
test_output(oefening_path, "0 stukken", "2", "4")