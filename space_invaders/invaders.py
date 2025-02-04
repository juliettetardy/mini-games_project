# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from PIL import Image, ImageTk
from space_invaders import missile
from random import randint
from tkinter import messagebox

class Invader :
    """
    Une classe qui permet de créer et afficher un alien
    Cette classe s'occupe de tous les éléments graphiques vis à vis d'un alien et comment les afficher.

    Fonctions 
    ---------
        get_position : 
            Fonction qui récupère les coordonnées d'un alien
        invaders_move :
            Fonction qui gère le déplacement d'un alien
    """

    def __init__ (self, x, y, canevas, image_path) :
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle ci.
        Entrée(s): 
            x : coordonées en abscisse d'un alien
                type = int
            y : coordonées en ordonnée d'un alien
                type = int
            canevas : canva du jeu sur lequel l'alien va être placé
                type = Canvas
            image_path : image de l'alien
                type = str

        Sortie(s): None

        """
        # Initialisation du canevas
        self.canevas = canevas

        # Initialistion des coordonnées 
        self.x = x
        self.y = y

        # Chargement de l'image de l'alien
        self.invader_pic = Image.open (image_path)
        self.invader_pic = self.invader_pic.resize ((100, 100))
        self.pic = ImageTk.PhotoImage (self.invader_pic)
        self.invader_item = self.canevas.create_image (self.x + 20, self.y + 20, image = self.pic)

    def get_position (self) :
        """ 
        Fonction qui récupère les coordonnées d'un alien
        Entrée(s): None
        Sortie(s): 
            self.canevas.coords : 
                Coordonnées sur le canva de l'alien
                type = list

        """
        # On récupère les coordonées de l'alien
        return self.canevas.coords (self.invader_item)
    
    def invaders_move (self, speed, moving_down) :
        """ 
        Fonction qui gère le déplacement d'un alien
        Entrée(s): 
            speed : 
                Vitesse à laquelle se déplace l'alien
                type = int
            moving_down : 
                Déplacement vers le bas de l'alien
                type = float

        Sortie(s): None

        """
        # Cas ou l'alien ne descend pas
        if moving_down == 0 :
            self.canevas.move (self.invader_item, speed, 0)

        # Cas ou l'alien doit descendre
        elif moving_down == 1 :
            self.canevas.move (self.invader_item, speed, 2)

class Invaders :
    """
    Une classe qui permet de créer et afficher les aliens
    Cette classe s'occupe de tous les éléments graphiques vis à vis des aliens à afficher et de comment les afficher.

    Fonctions 
    ---------
        add_invaders :
            Fonction qui ajoute plusieurs aliens (à partir de un crée dans la classe précedente)
        move_invaders :
            Fonction qui gère le déplacement de tous les aliens placés sur la canevas
        shoot_ship :
            Fonction qui permet aux aliens de tirer des missiles de manière aléatoire
        suppr_figures :
            Fonction qui supprime les aliens et le vaisseau
        
    """

    def __init__ (self, window, canevas, ship, image_path) :
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle ci.
        Entrée(s): 
            window : 
                fenêtre associée au jeu ou apparaissent les aliens
                type = Tk
            canevas : 
                canevas du jeu sur lequel l'alien va être placé
                type = Canvas
            ship : 
                ship représente le vaisseau du joueur/ le joueur
                type = int
            image_path : 
                image de l'alien
                type = str

        Sortie(s): None
        """
        self.window = window
        self.canevas = canevas
        self.ship = ship
        self.image_path = image_path
        self.invaders = []
        self.index_invaders = []
        self.speed = 4

    def get_invaders (self) :
        """ 
        Fonction qui ajoute plusieurs aliens (à partir de un créé dans la classe précédente)
        Entrée(s): None
        Sortie(s): 
            self.invaders : 
                Liste des numéros liés aux aliens sur le canevas et qui y sont toujours présents
                type = list

        """
        return self.index_invaders

    def add_invaders (self) :
        """ 
        Fonction qui ajoute plusieurs aliens (à partir de un créé dans la classe précédente)
        Entrée(s): None
        Sortie(s): None

        """
        # Initialisation des grandeurs 
        width_canvas = 1530
        height_aliens = 30

        # Création de 3 lignes
        for nmb_lines in range (1, 4) :

            # Distinction des cas pour que les aliens soit en quinconce 
            if nmb_lines % 2 != 0 :
                # Premier cas : ligne de 5 aliens

                # Coordonnées X,Y de chaque alien :
                place_for5 = width_canvas / 5
                final_place_for5 = place_for5 - 20 - width_canvas / 10
                coord_for5 = [[final_place_for5, height_aliens], [final_place_for5 + place_for5, height_aliens], [final_place_for5 + 2 * place_for5, height_aliens], [final_place_for5 + 3 * place_for5, height_aliens], [final_place_for5 + 4 * place_for5, height_aliens]]
                i = 0

                # Ajout un par un des aliens
                while i < 5 :
                    x0, y0 = coord_for5 [i][0], coord_for5 [i][1]
                    invader = Invader (x0, y0, self.canevas, self.image_path)
                    self.invaders.append (invader)
                    self.index_invaders.append (invader.invader_item)
                    i += 1

            else : 
                # Deuxième cas : ligne de 4 aliens
                # Coordonnées X,Y de chaque alien :
                place_for4 = width_canvas / 5
                final_place_for4 = place_for4 - 20 
                coord_for4 = [[final_place_for4, height_aliens], [final_place_for4 + place_for4, height_aliens], [final_place_for4 + 2 * place_for4, height_aliens], [final_place_for4 + 3 * place_for4, height_aliens]]
                i = 0

                # Ajout un par un des aliens
                while i < 4 :
                    x0, y0 = coord_for4 [i][0], coord_for4 [i][1]
                    invader = Invader (x0, y0, self.canevas, self.image_path)
                    self.invaders.append (invader)
                    self.index_invaders.append (invader.invader_item)
                    i += 1

            # Espace entre les aliens
            height_aliens += 80

    def move_invaders (self) :
        """ 
        Fonction qui gère le déplacement de tous les aliens placés sur le canevas
        Entrée(s): None
        Sortie(s): None

        """        
        # Inversion de la vitesse de tous les aliens si celui le plus à droite ou le plus à gauche touche le bord du canvas
        for invader in self.invaders :
            coord = invader.get_position()
            if len (coord) == 2 :

                # Prise en compte de la largeur de l'image de l'alien et des bords droit et gauche du canvas
                if coord [0] + 20 >= 1530 or coord [0] - 20 <= 0 :

                    # Inversion de la vitesse des aliens
                    self.speed = - self.speed 
                    break

        # Descente des aliens si ils tapent à gauche
        for invader in self.invaders :
            coord = invader.get_position()
            if len (coord) == 2 :
                if coord [0] - 40 <= 0 :
                    for invader in self.invaders :

                        # Les aliens bougent vers le bas 
                        invader.invaders_move (self.speed, 1)
                    break

                else :
                    # Les aliens ne bougent pas vers le bas 
                    invader.invaders_move (self.speed, 0)

        # Destruction du vaisseau et arrêt de la partie si les aliens touchent le vaisseau ou le bas du canvas
        for invader in self.invaders :
            coords = invader.get_position()
            if len (coords) == 2 :
                coord = [coords [0] - 20, coords [1] - 20] + coords

                # Utilisation de find_overlapping pour savoir si les coordonnées sont les mêmes que d'autres éléments sur le canvas
                contacts = self.canevas.find_overlapping (*coord)
                if coord [1] > 620 :
                    self.canevas.delete (invader.invader_item)
                    self.invaders.remove (invader)
                    self.ship.life = 0

                    # Suppression des figures sur le canvas
                    self.suppr_figures()

                    # Création d'un message de fin
                    messagebox.showinfo ("Perdu", "Vous n'avez pas réussi à détruire tous les aliens à temps")
                    break
                
                else : 
                    for item in contacts :
                        if item == self.ship.player_item :
                            self.ship.life = 0

                            # Suppression des figures sur le canvas
                            self.suppr_figures()

                            # Création d'un message de fin
                            messagebox.showinfo ("Perdu", "Vous avez été tué par les aliens")
                            break
        """
        # Si il n'y a plus d'aliens, c'est la fin de la partie
        if self.get_invaders() == [] :
            messagebox.showinfo ("Bravo !", "Vous avez réussi à éliminer tous les aliens !")
        """

        # Exécute la fonction après un délai (pas immédiatement)
        self.window.after (20, self.move_invaders)

    def shoot_ship (self, back_img) :
        """ 
        Fonction qui permet aux aliens de tirer des missiles de manière aléatoire
        Entrée(s): 
            back_img : Image de fond du jeu ou se trouve les aliens
                type = int
        Sortie(s): None

        """
        for invader in self.invaders :
            can_shoot = randint(0, 250)

            # Probabilité de 1/250 de tirer 
            if can_shoot == 250 :
                coord = invader.get_position()
                if len (coord) == 2 :

                    # L'alien tire un missile
                    shot = missile.Missile_I (coord[0] - 5, coord[1] + 40, self.window, self.canevas, self.ship)
                    shot.bullet_invaders (back_img, self.invaders)

        # Exécute la fonction après un délai (pas immédiatement)
        self.window.after (30, lambda : self.shoot_ship (back_img))

    def suppr_figures (self) :
        """ 
        Fonction qui supprime les aliens et le vaisseau
        Entrée(s): None
        Sortie(s): None

        """
        # Suppression de chaque alien
        for invader in self.invaders :
            self.canevas.delete (invader.invader_item)
            self.invaders.remove (invader)

        # Suppression du vaisseau
        self.canevas.delete (self.ship.player_item)

    

