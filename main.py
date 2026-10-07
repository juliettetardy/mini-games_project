"""
Réalisation d'une interface de mini-jeux sous Tkinter

Jeux à programmer : 
- Jeu du pendu
- Mastermind

Jeux programmés :
- Space invaders
- Jeu de la vie (fonctionnements manuel et aléatoire)

Commencé le : 18/05/2024
Dernières avancées le : 01/09/2025

Il reste à faire : 
- le retour, après avoir fermé chaque jeu, au menu de choix de jeux
- le fonctionnement et la logique du jeu Mastermind
- le fonctionnement et la logique du jeu du pendu
- l'affichage sur le menu du jeu Mastermind et du jeu du pendu
- l'amélioration visuelle des boutons du jeu Space Invaders
- l'amélioration visuelle de toute l'interface
- le changement de fonctionnement pour le lancement du niveau boss dans Space Invaders
- rajouter d'autres mini-jeux (garçon feu/fille eau, pacman 2D, ...)
"""

# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from display import Display

if __name__ == "__main__" :
    mini_games = Display()