"""
Menu-related functionality
"""
from typing import Dict, Tuple, Callable

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
            '11': ('Marquer une sous-tâche comme terminée', None),
            '12': ('Quitter', None)
        }

    def display(self):
        """Display the main menu"""
        print("\n=== Todo List ===")
        for key, (description, _) in self.commands.items():
            print(f"{key}. {description}")

    def set_command(self, key: str, command: Callable) -> None:
        """Set the callback for a menu item"""
        if key in self.commands:
            description = self.commands[key][0]
            self.commands[key] = (description, command)