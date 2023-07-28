from lib.check_grammar import *
import pytest

def test_empty_string_returns_false():
    result = check_grammar("")
    assert result == False

def test_string_doesnt_start_with_lowercase():
    result = check_grammar('ami')
    assert result == False

def test_string_does_start_with_uppercase_and_doesnt_end_with_punctuation_mark():
    result = check_grammar('Ami')
    assert result == False

def test_string_does_start_with_uppercase_and_does_end_with_punctuation_mark():
    result = check_grammar('Makers!')
    assert result == True

def test_string_doesnt_start_with_uppercase_and_does_end_with_punctuation_mark():
    result = check_grammar("makers!")
    assert result == False

def test_argument_not_string():
    with  pytest.raises(Exception) as e:
        check_grammar(100)
    error_message = str(e.value)
    assert error_message == "Error: input not a string"

