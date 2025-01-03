"""
Gestionnaire de l'historique des modifications
"""
from datetime import datetime
from typing import Any, Optional
from ..core.history import HistoryEntry, ChangeType
from ..storage.history_storage import HistoryStorage
from ..core.task import Task

class HistoryManager:
    def __init__(self):
        self.storage = HistoryStorage()
    
    def log_task_created(self, task: Task) -> None:
        """Enregistre la création d'une tâche"""
        self.storage.add_entry(HistoryEntry(
            timestamp=datetime.now(),
            task_id=task.id,
            change_type=ChangeType.CREATED
        ))
    
    def log_task_updated(self, task_id: int, field: str, old_value: Any, new_value: Any) -> None:
        """Enregistre la modification d'un champ d'une tâche"""
        self.storage.add_entry(HistoryEntry(
            timestamp=datetime.now(),
            task_id=task_id,
            change_type=ChangeType.UPDATED,
            field_name=field,
            old_value=old_value,
            new_value=new_value
        ))
    
    def log_task_completed(self, task_id: int, completed: bool) -> None:
        """Enregistre le changement de statut d'une tâche"""
        self.storage.add_entry(HistoryEntry(
            timestamp=datetime.now(),
            task_id=task_id,
            change_type=ChangeType.COMPLETED if completed else ChangeType.UNCOMPLETED
        ))
    
    def log_task_deleted(self, task_id: int) -> None:
        """Enregistre la suppression d'une tâche"""
        self.storage.add_entry(HistoryEntry(
            timestamp=datetime.now(),
            task_id=task_id,
            change_type=ChangeType.DELETED
        ))
    
    def log_subtask_change(self, task_id: int, subtask_title: str, completed: bool) -> None:
        """Enregistre les changements de sous-tâches"""
        change_type = ChangeType.SUBTASK_COMPLETED if completed else ChangeType.SUBTASK_UNCOMPLETED
        self.storage.add_entry(HistoryEntry(
            timestamp=datetime.now(),
            task_id=task_id,
            change_type=change_type,
            field_name="subtask",
            new_value=subtask_title
        ))
    
    def get_task_history(self, task_id: int) -> list[HistoryEntry]:
        """Récupère l'historique d'une tâche"""
        return self.storage.get_task_history(task_id)