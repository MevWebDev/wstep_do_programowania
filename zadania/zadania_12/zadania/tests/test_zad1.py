import pytest

@pytest.fixture
def my_list():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def x():
    return 3

def test_list(my_list, x):
    assert x in my_list
