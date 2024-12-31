"""
Task deletion operations for the CLI interface
"""
from ..managers.task_manager import TaskManager

def delete_task_operation(manager: TaskManager) -> None:
    """Handle task deletion"""
    print("\n=== Supprimer une tâche ===")
    try:
        task_id = int(input("ID de la tâche à supprimer: "))
        task = manager.get_task(task_id)
        
        if not task:
            print("Tâche non trouvée")
            return
            
        confirm = input(f"Êtes-vous sûr de vouloir supprimer la tâche '{task.title}' ? (o/n): ")
        if confirm.lower() == 'o':
            if manager.delete_task(task_id):
                print("Tâche supprimée avec succès")
            else:
                print("Échec de la suppression de la tâche")
        else:
            print("Suppression annulée")
            
    except ValueError:
        print("ID invalide")