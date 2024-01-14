import pytest
@pytest.fixture


def lista():
    return [4,2,5,1,7,3]
def bubblesort(lista):
    for n in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                swap = lista[i]
                lista[i] = lista[i+1]
                lista[i + 1] = swap             
    return lista

def test_bubblesort(lista):
    assert bubblesort(lista) == [1,2,3,4,5,7]
            
        
