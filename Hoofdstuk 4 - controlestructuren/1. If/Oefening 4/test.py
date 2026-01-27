import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "Geslaagd", "2","5","10","4","8")
test_output(oefening_path, "Geslaagd", "3","5","10","4","8", "3","5")
test_output(oefening_path, "Gebuisd", "2","4","10","4","8")