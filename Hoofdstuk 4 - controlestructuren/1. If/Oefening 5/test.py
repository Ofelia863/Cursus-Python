import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "Hittegolf", "27", "25", "26", "31", "32", "31", "20")
test_output(oefening_path, "Hittegolf", "25", "25", "26", "31", "32", "30", "20")
test_output(oefening_path, "", "25", "25", "26", "31", "32", "20", "21")
test_output(oefening_path, "", "24", "25", "32", "31", "32", "20", "21")

