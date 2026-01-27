import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: getal = 5.1")
test_output(oefening_path, "26.009999999999998", "5.1")


print("Test 2: getal = 0")
test_output(oefening_path, "0.0", "0")


print("Test 3: getal = -2.1")
test_output(oefening_path, "4.41", "-2.1")

