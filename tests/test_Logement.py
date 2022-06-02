import sys

sys.path.insert(1, "src")
from Logement import Logement


def test_updatePrice_appartement():
    logement_test = Logement(0, "2 rue du Pin", "Ry", "Appartement", 30, 70000)
    assert logement_test.updatePrice() == 66500


def test_updatePrice_maison():
    logement_test = Logement(0, "1 rue du Pin", "Niort", "Maison", 110, 160000)
    assert logement_test.updatePrice() == 184000


def test_updatePrice_error():
    logement_test = Logement(0, "3 rue du Pin", "Arles", "Terrain", 60, 50000)
    assert logement_test.updatePrice() == 50000
