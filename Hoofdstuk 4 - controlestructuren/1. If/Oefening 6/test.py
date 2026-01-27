import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")


test_output(oefening_path, "Controleer de machine!", "31.34", "32", "33.7", "31.2", "31.3", "35.9", "33", "32", "31.8", "32.3", "32.5", "34.2", "34.3", "33.1", "33")
test_output(oefening_path, "", "31.35", "32", "33.7", "31.2", "31.3", "35.9", "33", "32", "31.8", "32.3", "32.5", "34.2", "34.3", "33.1", "33")
test_output(oefening_path, "Controleer de machine!", "31.35", "32", "33.7", "31.2", "31.3", "35.9", "33", "32", "31.8", "32.3", "32.5", "34.2", "34.66", "33.1", "33")
test_output(oefening_path, "", "31.35", "32", "33.7", "31.2", "31.3", "35.9", "33", "32", "31.8", "32.3", "32.5", "34.2", "34.65", "33.1", "33")
test_output(oefening_path, "", "31.36", "32", "33.7", "31.2", "31.3", "35.9", "33", "32", "31.8", "32.3", "32.5", "34.2", "34.3", "33.1", "33")
test_output(oefening_path, "", "30", "31", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33")
test_output(oefening_path, "", "35", "35", "30", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33")
test_output(oefening_path, "Controleer de machine!", "30", "31", "35", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33", "33", "30")
