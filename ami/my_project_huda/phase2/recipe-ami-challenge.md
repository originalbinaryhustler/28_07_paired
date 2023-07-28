ONE

1. Describe the Problem
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature
Single function called check_text_includes_todo().
Takes one string as an argument consisting of text.

def check_text_includes_todo(text):
    '''Takes a string of text and checks if the text includes the string #TODO.'''

    Parameters:
        text: a string representing some text
    
    Returns:
        A boolean which indicates whether the text includes the string #TODO.
    
    Side effects:
        This function doesn't have any other side effects
    '''
    pass

3. Create Examples as Tests
Make a list of examples of what the function will take and return.

'''
Given an empty string, the function returns False
'''
check_text_includes_todo("") => False

'''
Given a string that does not contain the text #TODO, return False
'''
check_text_includes_todo(string) => False

'''
Given a string that does contain the text #TODO, return True
''''
check_text_includes_todo(string) => True

'''Given a string contains the text #TODO twice, return True'''
check_text_includes_todo(string) => True

4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.
Given an empty string
Should return False
'''
