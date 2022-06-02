import sys
import os

sys.path.insert(1, "src")
from Logement import Logement
from ExportData import ExportData


def test_export():
    lst_test = []
    lst_test.append(Logement(0, "1 rue Pavé ", "Ry", "Appartement", 30, 70000))
    lst_test.append(Logement(1, "2 rue du Pin", "Pau", "Maison", 110, 160000))

    ExportData().export(lst_test, "exportTest.csv")
    csvExiste = os.path.isfile("data/output/exportTest.csv")

    assert csvExiste is True
