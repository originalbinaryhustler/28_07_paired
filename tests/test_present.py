import pytest 

from lib.present import *

def test_present_initial():
    example = Present()
    result = example.contents
    assert result == None

def test_present_wrap():
    example = Present()
    example.wrap('Book')
    result = example.contents 
    assert result == 'Book'


def test_present_wrap_error():
    example = Present()
    example.wrap('Book')
    with pytest.raises(Exception) as e:
        example.wrap('Chocolate')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


def test_present_unwrap():
    example = Present()
    example.wrap('Book')
    result = example.unwrap()
    assert result == "Book"


def test_present_unwrap_error():
    example = Present()
    with pytest.raises(Exception) as e:
        example.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."


