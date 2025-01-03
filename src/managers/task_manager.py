"""
Task management business logic
"""
from datetime import datetime
from typing import List, Optional, Tuple
from ..core.task import Task, SubTask, Priority
from ..storage.json_storage import JsonTaskStorage
from .history_manager import HistoryManager
from ..core.history import HistoryEntry, ChangeType
from ..core.auto_tagging.suggester import TagSuggester

class TaskManager:
    def __init__(self):
        self.storage = JsonTaskStorage()
        self.history = HistoryManager()

    def add_task(self, title: str, description: str, tags: List[str], 
                 priority: Priority, due_date: Optional[datetime] = None, category_id: Optional[int] = None) -> Tuple[Task, List[str]]:
        """Add a new task to the list and return suggested tags"""
        suggested_tags = TagSuggester.suggest_tags(title, description, tags)
        
        task_id = len(self.storage.tasks) + 1
        task = Task(
            id=task_id,
            title=title,
            description=description,
            created_at=datetime.now(),
            tags=tags,
            priority=priority,
            due_date=due_date,
            subtasks=[],
            completed=False,
            category_id=category_id  # Change here
        )
        self.storage.tasks.append(task)
        self.storage.save_tasks()
        self.history.log_task_created(task)
        
        return task, suggested_tags

    def get_all_tasks(self) -> List[Task]:
        """Get all tasks"""
        return self.storage.tasks

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a specific task by ID"""
        return next((task for task in self.storage.tasks if task.id == task_id), None)

    def update_task(self, task_id: int, **kwargs) -> bool:
        """Update task fields"""
        task = self.get_task(task_id)
        if not task:
            return False

        for field, new_value in kwargs.items():
            if hasattr(task, field):
                old_value = getattr(task, field)
                setattr(task, field, new_value)
                self.history.log_task_updated(task_id, field, old_value, new_value)

        self.storage.save_tasks()
        return True

    def toggle_task(self, task_id: int) -> bool:
        """Toggle task completion status"""
        task = self.get_task(task_id)
        if task:
            task.completed = not task.completed
            self.storage.save_tasks()
            self.history.log_task_completed(task_id, task.completed)
            return True
        return False

    def add_subtask(self, task_id: int, title: str) -> bool:
        """Add a subtask to a task"""
        task = self.get_task(task_id)
        if task:
            subtask_id = len(task.subtasks) + 1
            subtask = SubTask(id=subtask_id, title=title, completed=False)
            task.subtasks.append(subtask)
            self.storage.save_tasks()
            self.history.log_subtask_change(task_id, title, False)
            return True
        return False

    def toggle_subtask(self, task_id: int, subtask_id: int) -> bool:
        """Toggle subtask completion status"""
        task = self.get_task(task_id)
        if task:
            for subtask in task.subtasks:
                if subtask.id == subtask_id:
                    subtask.completed = not subtask.completed
                    self.storage.save_tasks()
                    self.history.log_subtask_change(task_id, subtask.title, subtask.completed)
                    return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        task = self.get_task(task_id)
        if task:
            self.storage.tasks.remove(task)
            self.storage.save_tasks()
            self.history.log_task_deleted(task_id)
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
        """Get tasks by tag"""
        return [task for task in self.storage.tasks if tag in task.tags]

    def get_tasks_by_priority(self, priority: Priority) -> List[Task]:
        """Get tasks by priority"""
        return [task for task in self.storage.tasks if task.priority == priority]

    def get_overdue_tasks(self) -> List[Task]:
        """Get overdue tasks"""
        now = datetime.now()
        return [
            task for task in self.storage.tasks
            if task.due_date and task.due_date < now and not task.completed
        ]

    def get_task_history(self, task_id: int) -> List[HistoryEntry]:
        """Get task history"""
        return self.history.get_task_history(task_id)