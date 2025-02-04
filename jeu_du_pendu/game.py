# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import Tk, Canvas, CENTER
from random import choice
from PIL import Image, ImageTk

def new_word() :
    """ Fonction qui cherche un nouveau mot dans le fichier txt et le renvoie
        Entrée(s): None
        Sortie(s): word (str)
    """
    with open('jeu_du_pendu/liste_de_mots_fr.txt', 'r', encoding = 'utf-8') as fichier : # 'r' signifie read only
        words_list = fichier.readlines()    

    word = choice(words_list) # choisis un mot aléatoirement dans la liste créée grâce au fichier
    word = word[:-1] # enlève le dernier caractère \n qui permet de sauter une ligne

    return word

def img_pendu(name_img) :
    """ Fonction qui affiche l'image du pendu
        Entrée(s): name_img (str, nom de l'image dans le dossier images)
        Sortie(s): None
    """
    img = Image.open (f"jeu_du_pendu/images/{name_img}")
    resized_img = img.resize ((350, 350))
    biscuit_img = ImageTk.PhotoImage (resized_img)
    return biscuit_img

def display (random_word, letter_list = []) :
    """ Fonction qui transforme le mot sous forme d'underscores lorsque les lettres ne sont pas encore devinées
        Entrée(s): None
        Sortie(s): display_word (str, contient les lettres déjà affichées ou sinon des underscores)
    """
    display_word = ""
    for letter in random_word :
        if letter == random_word[0] : # affiche la 1ère lettre
            display_word += random_word[0]
        else :
            if letter in letter_list :
                display_word += letter
            else :
                display_word += "_ "
    return display_word  

window = Tk()
window.title ("Jeu du pendu")

w = 1535
h = 780
window.geometry(f"{w}x{h}+{-10}+0")
Canevas = Canvas (window, width = w, height = h, bg = 'RosyBrown3')

# Affichage de l'image du pendu
biscuit_img = img_pendu("bonhomme8.gif")
Canevas.create_image(1535/2 - 500, 780/2, image = biscuit_img, anchor = CENTER)
Canevas.grid()


window.mainloop()