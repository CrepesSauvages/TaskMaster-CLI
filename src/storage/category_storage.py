"""
Stockage des catégories
"""
import json
from typing import List, Optional
from ..core.category import Category
from .file_handler import read_json_file, write_json_file

class CategoryStorage:
    def __init__(self, filename: str = "data/categories.json"):
        self.filename = filename
        self.categories: List[Category] = []
        self.load_categories()
    
    def load_categories(self) -> None:
        """Charge les catégories depuis le fichier"""
        try:
            data = read_json_file(self.filename)
            self.categories = [
                Category(
                    id=cat['id'],
                    name=cat['name'],
                    description=cat['description'],
                    color=cat['color'],
                    parent_id=cat.get('parent_id')
                )
                for cat in data
            ]
        except FileNotFoundError:
            self.categories = []
    
    def save_categories(self) -> None:
        """Sauvegarde les catégories dans le fichier"""
        data = [
            {
                'id': cat.id,
                'name': cat.name,
                'description': cat.description,
                'color': cat.color,
                'parent_id': cat.parent_id
            }
            for cat in self.categories
        ]
        write_json_file(self.filename, data)