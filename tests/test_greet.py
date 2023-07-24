#file: tests/test_greet.py
from lib.greet import greet

def test_greet_person_of_given_name():
    result = greet("Alice")
    assert result == "hello, Alice!"