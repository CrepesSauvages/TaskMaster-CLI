"""
Command-line interface implementation
"""
from datetime import datetime
from typing import List
from ..managers.task_manager import TaskManager
from ..core.task import Task, Priority
from .menu import Menu
from .task_operations import toggle_task_completion, toggle_subtask_completion
from .task_deletion import delete_task_operation

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
        self.menu.set_command('5', self.add_subtask)
        self.menu.set_command('6', self.search_tasks)
        self.menu.set_command('7', self.filter_tasks)
        self.menu.set_command('8', self.export_tasks)
        self.menu.set_command('9', self.import_tasks)
        self.menu.set_command('10', self.show_overdue)

        

    def toggle_task(self):
        """Handle toggling task completion status"""
        self.list_tasks()  # Show current tasks
        toggle_task_completion(self.manager)

    def delete_task(self):
        """Handle task deletion"""
        self.list_tasks()  # Show current tasks
        delete_task_operation(self.manager)    

    def _get_priority_input(self) -> Priority:
        """Get priority input from user"""
        print("\nPriorité:")
        for i, priority in enumerate(Priority, 1):
            print(f"{i}. {priority.value}")
        while True:
            try:
                choice = int(input("Choisissez la priorité (1-3): "))
                if 1 <= choice <= 3:
                    return list(Priority)[choice - 1]
            except ValueError:
                pass
            print("Choix invalide")

    def _get_due_date_input(self) -> datetime:
        """Get due date input from user"""
        while True:
            date_str = input("Date limite (YYYY-MM-DD, vide pour ignorer): ").strip()
            if not date_str:
                return None
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                print("Format de date invalide")

    def _get_tags_input(self) -> List[str]:
        """Get tags input from user"""
        tags_str = input("Tags (séparés par des virgules): ").strip()
        return [tag.strip() for tag in tags_str.split(",") if tag.strip()]

    def add_task(self):
        """Handle adding a new task"""
        print("\n=== Ajouter une tâche ===")
        title = input("Titre: ").strip()
        description = input("Description: ").strip()
        
        if not (title and description):
            print("\nErreur: Le titre et la description sont requis")
            return

        priority = self._get_priority_input()
        due_date = self._get_due_date_input()
        tags = self._get_tags_input()
        
        task = self.manager.add_task(title, description, tags, priority, due_date)
        print(f"\nTâche ajoutée avec succès: {task}")

    def add_subtask(self):
        """Handle adding a subtask"""
        print("\n=== Ajouter une sous-tâche ===")
        self.list_tasks()
        try:
            task_id = int(input("\nID de la tâche principale: "))
            title = input("Titre de la sous-tâche: ").strip()
            
            if self.manager.add_subtask(task_id, title):
                print("Sous-tâche ajoutée")
            else:
                print("Tâche principale non trouvée")
        except ValueError:
            print("ID invalide")

    def list_tasks(self):
        """Display all tasks"""
        print("\n=== Liste des tâches ===")
        tasks = self.manager.get_all_tasks()
        self._display_tasks(tasks)

    def _display_tasks(self, tasks: List[Task]):
        """Helper to display a list of tasks"""
        if not tasks:
            print("Aucune tâche")
            return

        for task in tasks:
            print(task)
            if task.subtasks:
                print("  Sous-tâches:")
                for subtask in task.subtasks:
                    print(f"  {subtask}")
                print(f"  Progression: {task.progress():.1f}%")

    def search_tasks(self):
        """Handle task search"""
        print("\n=== Rechercher des tâches ===")
        keyword = input("Mot-clé: ").strip()
        tasks = self.manager.search_tasks(keyword)
        self._display_tasks(tasks)

    def filter_tasks(self):
        """Handle task filtering"""
        print("\n=== Filtrer les tâches ===")
        print("1. Par tag")
        print("2. Par priorité")
        print("3. Par statut")
        
        choice = input("Choisissez une option: ").strip()
        
        if choice == "1":
            tag = input("Tag: ").strip()
            tasks = self.manager.get_tasks_by_tag(tag)
        elif choice == "2":
            priority = self._get_priority_input()
            tasks = self.manager.get_tasks_by_priority(priority)
        elif choice == "3":
            completed = input("Complétées (o/n)? ").lower() == "o"
            tasks = [t for t in self.manager.get_all_tasks() if t.completed == completed]
        else:
            print("Option invalide")
            return
            
        self._display_tasks(tasks)

    def show_overdue(self):
        """Display overdue tasks"""
        print("\n=== Tâches en retard ===")
        tasks = self.manager.get_overdue_tasks()
        self._display_tasks(tasks)

    def export_tasks(self):
        """Export tasks to a file"""
        print("\n=== Exporter les tâches ===")
        filename = input("Nom du fichier: ").strip()
        if filename:
            self.manager.storage.export_tasks(filename)
            print(f"Tâches exportées vers {filename}")
        else:
            print("Nom de fichier invalide")

    def import_tasks(self):
        """Import tasks from a file"""
        print("\n=== Importer des tâches ===")
        filename = input("Nom du fichier: ").strip()
        if filename:
            try:
                self.manager.storage.import_tasks(filename)
                print("Tâches importées avec succès")
            except Exception as e:
                print(f"Erreur lors de l'importation: {e}")
        else:
            print("Nom de fichier invalide")

    def run(self):
        """Run the CLI application"""
        while True:
            try:
                self.menu.display()
                choice = input("\nChoisissez une option: ").strip()
                
                if choice == '11':
                    print("\nAu revoir!")
                    break
                    
                command = self.menu.commands[choice][1]
                if command:
                    command()
                else:
                    print("Option invalide")
                    
            except Exception as e:
                print(f"Une erreur est survenue: {e}")
                
            input("\nAppuyez sur Entrée pour continuer...")        