"""
Task management business logic
"""
from datetime import datetime
from typing import List, Optional
from ..core.task import Task, SubTask, Priority
from ..storage.json_storage import JsonTaskStorage

class TaskManager:
    def __init__(self):
        self.storage = JsonTaskStorage()

    def add_task(self, title: str, description: str, tags: List[str], 
                 priority: Priority, due_date: Optional[datetime] = None) -> Task:
        """Add a new task to the list"""
        task_id = len(self.storage.tasks) + 1
        task = Task(
            id=task_id,
            title=title,
            description=description,
            created_at=datetime.now(),
            tags=tags,
            priority=priority,
            due_date=due_date,
            subtasks=[]
        )
        self.storage.tasks.append(task)
        self.storage.save_tasks()
        return task

    def add_subtask(self, task_id: int, title: str) -> bool:
        """Add a subtask to an existing task"""
        task = self.get_task(task_id)
        if task:
            subtask_id = len(task.subtasks) + 1
            task.subtasks.append(SubTask(id=subtask_id, title=title))
            self.storage.save_tasks()
            return True
        return False

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

    def toggle_subtask(self, task_id: int, subtask_id: int) -> bool:
        """Toggle the completion status of a subtask"""
        task = self.get_task(task_id)
        if task:
            for subtask in task.subtasks:
                if subtask.id == subtask_id:
                    subtask.completed = not subtask.completed
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

    def search_tasks(self, keyword: str) -> List[Task]:
        """Search tasks by keyword"""
        keyword = keyword.lower()
        return [
            task for task in self.storage.tasks
            if keyword in task.title.lower() or 
               keyword in task.description.lower() or
               any(keyword in tag.lower() for tag in task.tags)
        ]

    def get_tasks_by_tag(self, tag: str) -> List[Task]:
        """Filter tasks by tag"""
        return [task for task in self.storage.tasks if tag in task.tags]

    def get_overdue_tasks(self) -> List[Task]:
        """Get all overdue tasks"""
        now = datetime.now()
        return [
            task for task in self.storage.tasks
            if task.due_date and task.due_date < now and not task.completed
        ]

    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """Filter tasks by priority"""
        return [task for task in self.storage.tasks if task.priority == priority]