import pytest
from lib.test_drive_single_function import *

# Tests for the make_snippet function

def test_make_snippet_shorter_than_five():
    result = make_snippet("one two three four")
    assert result == "one two three four"

def test_make_snippet_with_length_of_five():
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

def test_make_snippet_longer_than_five():
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."

def test_make_snippet_wrong_type():
    with pytest.raises(Exception) as e:
        make_snippet(True)
    error_message = str(e.value)
    assert error_message == "Error: Input was not a string."

# Tests for the count_words function

def test_empty_string_has_count_of_zero():
    result = count_words('')
    assert result == 0

def test_string_with_5_words_returns_count_of_five():
    result = count_words('one two three four five')
    assert result == 5

def test_wrong_type_given():
    with pytest.raises(Exception) as e:
        count_words(100)
    error_message = str(e.value)
    assert error_message == 'Error: Input was not a string.'