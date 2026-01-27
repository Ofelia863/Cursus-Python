import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: getal = 5.4")
test_output(oefening_path, "3.1", "5.4")


print("Test 1: getal = 0")
test_output(oefening_path, "-2.3", "0")


print("Test 1: getal = -2.3")
test_output(oefening_path, "-4.6", "-2.3")
