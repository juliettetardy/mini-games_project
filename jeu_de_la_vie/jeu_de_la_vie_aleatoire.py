"""
Jeu de la vie avec génération aléatoire, créé par NewNova88

Ce jeu de la vie est aléatoire (on ne place pas les cellules à la souris).

Néanmoins, afin de ne pas etre limité par le cadre, j'utilise ici
un tableau torique. Cela permet par exemple qu'une structure mouvante partant vers l'extreme
droite se retrouvera à gauche pour continuer son mouvement (idéal pour étudier les planeurs)

On a donc les entrées de la hauteur et de la largeur au début 

Une fois les valeurs entrées, on a donc l'interface qui montre la table avec les cellules mortes et vivantes évoluant dans l'environnement.
On pourra avoir plusieurs résultats comme des structures stables (un carré de 2x2 cellules) ou instables (comme le clignotant ou le planeur,
un peu plus complexe).

Ici, on utilise l'interface intégrée tkinter, parce que dans ce TP/Projet, les librairies externes ne sont pas autorisées. On n'utilisera donc pas
pygame, et de toute façon il ne serait pas très efficace pour le jeu de la vie.

Le programme est commenté et trié, n'utilisant donc pas de variables globales, et utilisant des raccourcis Python mineurs (notamment
pour la création des matrices) afin d'atténuer la longueur du code.

On a en premier les deux importations, puis toutes les définitions des fonctions et procédures, pour enfin finir par le "MAIN", ou juste la partie
principale où l'on trouve les appels de fonctions.
"""

# Importations de tkinter pour l'interface et de random (ici on veut juste randrange) pour l'aléatoire
from tkinter import Tk, Canvas, Button
from random import randrange
import sys, subprocess

def tableau() :
    """ Fonction qui calcule et dessine le nouveau tableau
        Entrée(s): None
        Sortie(s): None
    """
    calculer()
    draw()
    window.after(1, tableau)

def initialisation() :
    """ Fonction qui initialise
        Entrée(s): None
        Sortie(s): None
    """
    for y in range (hauteur) :
        for x in range (largeur) :
            # on met les cellules mortes d'abord, et la variable temporaire à morte aussi.
            state [x] [y] = mort
            temp [x] [y] = mort
            cellule [x] [y] = canvas.create_rectangle ((x*cote, y*cote,(x+1)*cote, (y+1)*cote), outline="gray", fill="white") # création des rectangles blancs

    # On place au hasard environ 25% de cellules en vie (permet d'éviter qu'il n'y aie qu'1 seule cellule, et donc de ne rien produire)
    for i in range (largeur*hauteur//4) :
        state [randrange(largeur)] [randrange(hauteur)] = vivant

def calculer() :
    """ Fonction qui applique les règles du jeu
        Entrée(s): None
        Sortie(s): None
    """
    for y in range (hauteur) :
        for x in range (largeur) :
            nombre_voisins = compte_voisins (x, y) # on appelle la fonction permettant de connaître le nombre de voisins
            
            # Règle 1 - Mort d'isolement
            if state [x][y] == vivant and nombre_voisins < 2 : # Si la cellule est vivante et qu'elle a un nombre de voisins inférieur à deux
                temp [x][y] = mort # alors elle meurt
            
            # Règle 2 - Toute cellule avec 2 ou 3 voisins survit.
            if state [x][y] == vivant and (nombre_voisins == 2 or nombre_voisins == 3) : # Si une cellule est vivante et qu'elle a deux ou trois voisins
                temp [x][y] = vivant # alors elle reste en vie
            
            # Règle 3 - Mort par surpopulation
            if state [x][y] == vivant and nombre_voisins > 3 : # si une cellule est vivante et qu'elle a plus de trois voisins
                temp [x][y] = mort # alors elle meurt
            
            # Règle 4 - Naissance
            if state [x][y] == mort and nombre_voisins == 3 : # si une cellule est morte et qu'elle a trois voisins
                temp [x][y] = vivant # alors elle nait (son état est à vivant)
        
    for y in range (hauteur) :
        for x in range (largeur) :
            state [x][y] = temp [x][y] # l'état prend la valeur de la variable temporaire, définis par les tests des quatre règles ci-dessus

def compte_voisins (x, y) :
    """ Fonction qui compte les voisins en vie (tableau torique, voir plus haut)
        Entrée(s): positions x et y
        Sortie(s): nombre_voisins (int, compteur du nombre de voisins)
    """
    nombre_voisins = 0 # compteur du nombre de voisins à 0

    # on teste si chaque cellule à un voisin selon les 8 directions

    # diagonale haut-gauche
    if state [(x-1)%largeur] [(y+1)%hauteur] == 1 :
        nombre_voisins += 1

    # haut
    if state [x] [(y+1)%hauteur] == 1 :
        nombre_voisins += 1

    # Diagonale haut-droite
    if state [(x+1)%largeur] [(y+1)%hauteur] == 1 :
        nombre_voisins += 1

    # gauche
    if state [(x-1)%largeur] [y] == 1 :
        nombre_voisins += 1

    # droite
    if state [(x+1)%largeur] [y] == 1 :
        nombre_voisins += 1

    # Diagonale bas-gauche
    if state [(x-1)%largeur] [(y-1)%hauteur] == 1 :
        nombre_voisins += 1

    # bas
    if state [x] [(y-1)%hauteur] == 1 :
        nombre_voisins += 1

    # diagonale bas-droite
    if state [(x+1)%largeur] [(y-1)%hauteur] == 1 :
        nombre_voisins += 1
        
    return nombre_voisins # on retourne la valeur du nombre de voisins

def draw() :
    """ Fonction qui dessine toute les cellules
        Entrée(s): None
        Sortie(s): None
    """
    for y in range (hauteur) :
        for x in range (largeur) :
            if state [x][y] == 0 : # si l'état est à 0 (donc cellule morte)
                couleur = "white" # on met la couleur blanche
            else : # sinon elle est vivante
                couleur = "black" # donc on met la couleur noire
            canvas.itemconfig (cellule [x][y], fill = couleur) # application du changement de couleur

def jeu_manuel() :
    """ Fonction qui lance le jeu de la vie avec fonctionnement manuel
        Entrée(s): None
        Sortie(s): None
    """
    window.destroy()
    subprocess.run (["python", "jeu_de_la_vie/jeu_de_la_vie_manuel.py"])

def on_enter() :
    """ Fonction appelée sur le clic de la touche entrée et appelle la fonction jeu_manuel
        Entrée(s): None
        Sortie(s): None
    """
    jeu_manuel()

### ------- MAIN ------- ###

# Définitions des variables
hauteur = int (sys.argv[1]) # Hauteur du tableau (fait donc varier le nombre de cellules à la verticale, plus il y en a, plus c'est lent)
largeur = int (sys.argv[2]) # Largeur du tableau (fait donc varier le nombre de cellules à l'horizontale, plus il y en a, plus c'est lent)
cote = 10  # Taille d'une cellule (fixe, car il ne sert à rien de la modifier)
vivant = 1 # L'état vivant est définit à 1 (comme le binaire, en "True")
mort = 0   # L'état mort est définit à 0 (comme en binaire, en "False")

# Création des matrices
cellule = [[0 for row in range(hauteur)] for col in range(largeur)] # utilisation des raccourcis python (non obligatoire mais pratique)
state = [[mort for row in range(hauteur)] for col in range(largeur)]
temp = [[mort for row in range(hauteur)] for col in range(largeur)]

# Rassemblement des fonctions et procédures pour faire le programme
window = Tk()
window.title ("Jeu de la vie")

width_w = cote*largeur
height_w = cote*hauteur + 40
x = int(1535/2 - width_w/2)
y = int(780/2 - height_w/2)
if y < 0 :
    y = 0
if x < 20 :
    x = -10
window.geometry(f"{width_w}x{height_w}+{x}+{y}") # Définir le placement de la nouvelle fenêtre

canvas = Canvas (window, width = cote*largeur, height = cote*hauteur, highlightthickness = 0)
canvas.pack()

button = Button (window, 
                 text = 'A vous de jouer !', 
                 fg = 'black', bg = 'white', bd = 10, 
                 font = ("Georgia", 10, "bold"),
                 command = jeu_manuel)
button.pack()

# Liaison de la touche Entrée à la fonction on_enter
window.bind('<Return>', lambda event: on_enter)

initialisation()
tableau()

window.mainloop()