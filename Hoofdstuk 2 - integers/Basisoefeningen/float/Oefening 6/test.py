import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: getal = 25")
test_output(oefening_path, "2.04939015319192", "4.2")


print("Test 1: getal = 0")
test_output(oefening_path, "0.0", "0")


print("Test 1: getal = 4")
test_output(oefening_path, "2.0", "4")


print("Test 1: getal = -9")
test_output(oefening_path, "(1.8369701987210297e-16+3j)", "-9")
