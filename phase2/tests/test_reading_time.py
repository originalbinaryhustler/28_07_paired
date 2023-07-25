import pytest
from lib.reading_time import *

'''
Single function called reading_time().
Takes one string as an argument consisting of a text with multiple words.
The user has a reading speed of 200 words a minute - but perhaps functionality could be put in to take another argument with the users reading speed in wpm.
The output should be a string which states the time in minutes and seconds by dividing the number of words but 200. For the minutes we can use a modulo (%).
'''

def test_blank_string_returns_message():
    result = reading_time("", 200)
    assert result == 'No text has been entered'

