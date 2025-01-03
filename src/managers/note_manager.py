"""
Gestionnaire des notes
"""
from typing import List, Optional
from datetime import datetime
from ..core.note import Note
from ..storage.note_storage import NoteStorage

class NoteManager:
    def __init__(self):
        self.storage = NoteStorage()
    
    def add_note(self, task_id: int, content: str) -> Note:
        """Ajoute une nouvelle note à une tâche"""
        note_id = len(self.storage.notes) + 1
        note = Note(
            id=note_id,
            task_id=task_id,
            content=content,
            created_at=datetime.now()
        )
        self.storage.notes.append(note)
        self.storage.save_notes()
        return note
    
    def get_task_notes(self, task_id: int) -> List[Note]:
        """Récupère toutes les notes d'une tâche"""
        return [note for note in self.storage.notes if note.task_id == task_id]
    
    def update_note(self, note_id: int, content: str) -> bool:
        """Met à jour une note"""
        note = self.get_note(note_id)
        if note:
            note.content = content
            note.updated_at = datetime.now()
            self.storage.save_notes()
            return True
        return False
    
    def delete_note(self, note_id: int) -> bool:
        """Supprime une note"""
        note = self.get_note(note_id)
        if note:
            self.storage.notes.remove(note)
            self.storage.save_notes()
            return True
        return False
    
    def get_note(self, note_id: int) -> Optional[Note]:
        """Récupère une note par son ID"""
        return next((note for note in self.storage.notes if note.id == note_id), None)