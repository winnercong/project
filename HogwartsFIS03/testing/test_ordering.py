# -*- coding: utf -8 -*-
# @Author   : shencong
# @File     : test_ordering.py

from time import sleep

import pytest


@pytest.mark.last
def test_foo():
    sleep(1)
    assert True


@pytest.mark.fourth
def test_bar():
    sleep(1)
    assert True


@pytest.mark.third
def test_aar():
    sleep(1)
    assert True
