"""
Statistiques des tâches
"""
from typing import List
from datetime import datetime
from ..core.task import Task, Priority
from .colors import colorize, Colors, header, info

def calculate_statistics(tasks: List[Task]) -> None:
    """Affiche les statistiques des tâches"""
    if not tasks:
        print(colorize("Aucune tâche à analyser", Colors.WARNING))
        return

    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task.completed)
    completion_rate = (completed_tasks / total_tasks) * 100

    # Statistiques par priorité
    priority_stats = {priority: 0 for priority in Priority}
    for task in tasks:
        priority_stats[task.priority] += 1

    # Tâches en retard
    overdue = sum(1 for task in tasks 
                 if task.due_date and task.due_date < datetime.now() and not task.completed)

    # Affichage
    print(header("\n=== Statistiques des tâches ==="))
    print(info(f"Nombre total de tâches: {total_tasks}"))
    print(info(f"Tâches terminées: {completed_tasks}"))
    print(info(f"Taux de completion: {completion_rate:.1f}%"))
    print(info(f"Tâches en retard: {overdue}"))
    
    print(header("\nRépartition par priorité:"))
    for priority, count in priority_stats.items():
        percentage = (count / total_tasks) * 100
        print(info(f"{priority.value}: {count} ({percentage:.1f}%)"))

    # Tags les plus utilisés
    all_tags = [tag for task in tasks for tag in task.tags]
    if all_tags:
        tag_counts = {}
        for tag in all_tags:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1
        
        print(header("\nTags les plus utilisés:"))
        sorted_tags = sorted(tag_counts.items(), key=lambda x: x[1], reverse=True)
        for tag, count in sorted_tags[:5]:
            print(info(f"{tag}: {count}"))