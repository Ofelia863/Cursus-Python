import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")


test_output(oefening_path, "-4 is geen priemgetal.", "-4")
test_output(oefening_path, "-3 is een priemgetal.", "-3")
test_output(oefening_path, "3 is een priemgetal.", "3")
test_output(oefening_path, "4 is geen priemgetal.", "4")
test_output(oefening_path, "6 is geen priemgetal.", "6")
test_output(oefening_path, "7 is een priemgetal.", "7")
test_output(oefening_path, "8 is geen priemgetal.", "8")