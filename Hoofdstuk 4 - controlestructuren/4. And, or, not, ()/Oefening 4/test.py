import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")


test_output(oefening_path, "Toegestaan", "2008", "Wel")
test_output(oefening_path, "Toegestaan", "2008", "Niet")
test_output(oefening_path, "Toegestaan", "2010", "Wel")
test_output(oefening_path, "Geweigerd", "2010", "Niet")
test_output(oefening_path, "Geweigerd", "2011", "Niet")
test_output(oefening_path, "Geweigerd", "2011", "Niet")

