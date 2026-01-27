import os, sys, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

print("Test 1: Amber")
test_output(oefening_path, "Hallo Amber", "Amber")


print("Test 2: Barry")
test_output(oefening_path, "Hallo Barry", "Barry")


print("Test 3: Charles")
test_output(oefening_path, "Hallo Charles", "Charles")
