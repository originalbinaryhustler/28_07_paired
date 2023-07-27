from lib.grammar_stats import *
import pytest


''' 
    `self.percentage_true = 100 / self.checks_made * self.checks_true
    self.checks_false = 100 - self.percentage `
Use Case
Two Methods:

    0: __init__(self)
    self.punctuation == to our punctuation
    self.checks_made = 0
    self.checks_true = 0
    

    1: check(self , one param text: str)
        returns : boolean
        Check first char in string if its Upper-Case
        Check last char in string if its sentecne-ending punctuation mark
            using Idexing [0],[-1]

    2: percentage_good(self)
        returns: int
        100 / num of checks made * num checks resulting in true


'''



def test_init_of_class():
    example = GrammarStats()
    assert example.punctuation == ['.','!','?']
    assert example.checks_made == 0
    assert example.checks_true == 0

def test_check_asserts():
    example = GrammarStats()
    assert example.check('hey') == False
    assert example.check('Hey') == False
    assert example.check('hey!') == False
    assert example.check('Hey!') == True

def test_check_percentage_successive_checks_made():
    example = GrammarStats()
    assert example.percentage_good() == 0
    example.check('Hey!')
    assert example.percentage_good() == 100
    example.check('hey')
    assert example.percentage_good() == 50
    example.check('Benedict.')
    example.check('YASIEN?')
    assert example.percentage_good() == 75

def test_check_percentage_one_false_check_made():
    example = GrammarStats()
    example.check('hey')
    assert example.percentage_good() == 0

def test_assertion_err_in_check_method():
    example = GrammarStats()
    with pytest.raises(Exception) as err:
        example.check('')
        example.check(100)
    error_message = str(err.value)
    assert error_message == 'Error: Instance type must be a string'
    




'''
Test Case
Tests:
1.
    Make an instance of gramamr stats class example= GrammarStats()
        Check that self.punctuation contains ! or . or ?
        Check that self.checks_made starts at 0
        Check that self.checks_true starts at 0
    
2.
    for check
        Check that empty string returns False
        Check that lower cap [0] returns False
        Check that upper case [0] and no punc[-1] returns False
        Check that lower case [0] and punc inc[-1] returns False
        Check that upper case[0] and punc inc[-1] returns True
        check the input of worng type throws err isinstance()

3.
    for percentage_good
        Check that no grammar checks returns 0
        Check 1 True in 1 check returns 100
        Check that 1 False in 1 check returns 0
        Check that 1 True and 1 False in 2 checks returns 50
        Check that 3 True and 1 False in 4 checks returns 75
        
'''