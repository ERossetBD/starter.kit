import sys
import pytest

sys.path.insert(1, 'src')
from ImportData import ImportData

def test_load():
    data_test = ImportData().load('dataTest.csv')
    assert data_test.shape[0] == 17