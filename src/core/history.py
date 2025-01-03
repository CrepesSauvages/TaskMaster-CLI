"""
Modèles pour l'historique des modifications
"""
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Optional

class ChangeType(Enum):
    CREATED = "création"
    UPDATED = "modification"
    COMPLETED = "terminée"
    UNCOMPLETED = "réouverte"
    DELETED = "suppression"
    SUBTASK_ADDED = "sous-tâche ajoutée"
    SUBTASK_COMPLETED = "sous-tâche terminée"
    SUBTASK_UNCOMPLETED = "sous-tâche réouverte"

@dataclass
class HistoryEntry:
    """Représente une entrée dans l'historique des modifications"""
    timestamp: datetime
    task_id: int
    change_type: ChangeType
    field_name: Optional[str] = None
    old_value: Optional[Any] = None
    new_value: Optional[Any] = None
    
    def __str__(self) -> str:
        if self.field_name:
            return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] Tâche #{self.task_id}: {self.change_type.value} - {self.field_name} changé de '{self.old_value}' à '{self.new_value}'"
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M')}] Tâche #{self.task_id}: {self.change_type.value}"