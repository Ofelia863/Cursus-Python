import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "Negatief saldo", "-239")
test_output(oefening_path, "Negatief saldo", "-0.01")
test_output(oefening_path, "", "0")
test_output(oefening_path, "", "10000")
test_output(oefening_path, "VIP-klant", "10000.01")
test_output(oefening_path, "VIP-klant", "4000000")