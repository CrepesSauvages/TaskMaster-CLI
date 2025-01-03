"""
Stockage de l'historique des modifications
"""
import json
from typing import List
from datetime import datetime
from ..core.history import HistoryEntry, ChangeType

class HistoryStorage:
    def __init__(self, filename: str = "data/history.json"):
        self.filename = filename
        self.entries: List[HistoryEntry] = []
        self.load_history()
    
    def add_entry(self, entry: HistoryEntry) -> None:
        """Ajoute une entrée dans l'historique"""
        self.entries.append(entry)
        self.save_history()
    
    def get_task_history(self, task_id: int) -> List[HistoryEntry]:
        """Récupère l'historique d'une tâche spécifique"""
        return [entry for entry in self.entries if entry.task_id == task_id]
    
    def load_history(self) -> None:
        """Charge l'historique depuis le fichier"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.entries = [
                    HistoryEntry(
                        timestamp=datetime.fromisoformat(entry['timestamp']),
                        task_id=entry['task_id'],
                        change_type=ChangeType[entry['change_type']],
                        field_name=entry.get('field_name'),
                        old_value=entry.get('old_value'),
                        new_value=entry.get('new_value')
                    )
                    for entry in data
                ]
        except FileNotFoundError:
            self.entries = []
    
    def save_history(self) -> None:
        """Sauvegarde l'historique dans le fichier"""
        data = [
            {
                'timestamp': entry.timestamp.isoformat(),
                'task_id': entry.task_id,
                'change_type': entry.change_type.name,
                'field_name': entry.field_name,
                'old_value': entry.old_value,
                'new_value': entry.new_value
            }
            for entry in self.entries
        ]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)