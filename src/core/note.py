"""
Modèle pour les notes attachées aux tâches
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Note:
    """Représente une note attachée à une tâche"""
    id: int
    task_id: int
    content: str
    created_at: datetime
    updated_at: datetime = None