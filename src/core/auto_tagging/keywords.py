from typing import Dict, List

# Catégories de tags avec leurs mots-clés associés
TAG_KEYWORDS: Dict[str, List[str]] = {
    "Dev": [
        "code", "script", "programming", "développement", "dev", "debug", 
        "api", "backend", "frontend", "coding", "logiciel", "algorithme", 
        "framework", "librairie", "repository", "intégration", "versionning", 
        "build", "compilation", "ci/cd", "git", "merge", "pull request", 
        "refactoring", "testing framework", "databases", "json", "xml", 
        "microservices", "architecture", "cloud", "docker", "kubernetes"
    ],
    "Urgent": [
        "urgent", "asap", "deadline", "critique", "important", 
        "immédiat", "prioritaire", "urgence", "à faire maintenant", 
        "impératif", "haute priorité", "retard", "tension", "alerte", 
        "crucial", "dernier délai", "stress", "pression", "solution immédiate"
    ],
    "Bug": [
        "bug", "erreur", "fix", "correction", "problème", "issue", 
        "dysfonctionnement", "défaillance", "anomalie", "plantage", 
        "failles", "crash", "bêta", "régression", "diagnostic", 
        "blocage", "instabilité", "exceptions", "timeout", "stack trace", 
        "crash report", "erreur fatale", "non-réponse", "debugging", 
        "code cassé", "échec"
    ],
    "Documentation": [
        "doc", "documentation", "wiki", "guide", "manuel", "tutoriel", 
        "instructions", "référence", "processus", "procédure", 
        "notes", "article", "glossaire", "exemples", "diagramme", 
        "FAQ", "how-to", "readme", "changelog", "specifications", 
        "documentation API", "manuel utilisateur", "best practices", 
        "diagrammes UML", "annotations"
    ],
    "Design": [
        "design", "ui", "ux", "interface", "maquette", "prototype", 
        "graphisme", "visuel", "layout", "conception", "style", 
        "typographie", "illustration", "branding", "palette", "wireframe", 
        "modèle", "animation", "icônes", "interaction", "accessibilité", 
        "mockup", "composants UI", "schémas", "personas", "responsive"
    ],
    "Test": [
        "test", "testing", "qa", "qualité", "validation", "vérification", 
        "évaluation", "expérimentation", "contrôle", "essai", 
        "automatisation", "test unitaire", "performance", "scénarios", 
        "acceptation", "tests manuels", "stress test", "load test", 
        "intégration continue", "tests fonctionnels", "tests de sécurité", 
        "assertions", "benchmarks", "bugs trouvés", "retours QA"
    ],
    "Maintenance": [
        "maintenance", "mise à jour", "update", "upgrade", "clean", 
        "entretien", "réparation", "optimisation", "support", "sauvegarde", 
        "monitoring", "correctif", "nettoyage", "configuration", 
        "tâche planifiée", "logs", "recovery", "patch", "audit", 
        "serveur", "analyse système", "monitoring continu", "dépannage"
    ],
    "Devoir": [
        "devoir", "exercice", "dm", "tp", "cours", "école", "université", 
        "travail", "études", "projet scolaire", "enseignement", 
        "devoir maison", "révision", "examen", "apprentissage", "recherche", 
        "formation", "sujet", "thème", "présentation", "mémoire", 
        "livrable", "exposé", "pratique", "dossier", "contenu éducatif"
    ],
    "Meeting": [
        "réunion", "meeting", "rendez-vous", "call", "visio", 
        "conférence", "discussion", "session", "entretien", "brainstorming", 
        "planning", "présentation", "agenda", "décision", "stand-up", 
        "atelier", "webinaire", "table ronde", "kickoff", "bilan", 
        "briefing", "compte-rendu", "suivi", "coordination", "préparation"
    ],
    "Feature": [
        "feature", "fonctionnalité", "amélioration", "enhancement", 
        "nouveauté", "option", "ajout", "innovation", "outil", "module", 
        "extension", "mise à jour", "configuration", "prototype", "plugin", 
        "personnalisation", "widget", "implémentation", "optimisation", 
        "idée", "spécifications", "module complémentaire", "nouvelle version"
    ],
}
