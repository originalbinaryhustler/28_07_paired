from lib.gratitudes import *

def test_gratitudes_intial():
    example = Gratitudes()
    result = example.gratitudes
    assert result == []

def test_gratitudes_add():
    example = Gratitudes()
    example.add('to be alive')
    result = example.gratitudes
    assert result == ['to be alive']

def test_gratitudes_format():
    example = Gratitudes()
    example.add('to see')
    result = example.format()
    assert result == "Be grateful for: to see"

def test_gratitudes_format_multiple():
    example = Gratitudes()
    example.add('to be able to walk')
    example.add('my family')
    result = example.format()
    assert result == "Be grateful for: to be able to walk, my family"