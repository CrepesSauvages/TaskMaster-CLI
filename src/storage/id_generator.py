"""
Utilities for managing task IDs
"""
from typing import List
from ..core.task import Task

def generate_next_id(existing_tasks: List[Task]) -> int:
    """Generate the next available task ID"""
    return max((task.id for task in existing_tasks), default=0) + 1

def adjust_imported_ids(existing_tasks: List[Task], imported_tasks: List[Task]) -> List[Task]:
    """Adjust IDs of imported tasks to avoid conflicts"""
    max_id = max((task.id for task in existing_tasks), default=0)
    for task in imported_tasks:
        max_id += 1
        task.id = max_id
    return imported_tasks