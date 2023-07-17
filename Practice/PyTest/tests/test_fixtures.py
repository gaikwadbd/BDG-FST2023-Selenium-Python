# The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute

# @pytest.fixture()
# executes specific method before every test method

# @pytest.yield_fixture()
# Executed specific method before and after every test method

import pytest


# python -m pytest -v -s .\test_fixtureStudy.py

@pytest.fixture()
def setUp():
    print("Once before every method")


def testmethod1(setUp):
    print("This is test method1")


def testmethod2(setUp):
    print("This is test method2")


# output-->
"""collected 2 items
test_fixtureStudy.py::testmethod1 Once before every method
This is test method1
PASSED
test_fixtureStudy.py::testmethod2 Once before every method
This is test method2
PASSED
"""