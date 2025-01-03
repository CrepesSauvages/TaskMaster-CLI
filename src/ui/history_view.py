"""
Affichage de l'historique des modifications
"""
from typing import List
from ..core.history import HistoryEntry
from .colors import Colors, colorize, header, info

def display_task_history(entries: List[HistoryEntry]) -> None:
    """Affiche l'historique des modifications d'une tâche"""
    if not entries:
        print(colorize("Aucun historique disponible", Colors.WARNING))
        return

    print(header("\n=== Historique des modifications ==="))
    
    # Trier les entrées par date
    sorted_entries = sorted(entries, key=lambda x: x.timestamp)
    
    for entry in sorted_entries:
        # Colorer différemment selon le type de changement
        if entry.change_type.name.startswith('COMPLETED'):
            entry_color = Colors.GREEN
        elif entry.change_type.name == 'DELETED':
            entry_color = Colors.FAIL
        elif entry.change_type.name == 'CREATED':
            entry_color = Colors.BLUE
        else:
            entry_color = Colors.CYAN
            
        print(colorize(str(entry), entry_color))