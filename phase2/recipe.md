ONE----------------------------------------------------------------------------------------------

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

TWO----------------------------------------------------------------------------------------------

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

THREE----------------------------------------------------------------------------------------------

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


FOUR----------------------------------------------------------------------------------------------



1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.
As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class TaskTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters: 0
        #   
      
        self.task_list = []
        

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def view_tasks(self):
        # Returns:
        #   A return string of tasks 'new lines for each tasks (Tasks to complete: new line and bullet points *)
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def task_complete(self, task):
        # Returns:
        #   Returns a string f'You have completed {Task}' 
        #   pop the task thats complete from the self.task_list
        #
        #
3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
Initialise an instance of the class 
Class initialised with empty list
"""
reminder = TaskTracker()
reminder.task_list # => []

"""
Check the add function with tasks
self.task_list contains the tasks 
"""
reminder = TaskTracker()
reminder.add_task('Go home and study!')
reminder.task_list # => ['Go home and study!]

reminder.add_task('Clean up!')
reminder.task_list # => ['Go home and study!','Clean up!']

"""
Check add function with input that isn't a string
Should throw an error
"""
reminder = TaskTracker()
reminder.add_task(100) => 'Error: Input not of string type'

"""
Calling view_task method on an instance with an empty task list
Should return a message telling the user the list is empty
"""
reminder = TaskTracker()
reminder.view_tasks()

Calling view_task method on an instance
Check the format of the list returning is correct format as proposed
"""
reminder = TaskTracker()
reminder.add_task('Charge laptop')
reminder.add_task('Go shopping')
reminder.view_tasks() # => f'You have the following tasks remaining:
                                * Charge laptop
                                * Go shopping'

"""
Calling task_complete with a task in self.task_list
Should retun a formatted string with task complete and remove task from self.task_list
"""
reminder = TaskTracker()
reminder.add_task('Walk the dog!')
reminder.add_task('Clean the kitchen')
reminder.task_complete('Walk the dog!') # => 'Task Completed: Walk the dog!'
reminder.task_list => ['Clean the kitchen']

"""
Calling task_complete with a task not in self.task_list
Should return an Exception
"""
reminder = TaskTracker()
reminder.add_task('Walk the dog!')
reminder.task_complete('Call mum') # => 'Error: Task not in Task List. Please use the add_task method first.'

"""
Calling task_complete with an input that isn't a string
Should throw an error
"""
reminder = TaskTracker()
reminder.add_task('Walk the dog!')
reminder.task_complete(100) # => 'Error: Input not of string type'


4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.




FIVE----------------------------------------------------------------------------------------------



1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them

2. Design the Class Interface

Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

# EXAMPLE

class MusicLibrary:
    
    def __init__(self):
        # Parameters:
        #   None  
        #   
        # Attributes:  
        #   self.music_dict = {}
        

    def add_track(self, artist, track):
        # Parameters:
        #   artist: string representing an artist or band
        #   track: string representing a track name
        # Returns:
        #   Nothing
        # Side-effects:
        #   Saves the artist and a track as a key: value pair in the self.music dict. Tracks will be saved in a list.
        #   Prints a message to the user stating that the track has been added
        pass # No code here yet

    def view_artists(self):
        # Parameters:
        #   None
        # Returns:
        #   Nothing
        # Side-effects:
        #   Prints each artist on a new line
        pass # No code here yet

    def view_tracks_by_artist(self, artist):
        # Parameters:
        #   artist: a string representing an artist stored in the music_dict
        # Returns:
        #   Nothing 
        #  Side-effects:
        #   Prints each song by the given artist on a new line
    
    def view_library(self):
        # Parameters:
        #   None
        # Returns:
        #   None
        # Side-effects:
        #   Prints a formatted string for each artist with the name of the artist followed by each song
        #       that artist has in the dictionary. E.g. Tupac: Starin Through My Rearview
    
    def remove_track(self, artist, track):
        # Parameters:
        #   artist: string representing an artist or band
        #   track: string representing a track name
        # Returns:
        #   None
        # Side-effects:
        #   Prints a message saying the track has been removed
        #   Removes the track from the music_dict
    
    def remove_artist(self, artist):
        # Parameters:
        #   artist: string representing an artist or band
        # Returns:
        #   None
        # Side-effects:
        #   Prints a message saying the artist has been removed
        #   Removes the dictionary with the key value matching the given artist
    
    def favourite_artist(self):
        # Parameters:
        #   None
        # Returns:
        #   None
        # Side-effects:
        #   Prints the name of the artist with the most songs and stating how many songs they have
    
3. Create Examples as Tests

Make a list of examples of how the class will behave in different situations.

# EXAMPLE

"""
Initialise an instance of the class 
Class initialised with empty dict
"""
library = MusicLibrary()
library.music_dict # => {}

"""
Check the add track function with artist: track pairs
self.music_dict contains the artist: tracks key, value pairs
"""
library = MusicLibrary()
library.add_track('Tupac', 'Uppercut')
library.music_dict # => {'Tupac': ['Uppercut']}
library.add_track('Nipsey Hussle', ''Blue Laces'')
library.music_dict # => {'Tupac': ['Uppercut'], 'Nipsey Hussle': ['Blue Laces']}
library.add_track('Tupac', 'The Return')
library.music_dict # => {'Tupac': ['Uppercut', 'The Return'], 'Nipsey Hussle': ['Blue Laces']}

"""
Check the add track function using the wrong object type
Should throw an error
"""
library = MusicLibrary()
library.add_track(100, True) # => 'Error: Please ensure inputs are of the type string.'

"""
Check remove_track method with an artist and track pair
Should remove track from the music_dict
"""
library = MusicLibrary()
library.add_track('Tupace', 'Uppercut')
library.add_track('Tupac', 'Starin Through My Rearview')
library.remove_track('Tupac', 'Uppercut')
library.music_dict # => {'Pink Tupac': ['Starin Through My Rearview']}

"""
Check the view tracks function using the wrong object type
Should throw an error
"""
library = MusicLibrary()
library.view_tracks_by_artist(100) # => 'Error: Please ensure input is of the type string.'

"""
Check the remove tracks function using the wrong object type
Should throw an error
"""
library = MusicLibrary()
library.remove_track(100, True) # => 'Error: Please ensure inputs are of the type string.'

"""
Check the remove artist function using the wrong object type
Should throw an error
"""
library = MusicLibrary()
library.remove_artist(100) # => 'Error: Please ensure input is of the type string.'




4. Implement the Behaviour

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.