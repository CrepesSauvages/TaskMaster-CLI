"""
Task model and related data structures
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from enum import Enum

class Priority(Enum):
    LOW = "Basse"
    MEDIUM = "Moyenne"
    HIGH = "Haute"

@dataclass
class SubTask:
    """Represents a subtask within a main task"""
    id: int
    title: str
    completed: bool = False

    def __str__(self) -> str:
        status = "✓" if self.completed else " "
        return f"  [{status}] {self.title}"

@dataclass
class Task:
    """Represents a single task in the todo list"""
    id: int
    title: str
    description: str
    created_at: datetime
    tags: List[str]
    priority: Priority
    due_date: Optional[datetime]
    subtasks: List[SubTask]
    completed: bool = False

    def __str__(self) -> str:
        status = "✓" if self.completed else " "
        due = f"(Due: {self.due_date.strftime('%Y-%m-%d')})" if self.due_date else ""
        tags = f"[{', '.join(self.tags)}]" if self.tags else ""
        return f"[{status}] {self.id}. {self.title} - {self.priority.value} {due} {tags}"

    def progress(self) -> float:
        """Calculate progress based on subtasks"""
        if not self.subtasks:
            return 100 if self.completed else 0
        completed = sum(1 for st in self.subtasks if st.completed)
        return (completed / len(self.subtasks)) * 100