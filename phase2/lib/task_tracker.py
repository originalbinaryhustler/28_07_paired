class TaskTracker():
    def __init__(self):
        self.task_list = []
    
    def add_task(self, task):
        if isinstance(task, str):
            self.task_list.append(task)
            print(f'{task} has been added to your task list.')
            return f'{task} has been added to your task list.'
        raise Exception('Error: Input type must be a string.')
    
    def view_tasks(self):
        if len(self.task_list) == 0:
            return 'Task list is currently empty. Please add a task first.'
        formatted_string = f'You have the following tasks remaining:'
        print(formatted_string)
        for i in range(len(self.task_list)):
            print(f' * {self.task_list[i]}\n')
    
    def task_complete(self, task):
        self.task_list.pop(self.task_list.index(task))
        return f'Task Completed: {task}'

tst= TaskTracker()
tst.add_task('Complete work')
tst.add_task('Workout')
tst.add_task('Clean House')
tst.view_tasks()
tst.task_complete('Workout')
tst.view_tasks()
