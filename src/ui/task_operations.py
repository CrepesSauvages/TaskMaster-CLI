"""
Task operation handlers for the CLI interface
"""
from typing import Optional
from ..managers.task_manager import TaskManager

def toggle_task_completion(manager: TaskManager) -> None:
    """Handle toggling task completion status"""
    print("\n=== Marquer une tâche comme terminée ===")
    try:
        task_id = int(input("ID de la tâche: "))
        task = manager.get_task(task_id)
        
        if not task:
            print("Tâche non trouvée")
            return
            
        success = manager.toggle_task(task_id)
        if success:
            status = "terminée" if task.completed else "non terminée"
            print(f"Tâche marquée comme {status}")
        else:
            print("Échec de la mise à jour de la tâche")
            
    except ValueError:
        print("ID invalide")

def toggle_subtask_completion(manager: TaskManager, task_id: Optional[int] = None) -> None:
    """Handle toggling subtask completion status"""
    if task_id is None:
        try:
            task_id = int(input("ID de la tâche principale: "))
        except ValueError:
            print("ID invalide")
            return
            
    task = manager.get_task(task_id)
    if not task:
        print("Tâche principale non trouvée")
        return
        
    if not task.subtasks:
        print("Cette tâche n'a pas de sous-tâches")
        return
        
    print("\nSous-tâches:")
    for subtask in task.subtasks:
        print(subtask)
        
    try:
        subtask_id = int(input("\nID de la sous-tâche: "))
        if manager.toggle_subtask(task_id, subtask_id):
            print("Statut de la sous-tâche mis à jour")
        else:
            print("Sous-tâche non trouvée")
    except ValueError:
        print("ID invalide")