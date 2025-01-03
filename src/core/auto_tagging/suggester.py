"""
Gestionnaire de suggestions de tags
"""
from typing import List, Set
from .analyzer import ContentAnalyzer

class TagSuggester:
    @staticmethod
    def suggest_tags(title: str, description: str, existing_tags: List[str] = None) -> List[str]:
        """Suggère des tags basés sur le contenu et les tags existants"""
        # Obtient les suggestions basées sur le contenu
        content_suggestions = ContentAnalyzer.get_suggested_tags(title, description)
        
        # Si pas de tags existants, retourne les suggestions
        if not existing_tags:
            return content_suggestions
            
        # Convertit en ensembles pour faciliter les opérations
        existing_set = set(existing_tags)
        suggestions_set = set(content_suggestions)
        
        # Ne suggère que les nouveaux tags
        new_suggestions = suggestions_set - existing_set
        
        return sorted(list(new_suggestions))  # Trie les suggestions par ordre alphabétique