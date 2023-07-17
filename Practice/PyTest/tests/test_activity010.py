import pytest


def test2_m1():
    a = 3
    b = 4
    assert a + 1 == b, "test failed"


def test2_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM"


def test2_m3():
    assert True


def test2_m4():
    assert False


def test2_m5():
    assert 100 == 100


def test2_m6():
    assert "Narwade" == "Narwade"

def test_login():
    assert 20 == 19