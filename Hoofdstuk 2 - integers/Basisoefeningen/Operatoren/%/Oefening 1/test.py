import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("a = 9, b = 5")
test_output(oefening_path, "4", "9", "5")

print("a = 11, b = 2")
test_output(oefening_path, "1", "11", "2")

print("a = -24, b = 5")
test_output(oefening_path, "1", "-24", "5")