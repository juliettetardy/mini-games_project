# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from random import choice
from tkinter import Tk, Label, Button, Canvas, PhotoImage

def display (random_word, letter_list = []) :
    """ Fonction qui affiche le mot avec des underscores dans le terminal
        Entrée(s): random_word
                   letter_list
        Sortie(s): random_word
                   display_word
    """
    display_word = ""
    for letter in random_word :
        if letter == random_word[0] : # affiche la 1ère lettre
            display_word += random_word[0]
        else :
            if letter in letter_list :
                display_word += letter
            else :
                display_word += "_"
    return random_word, display_word      

def choice_letter (random_word) :
    attempt = 8
    update = display (random_word)
    print(update)
    used_letter = []
    while attempt > 0 :
        if '_' not in update :
            print ("Vous avez gagné !")
            return update
        
        else :
            letter = str(input("Donner une lettre : "))
            
            if letter == random_word[0] :
                print("La lettre est déjà affichée")
                
            elif letter not in used_letter :
                used_letter += letter
                if letter in random_word :
                    update = display (random_word, used_letter)
                    print (update)
                    print ("Les lettres déjà utilisées sont : ", used_letter)
                    
                else :
                    print ("La lettre proposée n'est pas dans le mot")
                    print (update)
                    print ("Les lettres utilisées sont : ", used_letter)
                    attempt = attempt - 1
            
            else :
                print("La lettre est déjà affichée")
            
    print ("Vous n'avez pas réussi, le mot était",  random_word)
    return update
    
def open_image() :
    canevas = Canvas(window, width = 200, height = 200, bg ='black')
    photo = PhotoImage(file = 'bonhomme1.gif')
    item = canevas.create_image(80, 80, image = photo)
    return item
    
words_list = ['jeu', # 3 lettres
              'jeux', 'voir', # 4 lettres
              'avion', 'plage', 'table', 'ville', 'jouet', # 5 lettres
              'girafe', 'jardin', 'papier', 'pirate', 'requin', 'souris', 'masque', # 6 lettres
              'poisson', # 7 lettres
              'bonhomme', 'bracelet', 'vêtement', # 8 lettres
              'bouteille', 'vêtements', 'connaître', # 9 lettres
              'ordinateur', 'ordonnance' # 10 lettres
              'anticonstitutionnellement'] # 25 lettres
word = choice (words_list) # Choisis aléatoirement un mot dans liste

window = Tk()

labelstart = Label(window, text = 'Bienvenue dans le jeu du pendu !', fg = 'navy')
labelstart.grid(row = 1, column = 2)

buttonQuitt = Button(window, text = 'Proposer', fg = 'purple', command = open_image)
buttonQuitt.grid(row = 3, column = 2)





window.mainloop()