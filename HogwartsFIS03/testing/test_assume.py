import pytest


def test_a():
    # assert 1 == 1
    # assert False == True
    # assert 100 == 200

    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(100 == 200)
    pytest.assume(300 == 1)