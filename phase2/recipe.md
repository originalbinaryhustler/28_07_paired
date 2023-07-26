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

TWO

1. Describe the Problem
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

2. Design the Function Signature

def grammar_check(text):
    '''Returns a boolean if the string starts with a capital letter and ends with a suitable sentence-ending punctuation mark e.g. . !

    Parameters:
        text: a string representing some text (e.g 'Hello, my name is Ben. It is nice to meet you.')
    
    Returns:
        A boolean
    
    Side effects:
        This function doesn't have any other side effects
    '''
    pass

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

'''
Given an empty string
Should return False
'''
grammar_check('') => False

'''
Given a string that starts with a lower case letter
Should return False
'''
grammar_check('ami') => False

'''
Given a string starting with a capital letter
Should return True
'''
grammar_check('Ami') => True

'''
Given a string starting with a capital letter but not ending with a suitable punctuation mark
Should return False
'''
grammar_check('Hello') =>False

'''
Given a string starting with a capital letter and ending with a suitable punctuation mark
Should return True
'''
grammar_check('Makers!') => True

'''
Given a string that starts with a lowercase letter but ends with a suitable punctuation mark
Should return False
'''
grammar_check('makers.') => False



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

THREE

1. Describe the Problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature

def check_todo(text):
    '''Returns a Boolean if the input string contains the string '#TODO' (case sensitive)

    Parameters:
        text: a string representing some text (e.g '#TODO homework')
    
    Returns:
        A boolean
    
    Side effects:
        This function doesn't have any other side effects
    '''
    pass

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

'''
Given an empty string
It should return False
'''
check_todo('') => False

'''
Given a string that does not contain #TODO
Should return False
'''
check_todo('Hello there') => False

'''
Given a string that contains a lower_case #TODO
Should return Flase
'''
check_todo('#todo go for a walk') => False

'''
Given a string that contains an upper_case #TODO 
Should return True
'''
check_todo('#TODO walk the dog!') => True

'''
Given an argument that is not a string
Should throw an exception error
'''
check_todo(100) => Exception Error


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