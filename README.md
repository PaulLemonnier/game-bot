# 🤖 Game Bot

Projet Python permettant d'automatiser des actions au sein d'un jeu vidéo

## Structure du projet

```text
game-bot/
├── .venv/                   # Environnement virtuel Python local
├── src/
│   ├── actions.py           # Actions simples du jeu
│   ├── execution.py         # Lecture et rejouage des mouvements
│   ├── helpers.py           # Chargement et sauvegarde des fichiers JSON
│   ├── listener.py          # Enregistrement des touches ZQSD/E
│   ├── main.py              # Point d'entrée du bot
│   ├── system.py            # Boucle principale et interruptions
│   ├── data/
│   │   └── moves/           # Mouvements enregistrés au format JSON
│   └── game_bot.egg-info/   # Métadonnées générées par l'installation du paquet
├── .gitignore               # Fichiers et dossiers excluits de Git
├── pyproject.toml           # Configuration du paquet et dépendances
└── README.md                # Présentation et documentation du projet
```


## Initialisation du projet

Cloner le dépôt du projet :

```bash
git clone https://github.com/PaulLemonnier/game-bot.git
cd game-bot
```

Créer et activer un environnement virtuel Python :

```bash
python -m venv .venv
source .venv/bin/activate #for Linux
source .venv/Scripts/activate #for Windows
```

Installer les dépendances Python :

```bash
python -m pip install -e .
```
