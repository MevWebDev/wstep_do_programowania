import pytest
from datetime import datetime

# Define fixtures
@pytest.fixture
def pesel1():
    return "08231663632"

@pytest.fixture
def data1():
    return "2030-01-28"

@pytest.fixture
def pesel2():
    return "0"

@pytest.fixture
def data2():
    return "2020-01-28"

@pytest.fixture
def pesel3():
    return "08231663632"

@pytest.fixture
def data3():
    return "2004-01-28"


def pesel_checker(pesel, data):
    if len(pesel)==11:
        rok = "20" + pesel[0] + pesel[1]
        miesiac = pesel[2] + pesel[3]
        miesiac = int(miesiac) - 20
        miesiac = str(miesiac)
        if (len(miesiac) == 1):
            miesiac = "0" + miesiac
        dzien = pesel[4] + pesel[5]
        if (len(dzien)==1):
            dzien = "0" + dzien
        urodzenie = rok + '-' + miesiac + '-' + dzien
        urodzenie = datetime.strptime(urodzenie, '%Y-%m-%d')
        data= datetime.strptime(data, '%Y-%m-%d')
        if urodzenie<data:
            roznica_lat = (data.year - urodzenie.year)
            if (data.month, data.day) < (urodzenie.month, urodzenie.day):
                roznica_lat -= 1
            if (roznica_lat>18):
                return "Pełnoletnia"  
            else:
                return "Niepełnoletnia. Nie kupisz Monsterka kidzie"
        else:
            return "Jeszcze się nie urodziłeś"
    else:
        return "Wprowadzono zle dane"

# Define test function
def test1_peselchecker(pesel1, data1):
    assert pesel_checker(pesel1, data1) == "Pełnoletnia"

def test2_peselchecker(pesel2, data2):
    assert pesel_checker(pesel2, data2) == "Wprowadzono zle dane"

def test3_peselchecker(pesel3, data3):
    assert pesel_checker(pesel3, data3) == "Jeszcze się nie urodziłeś"