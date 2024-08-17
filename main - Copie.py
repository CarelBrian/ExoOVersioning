import os
import subprocess

# Définir premièrement la fonction permettant de créer l'arborescence du projet
def structure_projet():
    structure_projet = [
        "data/cleaned",
        "data/raw",
        "docs",
        "models",
        "notebooks",
        "reports",
        "src"
    ]

    for dir in structure_projet:
        os.makedirs(dir, exist_ok=True)

    with open("README.md", "w") as f:
        pass

    with open("Makefile", "w") as f:
        pass

    with open("LICENSE", "w") as f:
        pass

    with open("notebooks/main.ipynb", "w") as f:
        pass

    with open("requirements.txt", "w") as f:
        pass

    with open("src/utils.py", "w") as f:
        pass

# Création du dépôt git
def initialize_git_repo():
    subprocess.run(["git", "init"])

# Ajouter le dépôt distant
def add_remote_repo():
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/CarelBrian/ExoOVersioning.git"])

# Effectuer un premier commit après ajout de fichier
def add_and_commit_files():
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", "Initial commit"])

# Liste des fichiers à modifier et commiter
files_to_modify_commit = [
    "LICENSE",
    "Makefile",
    "notebooks/main.ipynb",
    "README.md",
    "requirements.txt",
    "src/utils.py"
]

# Modifier, commiter chaque fichier et effectuer un push après chaque commit
def modify_commit_and_push_files():
    for file in files_to_modify_commit:
        with open(file, "a") as f:
            f.write(f"# Modified {file}\n")  # Modifier le fichier file en ajoutant un commentaire
        subprocess.run(["git", "add", file])
        subprocess.run(["git", "commit", "-m", f"Add {file}"])
        push_to_remote()

# Création du dépôt distant sur GitHub via l'API GitHub
def create_remote_repo():
    GITHUB_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')
    if not GITHUB_TOKEN:
        raise ValueError("Le token GitHub n'est pas défini dans l'environnement.")
    
    subprocess.run([
        "curl",
        "-u",
        f"CarelBrian:{GITHUB_TOKEN}",
        "https://api.github.com/user/repos",
        "-d",
        '{"name":"ExoOVersioning"}'
    ])

# Push au dépôt distant
def push_to_remote():
    subprocess.run(["git", "push", "-u", "origin", "master"])

# fonction main pour appeler toutes les fonctions précédentes
if __name__ == "__main__":
    structure_projet()
    initialize_git_repo()
    add_and_commit_files()
    add_remote_repo()  # Ajouter le dépôt distant uniquement une fois
    create_remote_repo()
    push_to_remote()  # Pousser l'initial commit
    modify_commit_and_push_files()
