"""
Command-line interface implementation
"""
from datetime import datetime
from typing import List, Optional
from ..managers.task_manager import TaskManager
from ..managers.category_manager import CategoryManager
from ..managers.note_manager import NoteManager
from ..core.task import Task, Priority
from .menu import Menu
from .colors import Colors, colorize, success, error, warning, info, header
from .task_operations import toggle_task_completion, toggle_subtask_completion
from .task_deletion import delete_task_operation
from .formatters import format_task, format_subtask
from .statistics import calculate_statistics
from .history_view import display_task_history
from .category_operations import manage_categories
from .note_operations import manage_notes

class TodoCLI:
    def __init__(self):
        self.task_manager = TaskManager()
        self.category_manager = CategoryManager()
        self.note_manager = NoteManager()
        self.menu = Menu()
        self._setup_commands()

    def _setup_commands(self):
        """Configuration des commandes du menu"""
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
        self.menu.set_command('11', self.show_statistics)
        self.menu.set_command('12', self.sort_tasks)
        self.menu.set_command('13', self.toggle_subtask)
        self.menu.set_command('14', self.show_task_history)
        self.menu.set_command('15', self.manage_categories)
        self.menu.set_command('16', self.manage_notes)
        self.menu.set_command('17', None)

    def _get_priority_input(self) -> Priority:
        """Obtenir la priorité depuis l'entrée utilisateur"""
        print(info("\nPriorité:"))
        for i, priority in enumerate(Priority, 1):
            print(colorize(f"{i}. {priority.value}", Colors.CYAN))
        while True:
            try:
                choice = int(input("Choisissez la priorité (1-3): "))
                if 1 <= choice <= 3:
                    return list(Priority)[choice - 1]
            except ValueError:
                pass
            print(error("Choix invalide"))

    def _get_due_date_input(self) -> Optional[datetime]:
        """Obtenir la date limite depuis l'entrée utilisateur"""
        while True:
            date_str = input("Date limite (YYYY-MM-DD, vide pour ignorer): ").strip()
            if not date_str:
                return None
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                print(error("Format de date invalide"))

    def _get_tags_input(self) -> List[str]:
        """Obtenir les tags depuis l'entrée utilisateur"""
        tags_str = input("Tags (séparés par des virgules): ").strip()
        return [tag.strip() for tag in tags_str.split(",") if tag.strip()]

    def _get_category_input(self) -> Optional[int]:
        """Obtenir la catégorie depuis l'entrée utilisateur"""
        print(info("\nCatégories disponibles:"))
        categories = self.category_manager.storage.categories
        if not categories:
            print(warning("Aucune catégorie disponible"))
            return None

        for category in categories:
            print(colorize(f"{category.id}. {category.name}", category.color))

        category_id_str = input("\nID de la catégorie (vide pour ignorer): ").strip()
        if not category_id_str:
            return None

        try:
            category_id = int(category_id_str)
            if self.category_manager.get_category(category_id):
                return category_id
            print(error("Catégorie non trouvée"))
        except ValueError:
            print(error("ID invalide"))
        return None

    def add_task(self):
        """Ajouter une nouvelle tâche"""
        print(header("\n=== Ajouter une tâche ==="))
        title = input("Titre: ").strip()
        description = input("Description: ").strip()
        
        if not (title and description):
            print(error("\nErreur: Le titre et la description sont requis"))
            return

        priority = self._get_priority_input()
        due_date = self._get_due_date_input()
        tags = self._get_tags_input()
        category_id = self._get_category_input()
        
        task, suggested_tags = self.task_manager.add_task(
            title=title,
            description=description,
            tags=tags,
            priority=priority,
            due_date=due_date,
            category_id=category_id
        )
        
        print(success(f"\nTâche ajoutée avec succès: {format_task(task)}"))
        
        if suggested_tags:
            print(info("\nTags suggérés basés sur le contenu:"))
            for tag in suggested_tags:
                print(colorize(f"  - {tag}", Colors.CYAN))
            
            if input("\nVoulez-vous ajouter ces tags? (o/n): ").lower() == 'o':
                task.tags.extend(suggested_tags)
                self.task_manager.storage.save_tasks()
                print(success("Tags ajoutés avec succès!"))
                print(info(f"Tags finaux: {', '.join(task.tags)}"))

    def list_tasks(self):
        """Afficher toutes les tâches"""
        print(header("\n=== Liste des tâches ==="))
        tasks = self.task_manager.get_all_tasks()
        self._display_tasks(tasks)

    def _display_tasks(self, tasks: List[Task]):
        """Afficher une liste de tâches"""
        if not tasks:
            print(warning("Aucune tâche"))
            return

        for task in tasks:
            print(format_task(task))
            
            # Afficher la catégorie si elle existe
            if task.category_id:
                category = self.category_manager.get_category(task.category_id)
                if category:
                    print(colorize(f"  Catégorie: {category.name}", category.color))
            
            # Afficher les sous-tâches
            if task.subtasks:
                print(info("  Sous-tâches:"))
                for subtask in task.subtasks:
                    print(format_subtask(subtask))
                print(info(f"  Progression: {task.progress():.1f}%"))
            
            # Afficher les notes
            notes = self.note_manager.get_task_notes(task.id)
            if notes:
                print(info("  Notes:"))
                for note in notes:
                    print(colorize(f"    - {note.content[:50]}...", Colors.WHITE))

    def toggle_task(self):
        """Basculer l'état d'une tâche"""
        self.list_tasks()
        toggle_task_completion(self.task_manager)

    def delete_task(self):
        """Supprimer une tâche"""
        self.list_tasks()
        delete_task_operation(self.task_manager)

    def add_subtask(self):
        """Ajouter une sous-tâche"""
        print(header("\n=== Ajouter une sous-tâche ==="))
        self.list_tasks()
        try:
            task_id = int(input("\nID de la tâche principale: "))
            title = input("Titre de la sous-tâche: ").strip()
            
            if self.task_manager.add_subtask(task_id, title):
                print(success("Sous-tâche ajoutée"))
            else:
                print(error("Tâche principale non trouvée"))
        except ValueError:
            print(error("ID invalide"))

    def toggle_subtask(self):
        """Basculer l'état d'une sous-tâche"""
        self.list_tasks()
        toggle_subtask_completion(self.task_manager)

    def search_tasks(self):
        """Rechercher des tâches"""
        print(header("\n=== Rechercher des tâches ==="))
        keyword = input("Mot-clé: ").strip()
        tasks = self.task_manager.search_tasks(keyword)
        self._display_tasks(tasks)

    def filter_tasks(self):
        """Filtrer les tâches"""
        print(header("\n=== Filtrer les tâches ==="))
        print(colorize("1. Par tag", Colors.CYAN))
        print(colorize("2. Par priorité", Colors.CYAN))
        print(colorize("3. Par statut", Colors.CYAN))
        print(colorize("4. Par catégorie", Colors.CYAN))
        
        choice = input("\nChoisissez une option: ").strip()
        
        if choice == "1":
            tag = input("Tag: ").strip()
            tasks = self.task_manager.get_tasks_by_tag(tag)
        elif choice == "2":
            priority = self._get_priority_input()
            tasks = self.task_manager.get_tasks_by_priority(priority)
        elif choice == "3":
            completed = input("Complétées (o/n)? ").lower() == "o"
            tasks = [t for t in self.task_manager.get_all_tasks() if t.completed == completed]
        elif choice == "4":
            category_id = self._get_category_input()
            if category_id:
                tasks = [t for t in self.task_manager.get_all_tasks() if t.category_id == category_id]
            else:
                print(error("Catégorie invalide"))
                return
        else:
            print(error("Option invalide"))
            return
            
        self._display_tasks(tasks)

    def show_overdue(self):
        """Afficher les tâches en retard"""
        print(header("\n=== Tâches en retard ==="))
        tasks = self.task_manager.get_overdue_tasks()
        self._display_tasks(tasks)

    def show_statistics(self):
        """Afficher les statistiques"""
        calculate_statistics(self.task_manager.get_all_tasks())

    def sort_tasks(self):
        """Trier et afficher les tâches"""
        print(header("\n=== Trier les tâches ==="))
        print(colorize("1. Par date de création", Colors.CYAN))
        print(colorize("2. Par priorité", Colors.CYAN))
        print(colorize("3. Par statut", Colors.CYAN))
        print(colorize("4. Par catégorie", Colors.CYAN))
        
        choice = input("\nChoisissez une option: ").strip()
        tasks = self.task_manager.get_all_tasks()
        
        if choice == "1":
            tasks.sort(key=lambda x: x.created_at)
        elif choice == "2":
            tasks.sort(key=lambda x: x.priority.value)
        elif choice == "3":
            tasks.sort(key=lambda x: x.completed)
        elif choice == "4":
            tasks.sort(key=lambda x: (x.category_id or float('inf')))
        else:
            print(error("Option invalide"))
            return
            
        print(header("\n=== Tâches triées ==="))
        self._display_tasks(tasks)

    def show_task_history(self):
        """Afficher l'historique d'une tâche"""
        self.list_tasks()
        try:
            task_id = int(input("\nID de la tâche: "))
            history = self.task_manager.get_task_history(task_id)
            display_task_history(history)
        except ValueError:
            print(error("ID invalide"))

    def export_tasks(self):
        """Exporter les tâches"""
        print(header("\n=== Exporter les tâches ==="))
        filename = input("Nom du fichier: ").strip()
        if filename:
            try:
                self.task_manager.storage.export_tasks(filename)
                print(success(f"Tâches exportées vers {filename}"))
            except Exception as e:
                print(error(f"Erreur lors de l'exportation: {e}"))
        else:
            print(error("Nom de fichier invalide"))

    def import_tasks(self):
        """Importer des tâches"""
        print(header("\n=== Importer des tâches ==="))
        filename = input("Nom du fichier: ").strip()
        if filename:
            try:
                self.task_manager.storage.import_tasks(filename)
                print(success("Tâches importées avec succès"))
            except Exception as e:
                print(error(f"Erreur lors de l'importation: {e}"))
        else:
            print(error("Nom de fichier invalide"))

    def manage_categories(self):
        """Gérer les catégories"""
        manage_categories(self.category_manager)

    def manage_notes(self):
        """Gérer les notes"""
        manage_notes(self.task_manager, self.note_manager)

    def run(self):
        """Exécuter l'application"""
        while True:
            try:
                self.menu.display()
                choice = input("\nChoisissez une option: ").strip()
                
                if choice == '17':
                    print(info("\nAu revoir!"))
                    break
                    
                command = self.menu.get_command(choice)
                if command:
                    command()
                else:
                    print(error("Option invalide"))
                    
            except Exception as e:
                print(error(f"Une erreur est survenue: {e}"))
                
            input("\nAppuyez sur Entrée pour continuer...")