class TaskTracker():
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        if isinstance(task, str):
            self.task_list.append(task)
            return f'{task} has been added to your task list.'
        raise Exception('Error: Input type must be a string.')
    
    def view_tasks(self):
        if len(self.task_list) == 0:
            return 'Task list is currently empty. Please add a task first.'
        formatted_string = f'You have the following tasks remaining:'
        new_line = '\n'
        print(formatted_string)
        for i in range(len(self.task_list)):
            print(f' * {self.task_list[i]}')
    
    def task_complete(self, task):
        self.task_list.pop(self.task_list.index(task))
        return f'Task Completed: {task}'