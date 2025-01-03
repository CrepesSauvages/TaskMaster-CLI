"""
Analyseur de contenu pour le tagging automatique
"""
from typing import List, Set
from .keywords import TAG_KEYWORDS

class ContentAnalyzer:
    @staticmethod
    def analyze_text(text: str) -> Set[str]:
        """Analyse un texte et retourne les tags appropriés"""
        text = text.lower()
        words = set(text.split())
        
        suggested_tags = set()
        
        # Analyse basée sur les mots-clés
        for tag, keywords in TAG_KEYWORDS.items():
            if any(keyword.lower() in text for keyword in keywords):
                suggested_tags.add(tag)
                
        return suggested_tags

    @staticmethod
    def get_suggested_tags(title: str, description: str) -> List[str]:
        """Obtient les tags suggérés basés sur le titre et la description"""
        # Combine les résultats de l'analyse du titre et de la description
        title_tags = ContentAnalyzer.analyze_text(title)
        desc_tags = ContentAnalyzer.analyze_text(description)
        
        # Fusionne les tags en évitant les doublons
        all_tags = title_tags.union(desc_tags)
        
        return sorted(list(all_tags))  # Trie les tags par ordre alphabétique