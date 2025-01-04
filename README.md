# TaskMaster CLI

Un gestionnaire de tâches en ligne de commande puissant et flexible, écrit en Python.

## 🌟 Fonctionnalités

- ✅ Gestion complète des tâches (création, modification, suppression)
- 📋 Sous-tâches avec suivi de progression
- 🏷️ Tags avec suggestion automatique
- 📊 Catégories personnalisables avec codes couleur
- 📝 Système de notes attachées aux tâches
- 📅 Dates limites et priorités
- 📈 Statistiques détaillées
- 📜 Historique complet des modifications
- 🔍 Recherche et filtrage avancés
- 📤 Import/Export des données

## 🚀 Installation

```bash
# Cloner le repository
git clone https://github.com/votre-username/taskmaster-cli.git
cd taskmaster-cli

# Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## 💻 Utilisation

Pour lancer l'application :

```bash
python main.py
```

### Menu Principal

1. Ajouter une tâche
2. Afficher toutes les tâches
3. Marquer une tâche comme terminée
4. Supprimer une tâche
5. Ajouter une sous-tâche
6. Rechercher des tâches
7. Filtrer les tâches
8. Exporter les tâches
9. Importer des tâches
10. Afficher les tâches en retard
11. Statistiques
12. Trier les tâches
13. Marquer une sous-tâche comme terminée
14. Voir l'historique d'une tâche
15. Gérer les catégories
16. Gérer les notes
17. Quitter

## 📁 Structure du Projet

```
taskmaster-cli/
├── data/                 # Stockage des données
├── todo_app/            
│   ├── core/            # Modèles et logique métier
│   │   └── auto_tagging/# Système de tags automatiques
│   ├── managers/        # Gestionnaires des opérations
│   ├── storage/         # Gestion du stockage
│   └── ui/              # Interface utilisateur
└── main.py              # Point d'entrée
```

## 🎯 Fonctionnalités Détaillées

### Système de Tags Automatiques
Le système analyse le titre et la description des tâches pour suggérer automatiquement des tags pertinents basés sur des mots-clés prédéfinis.

### Catégories
- Création de catégories avec codes couleur
- Organisation hiérarchique (catégories et sous-catégories)
- Filtrage et tri par catégorie

### Notes
- Ajout de notes détaillées aux tâches
- Historique des modifications
- Visualisation rapide dans la liste des tâches

### Statistiques
- Taux de complétion
- Répartition par priorité
- Tags les plus utilisés
- Analyse des tâches en retard

## 📊 Stockage des Données

Les données sont stockées dans des fichiers JSON dans le dossier `data/` :
- `tasks.json` : Tâches et sous-tâches
- `categories.json` : Catégories
- `notes.json` : Notes
- `history.json` : Historique des modifications

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche (`git checkout -b feature/amazing-feature`)
3. Commit vos changements (`git commit -m 'Add amazing feature'`)
4. Push sur la branche (`git push origin feature/amazing-feature`)
5. Ouvrir une Pull Request

## 📝 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🙏 Remerciements

- Inspiré par les meilleures pratiques de gestion de tâches
- Utilise les principes SOLID et le design pattern MVC
- Interface colorée grâce à ANSI colors