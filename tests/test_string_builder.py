from lib.string_builder import *

def test_string_builder_initial():
    example = StringBuilder()
    result = example.str
    assert result == ""

def test_string_builder_add():
    example = StringBuilder()
    example.add("Hello there")
    result = example.str
    assert result == "Hello there"

def test_string_builder_size_empty():
    example = StringBuilder()
    result = example.size()
    assert result == 0

def test_string_builder_add_size():
    example = StringBuilder()
    example.add("Hello")
    result = example.size()
    assert result == 5

def test_string_builder_output():
    example = StringBuilder()
    example.add("Hello")
    result = example.output()
    assert result == "Hello"