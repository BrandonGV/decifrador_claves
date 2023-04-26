import pytest
from main import busqueda_binaria
from main import ordenar_mezlca
def test_busqueda_binaria():
    assert busqueda_binaria([1,2,3,4,5,6,7,8])==[1,2,3]
