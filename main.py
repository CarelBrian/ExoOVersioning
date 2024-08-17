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
        f.write("# ExoOVersioning\n\n"
                "## Description\n"
                "Ce projet contient un programme Python qui trace les courbes des équations x² et x³. "
                "Le projet est conçu pour être exécuté à l'aide de GitHub Actions, "
                "ce qui permet d'automatiser l'exécution des tâches CI/CD.\n\n"
                "## Conception\n"
                "Le programme est structuré de manière modulaire avec des dossiers séparés pour les données, "
                "les modèles, les notebooks, et le code source. "
                "Le fichier `main.py` contient le code principal pour tracer les courbes.\n\n"
                "## Comment faire fonctionner le programme\n"
                "1. Clonez le dépôt sur votre machine locale.\n"
                "2. Installez les dépendances listées dans `requirements.txt`.\n"
                "3. Exécutez `main.py` pour générer les graphiques.\n"
                "4. Poussez les changements sur GitHub pour déclencher GitHub Actions.\n")

    with open(".gitignore", "w") as f:
        f.write("*.pyc\n"
                "__pycache__/\n"
                ".vscode/\n"
                ".DS_Store\n"
                "data/raw/\n"
                "data/cleaned/\n"
                "models/\n"
                "notebooks/\n"
                "reports/\n"
                "plots.png\n")

    with open("Makefile", "w") as f:
        pass

    with open("LICENSE", "w") as f:
        pass

    with open("notebooks/main.ipynb", "w") as f:
        pass

    with open("requirements.txt", "w") as f:
        f.write("matplotlib\n"
                "numpy\n")

    with open("src/utils.py", "w") as f:
        pass

    with open("programme.py", "w") as f:
        f.write("""import matplotlib.pyplot as plt
import numpy as np

def plot_functions():
    x = np.linspace(-10, 10, 400)
    y1 = x ** 2
    y2 = x ** 3

    plt.figure(figsize=(10, 5))

    # Tracer y = x^2
    plt.subplot(1, 2, 1)
    plt.plot(x, y1, label="y = x^2", color='blue')
    plt.title("Graph of y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    # Tracer y = x^3
    plt.subplot(1, 2, 2)
    plt.plot(x, y2, label="y = x^3", color='green')
    plt.title("Graph of y = x^3")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig("plots.png")
    plt.show()

if __name__ == "__main__":
    plot_functions()
""")

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
    "src/utils.py",
    "programme.py"
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
