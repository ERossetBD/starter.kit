import sys
import os
import pytest
sys.path.insert(1, 'src')

from Logement import Logement
from ExportData import ExportData

def test_export():
    lst_test = []
    lst_test.append(Logement(0, "10 rue des Pins", "Niort", "Appartement", 30, 70000))
    lst_test.append(Logement(1, "12 rue des Pins", "Niort", "Maison", 110, 160000))

    ExportData().export(lst_test, "exportTest.csv")
    csvExiste=os.path.isfile("data/output/exportTest.csv")

    assert csvExiste == True