"""
Task model and related data structures
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    """Represents a single task in the todo list"""
    id: int
    title: str
    description: str
    created_at: datetime
    completed: bool = False

    def __str__(self) -> str:
        status = "✓" if self.completed else " "
        return f"[{status}] {self.id}. {self.title} - {self.description}"