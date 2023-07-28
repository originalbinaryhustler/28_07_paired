from lib.check_text_includes_todo import *

'''Given an empty string, the function returns False'''
def test_return_false_if_empty_string():
    result = check_text_includes_todo("")
    assert result == False

'''Given a string that does not contain the text #TODO, return False'''
def test_return_false_if_text_does_not_include_todo():
    result = check_text_includes_todo("Hello World")
    assert result == False

'''Given a string that contains the text #TODO once, return True'''
def test_return_true_if_text_includes_todo_once():
    result = check_text_includes_todo("Hello World #TODO")
    assert result == True

'''Given a string contains the text #TODO twice, return True'''
def test_return_true_if_text_includes_todo_twice():
    result = check_text_includes_todo("Hello World #TODO #TODO")
    assert result == True

