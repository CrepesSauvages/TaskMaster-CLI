"""
Opérations sur les catégories dans l'interface CLI
"""
from typing import Optional
from ..managers.category_manager import CategoryManager
from .colors import Colors, colorize, success, error, warning, info, header

def display_categories(manager: CategoryManager) -> None:
    """Affiche toutes les catégories"""
    categories = manager.storage.categories
    if not categories:
        print(info("Aucune catégorie"))
        return

    for category in categories:
        color = category.color if category.color.startswith('#') else f"#{category.color}"
        parent = manager.get_category(category.parent_id) if category.parent_id else None
        parent_info = f" (Sous-catégorie de: {parent.name})" if parent else ""
        print(colorize(f"{category.id}. {category.name}{parent_info}", color))
        print(colorize(f"   {category.description}", Colors.WHITE))

def manage_categories(manager: CategoryManager) -> None:
    """Gère les opérations sur les catégories"""
    while True:
        print(header("\n=== Gestion des catégories ==="))
        print(colorize("1. Afficher les catégories", Colors.CYAN))
        print(colorize("2. Ajouter une catégorie", Colors.CYAN))
        print(colorize("3. Modifier une catégorie", Colors.CYAN))
        print(colorize("4. Supprimer une catégorie", Colors.CYAN))
        print(colorize("5. Retour", Colors.CYAN))

        choice = input("\nChoisissez une option: ").strip()

        if choice == "1":
            display_categories(manager)
        elif choice == "2":
            add_category(manager)
        elif choice == "3":
            modify_category(manager)
        elif choice == "4":
            delete_category(manager)
        elif choice == "5":
            break
        else:
            print(error("Option invalide"))

def add_category(manager: CategoryManager) -> None:
    """Ajoute une nouvelle catégorie"""
    print(header("\n=== Ajouter une catégorie ==="))
    name = input("Nom: ").strip()
    description = input("Description: ").strip()
    color = input("Couleur (hex, ex: #FF0000): ").strip()
    
    display_categories(manager)
    parent_id_str = input("\nID de la catégorie parente (vide si aucune): ").strip()
    parent_id = int(parent_id_str) if parent_id_str else None

    if name and description and color:
        try:
            category = manager.add_category(name, description, color, parent_id)
            print(success(f"Catégorie '{category.name}' ajoutée avec succès"))
        except Exception as e:
            print(error(f"Erreur lors de l'ajout de la catégorie: {e}"))
    else:
        print(error("Tous les champs sont requis"))

def modify_category(manager: CategoryManager) -> None:
    """Modifie une catégorie existante"""
    print(header("\n=== Modifier une catégorie ==="))
    display_categories(manager)
    
    try:
        category_id = int(input("\nID de la catégorie à modifier: "))
        category = manager.get_category(category_id)
        
        if not category:
            print(error("Catégorie non trouvée"))
            return
            
        name = input(f"Nouveau nom ({category.name}): ").strip() or category.name
        description = input(f"Nouvelle description ({category.description}): ").strip() or category.description
        color = input(f"Nouvelle couleur ({category.color}): ").strip() or category.color
        
        if manager.update_category(category_id, name=name, description=description, color=color):
            print(success("Catégorie mise à jour avec succès"))
        else:
            print(error("Échec de la mise à jour"))
            
    except ValueError:
        print(error("ID invalide"))

def delete_category(manager: CategoryManager) -> None:
    """Supprime une catégorie"""
    print(header("\n=== Supprimer une catégorie ==="))
    display_categories(manager)
    
    try:
        category_id = int(input("\nID de la catégorie à supprimer: "))
        category = manager.get_category(category_id)
        
        if not category:
            print(error("Catégorie non trouvée"))
            return
            
        confirm = input(f"Êtes-vous sûr de vouloir supprimer la catégorie '{category.name}' ? (o/n): ")
        if confirm.lower() == 'o':
            if manager.delete_category(category_id):
                print(success("Catégorie supprimée avec succès"))
            else:
                print(error("Échec de la suppression"))
        else:
            print(info("Suppression annulée"))
            
    except ValueError:
        print(error("ID invalide"))