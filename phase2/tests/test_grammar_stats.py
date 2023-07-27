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
    assert example.check('') == False
    assert example.check('hey') == False
    assert example.check('Hey') == False
    assert example.check('hey!') == False
    assert example.check('Hey!') == True
    assert example.check(100) == False




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
        Check 1 True in 1 check returns 100
        Check that 1 False in 1 check returns 0
        Check that 1 True and 1 False in 2 checks returns 50
        Check that 3 True and 1 False in 4 checks returns 75
        
'''