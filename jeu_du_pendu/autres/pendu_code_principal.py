"""
Tardy Juliette et Curie Justine

TP 3 CS-DEV - Création du jeu du pendu version console et version graphique.

Réalisé le 06/10/2023
   
Il reste à coder la version graphique.

"""

from random import choice
from jeu_du_pendu import choice_letter

words_list = ['avion', 'plage', 'table', 'ville',
              'girafe', 'jardin', 'papier', 'pirate', 'python', 'requin', 'souris',
              'poisson', 'bonhomme', 'bracelet', 'ordinateur', 'ordonnance'
              'anticonstitutionnellement']

random_word = choice(words_list) # Choisis aléatoirement un mot dans liste
choice_letter(random_word)
