import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")


test_output(oefening_path, "Totaal: 16.0", "20", "17", "nee")
test_output(oefening_path, "Totaal: 16.0", "20", "18", "ja")
test_output(oefening_path, "Totaal: 16.0", "20", "25", "ja")
test_output(oefening_path, "Totaal: 20.0", "20", "18", "nee")
test_output(oefening_path, "Totaal: 20.0", "20", "25", "nee")
test_output(oefening_path, "Totaal: 20.0", "20", "26", "ja")


