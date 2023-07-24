import pytest
from lib.make_snippet import *

def test_make_snippet():
    result = make_snippet("a b c d e f")
    assert result == "a b c d e..."
    