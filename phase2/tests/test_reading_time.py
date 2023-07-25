import pytest
from lib.reading_time import *

'''
Single function called reading_time().
Takes one string as an argument consisting of a text with multiple words.
The user has a reading speed of 200 words a minute - but perhaps functionality could be put in to take another argument with the users reading speed in wpm.
The output should be a string which states the time in minutes and seconds by dividing the number of words but 200. For the minutes we can use a modulo (%).
'''

'''Takes an empty string and returns a message that no text has been entered.'''
def test_blank_string_returns_message():
    result = reading_time("", 200)
    assert result == 'No text has been entered'

'''Given a string where the words per minute is greater than the words in the text, return a formatted string: "At your reading speed of 200 WPM it would take you 0 minutes and y seconds to read the given text.'''
def test_wpm_greater_than_words_in_text():
    result = reading_time("Hello World",4)
    assert result == "At your reading speed of 4 WPM it would take you 0 minutes and 30 seconds to read the given text."

'''Given a string where the words per minute is less than the words in the text, return a formatted string: "At your reading speed of 200 WPM it would take you x minutes and y seconds to read the given text.'''
def test_wpm_less_than_words_in_text():
    result = reading_time("Hello I am Ben",2)
    assert result == "At your reading speed of 2 WPM it would take you 2 minutes and 0 seconds to read the given text."

'''Given a string where the words per minute is the same as the number of words in the text, return a formatted string: "At your reading speed of 200 WPM it would take you 1 minutes and 0 seconds to read the given text.'''
def test_wpm_equal_to_words_in_text():
    result = reading_time("Hello there",2)
    assert result == "At your reading speed of 2 WPM it would take you 1 minutes and 0 seconds to read the given text."

'''Given arguments that don't match the string and integer types, throw an error.'''
def test_type_error():
    with pytest.raises(Exception) as e:
        reading_time(True,2)
    error_message = str(e.value)
    assert error_message == "Error: Input type is incorrect."