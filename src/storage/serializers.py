"""
Serialization utilities for converting between Task objects and dictionaries
"""
from typing import Dict, Any, List
from ..core.task import Task, SubTask, Priority
from datetime import datetime

def task_to_dict(task: Task) -> Dict[str, Any]:
    """Convert a Task object to a dictionary"""
    return {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'created_at': task.created_at.isoformat(),
        'tags': task.tags,
        'priority': task.priority.name,
        'due_date': task.due_date.isoformat() if task.due_date else None,
        'completed': task.completed,
        'subtasks': [subtask_to_dict(st) for st in task.subtasks]
    }

def subtask_to_dict(subtask: SubTask) -> Dict[str, Any]:
    """Convert a SubTask object to a dictionary"""
    return {
        'id': subtask.id,
        'title': subtask.title,
        'completed': subtask.completed
    }

def dict_to_task(data: Dict[str, Any]) -> Task:
    """Convert a dictionary to a Task object"""
    return Task(
        id=data['id'],
        title=data['title'],
        description=data['description'],
        created_at=datetime.fromisoformat(data['created_at']),
        tags=data.get('tags', []),
        priority=Priority[data.get('priority', 'MEDIUM')],
        due_date=datetime.fromisoformat(data['due_date']) if data.get('due_date') else None,
        completed=data['completed'],
        subtasks=[dict_to_subtask(st) for st in data.get('subtasks', [])]
    )

def dict_to_subtask(data: Dict[str, Any]) -> SubTask:
    """Convert a dictionary to a SubTask object"""
    return SubTask(
        id=data['id'],
        title=data['title'],
        completed=data['completed']
    )