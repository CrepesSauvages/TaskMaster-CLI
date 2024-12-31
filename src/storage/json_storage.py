"""
JSON-based storage implementation
"""
import json
from datetime import datetime
from typing import List
from ..core.task import Task

class JsonTaskStorage:
    def __init__(self, filename: str = "data/tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from the JSON file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [
                    Task(
                        id=task['id'],
                        title=task['title'],
                        description=task['description'],
                        created_at=datetime.fromisoformat(task['created_at']),
                        completed=task['completed']
                    )
                    for task in data
                ]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self) -> None:
        """Save tasks to the JSON file"""
        # Ensure the data directory exists
        import os
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        
        data = [
            {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'created_at': task.created_at.isoformat(),
                'completed': task.completed
            }
            for task in self.tasks
        ]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)