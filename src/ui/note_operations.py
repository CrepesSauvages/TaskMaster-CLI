"""
Opérations sur les notes dans l'interface CLI
"""
from typing import Optional
from ..managers.note_manager import NoteManager
from ..managers.task_manager import TaskManager
from .colors import Colors, colorize, success, error, info, header
from .formatters import format_task

def display_task_notes(note_manager: NoteManager, task_id: int) -> None:
    """Affiche toutes les notes d'une tâche"""
    notes = note_manager.get_task_notes(task_id)
    if not notes:
        print(info("Aucune note"))
        return

    for note in notes:
        updated = f" (Modifiée le {note.updated_at.strftime('%Y-%m-%d %H:%M')})" if note.updated_at else ""
        print(colorize(f"\nNote #{note.id} - {note.created_at.strftime('%Y-%m-%d %H:%M')}{updated}", Colors.CYAN))
        print(note.content)

def manage_notes(task_manager: TaskManager, note_manager: NoteManager) -> None:
    """Gère les opérations sur les notes"""
    while True:
        print(header("\n=== Gestion des notes ==="))
        print(colorize("1. Afficher les notes d'une tâche", Colors.CYAN))
        print(colorize("2. Ajouter une note", Colors.CYAN))
        print(colorize("3. Modifier une note", Colors.CYAN))
        print(colorize("4. Supprimer une note", Colors.CYAN))
        print(colorize("5. Retour", Colors.CYAN))

        choice = input("\nChoisissez une option: ").strip()

        if choice == "1":
            display_notes(task_manager, note_manager)
        elif choice == "2":
            add_note(task_manager, note_manager)
        elif choice == "3":
            modify_note(task_manager, note_manager)
        elif choice == "4":
            delete_note(task_manager, note_manager)
        elif choice == "5":
            break
        else:
            print(error("Option invalide"))

def display_notes(task_manager: TaskManager, note_manager: NoteManager) -> None:
    """Affiche les notes d'une tâche"""
    print(header("\n=== Notes d'une tâche ==="))
    tasks = task_manager.get_all_tasks()
    for task in tasks:
        print(format_task(task))
    
    try:
        task_id = int(input("\nID de la tâche: "))
        task = task_manager.get_task(task_id)
        
        if not task:
            print(error("Tâche non trouvée"))
            return
            
        print(header(f"\nNotes pour la tâche: {task.title}"))
        display_task_notes(note_manager, task_id)
        
    except ValueError:
        print(error("ID invalide"))

def add_note(task_manager: TaskManager, note_manager: NoteManager) -> None:
    """Ajoute une nouvelle note"""
    print(header("\n=== Ajouter une note ==="))
    tasks = task_manager.get_all_tasks()
    for task in tasks:
        print(format_task(task))
    
    try:
        task_id = int(input("\nID de la tâche: "))
        task = task_manager.get_task(task_id)
        
        if not task:
            print(error("Tâche non trouvée"))
            return
            
        print(info(f"\nAjout d'une note pour: {task.title}"))
        content = input("Contenu de la note: ").strip()
        
        if content:
            note = note_manager.add_note(task_id, content)
            print(success("Note ajoutée avec succès"))
        else:
            print(error("Le contenu ne peut pas être vide"))
            
    except ValueError:
        print(error("ID invalide"))

def modify_note(task_manager: TaskManager, note_manager: NoteManager) -> None:
    """Modifie une note existante"""
    print(header("\n=== Modifier une note ==="))
    tasks = task_manager.get_all_tasks()
    for task in tasks:
        print(format_task(task))
    
    try:
        task_id = int(input("\nID de la tâche: "))
        task = task_manager.get_task(task_id)
        
        if not task:
            print(error("Tâche non trouvée"))
            return
            
        print(header(f"\nNotes pour la tâche: {task.title}"))
        display_task_notes(note_manager, task_id)
        
        note_id = int(input("\nID de la note à modifier: "))
        note = note_manager.get_note(note_id)
        
        if not note or note.task_id != task_id:
            print(error("Note non trouvée"))
            return
            
        content = input(f"Nouveau contenu:\n{note.content}\n> ").strip()
        
        if content:
            if note_manager.update_note(note_id, content):
                print(success("Note mise à jour avec succès"))
            else:
                print(error("Échec de la mise à jour"))
        else:
            print(error("Le contenu ne peut pas être vide"))
            
    except ValueError:
        print(error("ID invalide"))

def delete_note(task_manager: TaskManager, note_manager: NoteManager) -> None:
    """Supprime une note"""
    print(header("\n=== Supprimer une note ==="))
    tasks = task_manager.get_all_tasks()
    for task in tasks:
        print(format_task(task))
    
    try:
        task_id = int(input("\nID de la tâche: "))
        task = task_manager.get_task(task_id)
        
        if not task:
            print(error("Tâche non trouvée"))
            return
            
        print(header(f"\nNotes pour la tâche: {task.title}"))
        display_task_notes(note_manager, task_id)
        
        note_id = int(input("\nID de la note à supprimer: "))
        note = note_manager.get_note(note_id)
        
        if not note or note.task_id != task_id:
            print(error("Note non trouvée"))
            return
            
        confirm = input("Êtes-vous sûr de vouloir supprimer cette note ? (o/n): ")
        if confirm.lower() == 'o':
            if note_manager.delete_note(note_id):
                print(success("Note supprimée avec succès"))
            else:
                print(error("Échec de la suppression"))
        else:
            print(info("Suppression annulée"))
            
    except ValueError:
        print(error("ID invalide"))