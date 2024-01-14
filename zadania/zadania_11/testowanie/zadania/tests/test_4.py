def test_suma1():
    assert suma(1,2) == 3
def test_suma2():
    assert suma(-2,8) == 6
def test_suma3():
    assert suma(21,37) == 58

def suma(a,b):
    return a + b