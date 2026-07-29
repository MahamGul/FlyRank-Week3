from abc import ABC, abstractmethod


class TaskRepository(ABC):

    @abstractmethod
    def get_all_tasks(self):
        pass

    @abstractmethod
    def get_task_by_id(self, task_id):
        pass

    @abstractmethod
    def create_task(self, title):
        pass

    @abstractmethod
    def update_task(self, task_id, title=None, done=None):
        pass

    @abstractmethod
    def delete_task(self, task_id):
        pass