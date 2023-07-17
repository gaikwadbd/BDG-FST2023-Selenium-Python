# run this code:
# PS \\PyTest\\tests> py.test MarkerUse.py -m login ->>>>>> Run only markup related testcase
# PS \\PyTest\\tests> py.test .\MarkerUse.py -k LandingPage -v  ----------> run only group related only
import pytest


@pytest.mark.login
def test_m1():
    assert False


@pytest.mark.login
def test_m2_Login():
    assert 5 == 4


@pytest.mark.home
def test_m3_HomeTest():
    assert "nishant" == "Bharat"


@pytest.mark.login
def test_m3_LandingPage():
    assert "abc" != "Bharat"


@pytest.mark.home
def test_m4_LandingPage():
    assert "abc" != "Bharat"

