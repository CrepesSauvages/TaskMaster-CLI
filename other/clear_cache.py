import os
import shutil

def supprimer_pycache(dossier):
    for racine, dirs, fichiers in os.walk(dossier):
        for dir_name in dirs:
            if dir_name == '__pycache__':
                chemin = os.path.join(racine, dir_name)
                shutil.rmtree(chemin)
                print(f'Supprimé : {chemin}')

if __name__ == "__main__":
    dossier_cible = os.path.dirname(os.path.abspath(__file__))
    supprimer_pycache(dossier_cible)