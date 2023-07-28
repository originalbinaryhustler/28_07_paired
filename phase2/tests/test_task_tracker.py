import pytest
from lib.task_tracker import *

def test_class_init_with_empty_list():
    reminder = TaskTracker()
    assert reminder.task_list == []

def test_add_tasks():
    reminder = TaskTracker()
    assert reminder.add_task('Go home and study!') == 'Go home and study! has been added to your task list.'
    assert reminder.task_list == ['Go home and study!']
    assert reminder.add_task('Clean up!') == 'Clean up! has been added to your task list.'
    assert reminder.task_list == ['Go home and study!','Clean up!']

def test_add_task_with_wrong_input_type_throws_error():
    reminder = TaskTracker()
    with pytest.raises(Exception) as err:
        reminder.add_task(100)
    error_message = str(err.value)
    assert error_message == 'Error: Input type must be a string.'

def test_view_tasks_method_on_an_instance_with_empty_task_list():
    reminder = TaskTracker()
    assert reminder.view_tasks() == 'Task list is currently empty. Please add a task first.'

def test_task_complete_method_should_return_formatted_string_and_remove_task_from_task_list():
    reminder = TaskTracker()
    reminder.add_task('Walk the dog!')
    reminder.add_task('Clean the kitchen')
    assert reminder.task_complete('Walk the dog!') == 'Task Completed: Walk the dog!'
    assert reminder.task_list == ['Clean the kitchen']