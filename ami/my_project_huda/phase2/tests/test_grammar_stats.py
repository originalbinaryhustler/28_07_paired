from lib.grammar_stats import *

def test_object():
    grammar_stats = GrammarStats()
    assert grammar_stats

def test_check_with_empty_string():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("")
    assert result == False

def test_check_with_no_initial_capital_letter_and_no_punctuation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello")
    assert result == False

def test_check_with_no_initial_capital_letter_and_punctuation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("hello.")
    assert result == False

def test_check_with_initial_capital_letter_and_no_punctuation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello")
    assert result == False

def test_check_with_initial_capital_letter_and_punctuation_mark():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Hello.")
    assert result == True

def test_percentage_good():
    grammar_stats = GrammarStats()
    grammar_stats.check("Hello")
    grammar_stats.check("hello.")
    grammar_stats.check("Hello.")
    grammar_stats.check("hello")
    result = grammar_stats.percentage_good()
    assert result == 25
