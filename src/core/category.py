"""
Modèle pour les catégories de tâches
"""
from dataclasses import dataclass
from typing import List

@dataclass
class Category:
    """Représente une catégorie de tâches"""
    id: int
    name: str
    description: str
    color: str  # Code couleur hexadécimal
    parent_id: int = None  # Pour les sous-catégories