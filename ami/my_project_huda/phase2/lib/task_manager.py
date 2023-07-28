class TaskManager:

    def __init__(self):
        self.task_list = []

    def add(self, task):
        self.task_list.append(task)

    def mark_task_as_complete(self, task):
        self.task_list.remove(task)

    def list_tasks(self):
        if self.task_list != []:
            return self.task_list
        else:
            raise Exception("Error: no listed tasks.")

