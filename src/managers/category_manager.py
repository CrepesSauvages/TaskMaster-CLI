"""
Gestionnaire des catégories
"""
from typing import List, Optional
from ..core.category import Category
from ..storage.category_storage import CategoryStorage

class CategoryManager:
    def __init__(self):
        self.storage = CategoryStorage()
    
    def add_category(self, name: str, description: str, color: str, parent_id: Optional[int] = None) -> Category:
        """Ajoute une nouvelle catégorie"""
        category_id = len(self.storage.categories) + 1
        category = Category(
            id=category_id,
            name=name,
            description=description,
            color=color,
            parent_id=parent_id
        )
        self.storage.categories.append(category)
        self.storage.save_categories()
        return category
    
    def get_category(self, category_id: int) -> Optional[Category]:
        """Récupère une catégorie par son ID"""
        return next((cat for cat in self.storage.categories if cat.id == category_id), None)
    
    def get_subcategories(self, parent_id: int) -> List[Category]:
        """Récupère les sous-catégories d'une catégorie"""
        return [cat for cat in self.storage.categories if cat.parent_id == parent_id]
    
    def update_category(self, category_id: int, **kwargs) -> bool:
        """Met à jour une catégorie"""
        category = self.get_category(category_id)
        if category:
            for field, value in kwargs.items():
                if hasattr(category, field):
                    setattr(category, field, value)
            self.storage.save_categories()
            return True
        return False
    
    def delete_category(self, category_id: int) -> bool:
        """Supprime une catégorie"""
        category = self.get_category(category_id)
        if category:
            self.storage.categories.remove(category)
            self.storage.save_categories()
            return True
        return False