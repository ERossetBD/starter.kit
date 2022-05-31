import sys
import pytest

sys.path.insert(1, 'src')
from Logement import Logement

def test_updatePrice_appartement():
    logement_test = Logement(0, "10 rue des Pins", "Niort", "Appartement", 30, 70000)
    assert logement_test.updatePrice() == 66500

def test_updatePrice_maison():
    logement_test = Logement(0, "10 rue des Pins", "Niort", "Maison", 110, 160000)
    assert logement_test.updatePrice() == 184000

def test_updatePrice_error():
    logement_test = Logement(0, "10 rue des Pins", "Niort", "Terrain", 60, 50000)
    assert logement_test.updatePrice() == 50000
    
