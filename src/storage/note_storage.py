"""
Stockage des notes
"""
import json
from typing import List
from datetime import datetime
from ..core.note import Note
from .file_handler import read_json_file, write_json_file

class NoteStorage:
    def __init__(self, filename: str = "data/notes.json"):
        self.filename = filename
        self.notes: List[Note] = []
        self.load_notes()
    
    def load_notes(self) -> None:
        """Charge les notes depuis le fichier"""
        try:
            data = read_json_file(self.filename)
            self.notes = [
                Note(
                    id=note['id'],
                    task_id=note['task_id'],
                    content=note['content'],
                    created_at=datetime.fromisoformat(note['created_at']),
                    updated_at=datetime.fromisoformat(note['updated_at']) if note.get('updated_at') else None
                )
                for note in data
            ]
        except FileNotFoundError:
            self.notes = []
    
    def save_notes(self) -> None:
        """Sauvegarde les notes dans le fichier"""
        data = [
            {
                'id': note.id,
                'task_id': note.task_id,
                'content': note.content,
                'created_at': note.created_at.isoformat(),
                'updated_at': note.updated_at.isoformat() if note.updated_at else None
            }
            for note in self.notes
        ]
        write_json_file(self.filename, data)