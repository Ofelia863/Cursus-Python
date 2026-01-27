import os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir, os.pardir))
sys.path.insert(0, project_root)

from shared.test_helpers import test_output

oefening_path = os.path.join(os.path.dirname(__file__), "oefening.py")

test_output(oefening_path, "2000 is een schrikkeljaar", "2000")
test_output(oefening_path, "2004 is een schrikkeljaar", "2004")
test_output(oefening_path, "2003 is geen schrikkeljaar", "2003")
test_output(oefening_path, "1900 is geen schrikkeljaar", "1900")