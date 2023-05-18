import pytest
from satyampy import __main__

def test_adding(sample_inputs):
    x, y = sample_inputs
    assert __main__.adding(x, y) == 5