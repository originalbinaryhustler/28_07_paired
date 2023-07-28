from lib.task_manager import *
import pytest

""" When a TaskManager object is created, an empty list is
intialised.
"""
task_manager = TaskManager()
assert task_manager.task_list == []

"""
Given a task, TaskManager adds the task to
the list of tasks
"""
task_manager = TaskManager()
task_manager.add("Walk the Dog")
assert task_manager.task_list == ["Walk the Dog"]

"""
Given a task, #mark_test_as_complete removes the task from
the list of tasks.
"""
task_manager = TaskManager()
task_manager.add("Walk the dog")
task_manager.mark_task_as_complete("Walk the dog")
assert task_manager.task_list == []

"""
When #list_tasks is called, #list_tasks lists the tasks that
have been added and are not yet complete.
"""
task_manager = TaskManager()
task_manager.add("Walk the dog")
result = task_manager.list_tasks()
assert result == ["Walk the dog"]

"""
#list_tasks raises an exception if there are no listed tasks.
"""
task_manager = TaskManager()
with pytest.raises(Exception) as e:
    task_manager.list_tasks()
error_message = str(e.value)
assert error_message == "Error: no listed tasks."
