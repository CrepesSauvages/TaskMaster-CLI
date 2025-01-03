"""
Menu-related functionality with colors
"""
from typing import Dict, Tuple, Callable
from .colors import Colors, colorize, header

class Menu:
    def __init__(self):
        self.commands: Dict[str, Tuple[str, Callable]] = {
            '1': ('Ajouter une tâche', None),
            '2': ('Afficher toutes les tâches', None),
            '3': ('Marquer une tâche comme terminée', None),
            '4': ('Supprimer une tâche', None),
            '5': ('Ajouter une sous-tâche', None),
            '6': ('Rechercher des tâches', None),
            '7': ('Filtrer les tâches', None),
            '8': ('Exporter les tâches', None),
            '9': ('Importer des tâches', None),
            '10': ('Afficher les tâches en retard', None),
            '11': ('Statistiques', None),
            '12': ('Trier les tâches', None),
            '13': ('Marquer une sous-tâche comme terminée', None),
            '14': ('Voir l\'historique d\'une tâche', None),
            '15': ('Gérer les catégories', None),
            '16': ('Gérer les notes', None),
            '17': ('Quitter', None)
        }

    def display(self):
        """Display the main menu"""
        print(header("\n=== Todo List ==="))
        for key, (description, _) in self.commands.items():
            print(colorize(f"{key}. {description}", Colors.CYAN))

    def set_command(self, key: str, command: Callable) -> None:
        """Set the callback for a menu item"""
        if key in self.commands:
            description = self.commands[key][0]
            self.commands[key] = (description, command)

    def get_command(self, key: str) -> Callable:
        """Get the callback for a menu item"""
        return self.commands.get(key, (None, None))[1]