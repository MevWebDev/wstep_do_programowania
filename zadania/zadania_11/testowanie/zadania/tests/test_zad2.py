import pytest

@pytest.fixture
def lista():
    return [9,1,6,8,4,3,2,0]

def sort_by_max(lista):
    for i in range(len(lista)-1):
        max = 0
        for j in range (1,len(lista)-i):
            if lista[max] < lista[j]:
                max = j

        swap = lista[-1-i]
        lista[-1-i] = lista[max]
        lista[max] = swap

    return lista

def test_sort_by_max(lista):
    assert sort_by_max(lista) == [0,1,2,3,4,6,8,9]