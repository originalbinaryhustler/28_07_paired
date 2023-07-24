from lib.counter import *

def test_initial():
    example = Counter()
    result = example.count
    assert result == 0

def test_counter_add():
    example = Counter()
    example.add(5)
    result = example.count
    assert result == 5

def test_counter_report():
    example = Counter()
    result = example.report()
    assert result == "Counted to 0 so far."