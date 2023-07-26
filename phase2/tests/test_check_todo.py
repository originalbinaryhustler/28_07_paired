import pytest 
from lib.check_todo import *

def test_check_empty_string():
    result = check_todo('')
    assert result == False

def test_string_does_not_contain_todo():
    result = check_todo('Hello there')
    assert result == False

def test_string_contains_lower_case_todo():
    result = check_todo('#todo go for a walk')
    assert result == False

def test_string_contains_upper_case_todo():
    result = check_todo('#TODO walk the dog!')
    assert result == True

def test_uppercase_todo_with_punctuation_attached():
    result = check_todo('#TODO: Wash the dishes')
    assert result == True

def test_uppercase_todo_with_puctuation_attached_in_the_middle_of_string():
    result = check_todo('Remember that I have #TODO, the dishes today.')
    assert result == True