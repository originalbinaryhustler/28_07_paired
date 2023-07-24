import pytest 
from lib.present import *

def test_present_initial():
    example = Present()
    result = example.contents
    assert result == None