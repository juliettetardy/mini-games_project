"""
Tardy Juliette et Curie Justine

TP 3 CS-DEV - Création du jeu du pendu version console et version graphique.

Réalisé le 06/10/2023
   
Il reste à coder la version graphique.

"""

def display_random_word(random_word):
    # Cette fonction affiche un mot "à deviner" choisis aléatoirement dans une
    # liste pré-définie. Elle affiche la première lettre du mot et des
    # underscore pour les autres lettres qui sont différentes.
    hidden_word = ''
    for letter in random_word :
        if letter == random_word[0]: # afficher la 1ère lettre
            hidden_word = hidden_word + random_word[0] + " "
        else :
            hidden_word = hidden_word + "_ "
   
    print(hidden_word)
    return hidden_word


def word_display (letter, display_word, random_word) :
    #Cette fonction permet de mettre à jour le mot caché. Si la lettre saisie
    #est dans le mot à deviner, l'underscore est remplacé par la lettre.
    #display_word est un mot qui mélange underscore et lettre
    if letter in display_word :
        print ("La lettre est déjà affichée")
        return display_word
    else :
        for i, character in enumerate (random_word) :
            if character == letter :
                #permet d'afficher correctement le nouveau mot sachant qu'il faut conserver les espaces.
                display_word = display_word [ 0 : (2*i) ] + letter + display_word [ (2*i)+1 : ]
        return display_word

def choice_letter (random_word) :
    # Cette fonction permet de faire choisir une lettre à l'utilisateur.
    # Soit la lettre est déja écrite, soit elle est juste, soit elle ne l'est
    # pas. Cette fonction traîte ces trois cas.
    attempt = 8
    update = display_random_word(random_word)
    used_letter = [] #permet à l'utilisateur de savoir les lettres déja testées
   
    while attempt > 0 :
        if '_' not in update :
            print("") # rend l'affichage plus clair, saute une ligne
            print ("Vous avez gagné !!!")
            print("Le mot était", random_word)
            return update
        else :
            print("")
            letter = str(input("Donner une lettre : "))
            used_letter += letter
            if letter in random_word :
                update = word_display (letter, update, random_word)
                print (update)
                print ("les lettres utilisées sont : " , used_letter)
            else :
                print ("La lettre proposée n'est pas dans le mot")
                print (update)
                print ("les lettres utilisées sont : " , used_letter)
                attempt = attempt - 1 # l'utilisateur perd une vie
               
    print("")            
    print ("Vous n'avez pas réussi, le mot était", random_word)
    return update