import pytest


@pytest.fixture
def connectDB():
    print("这是test_a的connectDB方法 ")

def test_a(connectDB):
    print("sub_demo test_a")


def test_b():
    print("sub_demo test_b")