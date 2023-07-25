from lib.check_grammar import *

def test_empty_string_returns_false():
    result = check_grammar("")
    assert result == False

def test_string_doesnt_start_with_lowercase():
    result = check_grammar('ami')
    assert result == False

def test_string_does_start_with_uppercase():
    result = check_grammar('Ami')
    assert result == True

def test_string_does_start_with_uppercase_and_doesnt_end_with_punctuation_mark():
    result = check_grammar('Ami')
    assert result == False

