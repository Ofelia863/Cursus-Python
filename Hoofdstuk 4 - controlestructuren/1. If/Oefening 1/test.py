import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "Standaard levering", "-2")
test_output(oefening_path, "Standaard levering", "0")
test_output(oefening_path, "Standaard levering", "5")
test_output(oefening_path, "Standaard levering", "9.99999999")
test_output(oefening_path, "Express levering", "10")
test_output(oefening_path, "Express levering", "10.1")