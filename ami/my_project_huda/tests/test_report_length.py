from lib.report_length import *

def test_length_eight_works():
    result = report_length("Benedict")
    assert result == ("This string was 8 characters long.")

def test_empty_string():
    result = report_length("")
    assert result ==("This string was 0 characters long.")
