ONE

1. Describe the Problem
   As a user
   So that I can keep track of my tasks
   I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface

class TaskManager:

    def __init__(self):
        # Parameters:
        #   No parameters
        # Side effects:
        #   Initialises a list to store tasks
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def list_tasks(self):
        # Returns:
        #   A list consisting of todo tasks
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def mark_task_as_complete(self, task):
        # Parameters:
            # task: string representing a single task
        # Returns:
            Nothing
        # Side effects
        #   Removes the task from the self object

3. Create Examples as Tests

""" When a TaskManager object is created, an empty list is
intialised.
"""
task_manager = TaskManager()

"""
Given a task, TaskManager adds the task to
the list of tasks
"""
task_manager = TaskManager()
task_manager.add("Walk the dog") # stores "Walk the dog" as a task in a list

"""
Given a task, #mark_test_as_complete removes the task from
the list of tasks.
"""
task_manager = TaskManager()
task_manager.add("Walk the dog")
task_manager.mark_task_as_complete("Walk the dog") # removes "Walk the dog" from the list of tasks

"""
When #list_tasks is called, #list_tasks lists the tasks that
have been added and are not yet complete.
"""
task_manager = TaskManager()
task_manager.add("Walk the dog")
task_manager.list_tasks() # lists the tasks stored in the list of tasks

"""
#list_tasks raises an exception if there are no listed tasks.
"""
task_manager = TaskManager()
task_manager.list_tasks() # raises an error with the message "No tasks listed."
