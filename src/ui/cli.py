"""
Command-line interface implementation
"""
from ..managers.task_manager import TaskManager
from .menu import Menu

class TodoCLI:
    def __init__(self):
        self.manager = TaskManager()
        self.menu = Menu()
        self._setup_commands()

    def _setup_commands(self):
        """Set up menu command callbacks"""
        self.menu.set_command('1', self.add_task)
        self.menu.set_command('2', self.list_tasks)
        self.menu.set_command('3', self.toggle_task)
        self.menu.set_command('4', self.delete_task)

    def add_task(self):
        """Handle adding a new task"""
        print("\n=== Ajouter une tâche ===")
        title = input("Titre: ").strip()
        description = input("Description: ").strip()
        
        if title and description:
            task = self.manager.add_task(title, description)
            print(f"\nTâche ajoutée avec succès: {task}")
        else:
            print("\nErreur: Le titre et la description sont requis")

    def list_tasks(self):
        """Display all tasks"""
        print("\n=== Liste des tâches ===")
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("Aucune tâche")
            return

        for task in tasks:
            print(task)

    def toggle_task(self):
        """Handle toggling a task's completion status"""
        print("\n=== Marquer une tâche comme terminée ===")
        self.list_tasks()
        try:
            task_id = int(input("\nEntrez l'ID de la tâche: "))
            if self.manager.toggle_task(task_id):
                print("Statut de la tâche mis à jour")
            else:
                print("Tâche non trouvée")
        except ValueError:
            print("ID invalide")

    def delete_task(self):
        """Handle deleting a task"""
        print("\n=== Supprimer une tâche ===")
        self.list_tasks()
        try:
            task_id = int(input("\nEntrez l'ID de la tâche à supprimer: "))
            if self.manager.delete_task(task_id):
                print("Tâche supprimée")
            else:
                print("Tâche non trouvée")
        except ValueError:
            print("ID invalide")

    def run(self):
        """Main application loop"""
        while True:
            self.menu.display()
            choice = input("\nChoisissez une option: ").strip()
            
            if choice not in self.menu.commands:
                print("Option invalide")
                continue
                
            if choice == '5':
                print("Au revoir!")
                break
                
            command = self.menu.commands[choice][1]
            if command:
                command()