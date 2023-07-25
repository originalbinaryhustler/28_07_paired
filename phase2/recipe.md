ONE

1. Describe the Problem
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

2. Design the Function Signature
Single function called reading_time().
Takes one string as an argument consisting of a text with multiple words.
The user has a reading speed of 200 words a minute - but perhaps functionality could be put in to take another argument with the users reading speed in wpm.
The output should be a string which states the time in minutes and seconds by dividing the number of words by 200. For the minutes we can use a modulo (%).

def reading_time(text, wpm):
    '''Takes a string of words and returns the time it would take to read them according to a given speed in wpm (words per minute)

    Parameters:
        text: a string containing multiple words (e.g 'Hello, my name is Ben. It is nice to meet you')
        wpm: an integer value referring to the users reading speed in words per minute
    
    Returns:
        A string with the following structure ('At your reading speed of {wpm}, it would take you x minutes and y seconds to read the given text')
    
    Side effects:
        This function doesn't have any other side effects
    '''
    pass

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

'''
Given a blank string
It return a message
'''
reading_time('', 200) => 'No text has been entered'

'''
Given a string where the wpm is GREATER THAN the number of words in the text
It returns with '0 minutes and x seconds' within outputted string
'''
reading_time('Hello world!', 200) => 'At your reading speed of 200 WPM it would take you 0 minutes and y seconds to read the given text'

'''
Given a string where the wpm is LESS THAN the number of words in the text
It returns with 'x minutes and y seconds' within the outputted string
'''
reading_time('Hello, my name is Ben. It is nice to meet you', 5) => 'At your reading speed of 5 WPM it would take you x minutes and y seconds to read the given text'

'''
Given a string where the wpm is THE SAME as the number of words in the text
It returns with '1 minutes and 0 seconds' within the outputted string
'''
reading_time('Hello there', 2) => 'At your reading speed of 2 WPM it would take you 1 minutes and 0 seconds to read the given text'

'''
Given a string with a great number of words
It returns the correct answer in the correct format and is returned in an acceptable timeframe
'''
reading_time(<example-text>, 20) => 'At your reading speed of 20 WPM it would take you x minutes and y seconds to read the given text'

'''
Given an argument that isn't a string and integer pair
It throws an error
'''
reading_time(True, 200) => 'Input types incorrect: Please ensure it is a string and an integer'


4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

Here's an example for you to start with:

# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
Ensure all test function names are unique, otherwise pytest will ignore them!

