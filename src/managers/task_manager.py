"""
Task management business logic
"""
from datetime import datetime
from typing import List, Optional
from ..core.task import Task
from ..storage.json_storage import JsonTaskStorage

class TaskManager:
    def __init__(self):
        self.storage = JsonTaskStorage()

    def add_task(self, title: str, description: str) -> Task:
        """Add a new task to the list"""
        task_id = len(self.storage.tasks) + 1
        task = Task(
            id=task_id,
            title=title,
            description=description,
            created_at=datetime.now()
        )
        self.storage.tasks.append(task)
        self.storage.save_tasks()
        return task

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return self.storage.tasks

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a specific task by ID"""
        for task in self.storage.tasks:
            if task.id == task_id:
                return task
        return None

    def toggle_task(self, task_id: int) -> bool:
        """Toggle the completion status of a task"""
        task = self.get_task(task_id)
        if task:
            task.completed = not task.completed
            self.storage.save_tasks()
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by ID"""
        task = self.get_task(task_id)
        if task:
            self.storage.tasks.remove(task)
            self.storage.save_tasks()
            return True
        return False