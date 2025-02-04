# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
import random

def new_code() :
    """ Fonction qui retourne le code à 6 chiffres à trouver
        Entrée(s): None
        Sortie(s): code (str)
    """
    code = ''
    for i in range (6) : 
        code += str (random.randint(1,9))
    return code

def ask_code() :
    """ Fonction qui retourne le code à 6 chiffres donné par l'utilisateur
        Entrée(s): None
        Sortie(s): code (str) 
    """
    valid = [False, False, False, False, False, False]
    while False in valid :
        print ('Veuillez entrer seulement 6 chiffres, entre 1 et 9, sans espace ni autre caractère')
        code = input('')
        if len (code) == 6 :
            for i in range( len(code) ) :
                if code[i] in '123456789' :
                    valid[i] = True
    return code

def game () :
    """ Fonction qui fait fonctionner le jeu Mastermind
        Entrée(s): None
        Sortie(s): None
    """
    code = new_code()
    test = 0
    while test < 8 :
        user_code = ask_code()

        # Vérification du code entré par l'utilisateur est le bon code
        if code == user_code : 
            print ("Bravo, vous avez deviné le code !")
            break
        
        # Comparaison des chiffres du code et du user_code
        result = ''
        for i in range (6) :
            if user_code[i] == code[i] :
                result += 'B' # B pour bien placé
            elif user_code[i] in code :
                result += 'M' # M pour dans le code mais mal placé
            else :
                result += 'A' # A pour absent du code

        print("Pour chaque chiffre proposé, B signifie bien placé, M mal placé et A absent du code")
        print("Votre code : ", user_code, ", le résultat : ", result)
        print("")
        
        test += 1
        if 8 - test == 0 :
            # Message renvoyé lorsque les 8 propositions sont passées
            print("Vous avez perdu, le bon code était ", code) 
        elif 8 - test == 1 :
            print("Il vous reste 1 essai")
        elif 8 - test < 8 :
            print("Il vous reste", 8 - test, "essais")

game()