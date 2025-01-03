"""
Formatage de l'affichage des tâches
"""
from datetime import datetime
from typing import List
from ..core.task import Task
from .colors import Colors, colorize, success, warning

def format_task(task: Task) -> str:
    """Formate l'affichage d'une tâche"""
    status = "✓" if task.completed else "✗"
    status_color = Colors.GREEN if task.completed else Colors.FAIL
    
    # Formatage de base
    base = f"[{colorize(status, status_color)}] {task.id}. {colorize(task.title, Colors.BOLD)}"
    
    # Priorité
    priority_colors = {
        'HIGH': Colors.FAIL,
        'MEDIUM': Colors.WARNING,
        'LOW': Colors.GREEN
    }
    priority = colorize(task.priority.value, priority_colors[task.priority.name])
    
    # Date d'échéance
    due = ""
    if task.due_date:
        days_left = (task.due_date - datetime.now()).days
        if days_left < 0:
            due = colorize(f"(En retard de {abs(days_left)} jours)", Colors.FAIL)
        elif days_left == 0:
            due = warning("(Dû aujourd'hui)")
        else:
            due = info(f"(Dans {days_left} jours)")
    
    # Tags
    tags = f"[{', '.join(colorize(tag, Colors.CYAN) for tag in task.tags)}]" if task.tags else ""
    
    return f"{base} - {priority} {due} {tags}"

def format_subtask(subtask: str, indent: int = 2) -> str:
    """Formate l'affichage d'une sous-tâche"""
    status = "✓" if subtask.completed else "✗"
    status_color = Colors.GREEN if subtask.completed else Colors.FAIL
    return f"{' ' * indent}[{colorize(status, status_color)}] {subtask.title}"