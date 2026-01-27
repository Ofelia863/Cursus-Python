import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: Rood")
test_output(oefening_path, "Rood", "Rood")


print("Test 2: Groen")
test_output(oefening_path, "Groen", "Groen")


print("Test 3: Blauw")
test_output(oefening_path, "Blauw", "Blauw")
