# Importation des fichiers nécessaires au fonctionnement du jeu
from space_invaders import missile
from PIL import Image, ImageTk
from tkinter import messagebox

class Ship:
    """
    Une classe qui permet de controler le vaisseau du joueur.
    Cette classe s'occupe de tous les éléments graphiques vis à vis du vaisseau et la gestion des mouvements.

    Fonctions 
    ---------
        ship_move :
            Fonction qui permet de déplacer le vaisseau 
        fire_shoot :
            Fonction qui permet de déplacer le vaisseau
        get_score :
            Fonction qui récupère le score 
        add_score :
            Fonction qui ajoute le score du joueur 
        lost_life :
            Fonction qui démarre le jeu lorsque l'on est sur l'écran d"accueil

    """
    
    def __init__ (self, x, y, window, canevas, width, height, image_path) : 
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle ci.
        Entrée(s): 
            x : 
                Coordonnées en abscisse du vaisseau sur l'écran
                type = int

            y : 
                Coordonnées en ordonnée du vaisseau sur l'écran
                type = int

            window : 
                Fenêtre contenant le jeu
                type = Tk

            canevas : 
                Canva du jeu sur lequel le missile va se déplacer
                type = Canvas
            
            width : 
                Largeur du vaisseau
                type = int

            height :
                Hauteur du vaisseau
                type = int

            img_path :
                Image du vaisseau 
                type = str


        Sortie(s): None

        """
        self.x = x
        self.y = y
        self.window = window
        self.canevas = canevas

        self.life = 3
        self.var_life = None
        self.score = 0
        self.var_score = None

        # Création de l'image du vaisseau
        self.w = width / 2
        self.h = height - 70
        self.ship_pic = Image.open (image_path)
        self.ship_pic = self.ship_pic.resize ((100,100))
        self.pic = ImageTk.PhotoImage (self.ship_pic)
        self.player_item = self.canevas.create_image (self.w, self.h, image = self.pic)

    def ship_move (self, delta) :
        """ 
        Fonction qui permet de déplacer le vaisseau 
        Entrée(s): 
            delta : longueur de déplacement du vaisseau à chaque appel de la fonction
            type = int
        Sortie(s): None

        """
        coord = self.canevas.coords (self.player_item)
        if len (coord) == 2 :
            new_position = coord [0] + delta
            if 40 < new_position < 1490 : 
                self.canevas.move (self.player_item, delta, 0)
        
    def shoot_invaders (self, back_img, invaders) :
        """ 
        Fonction qui envoie un missile du vaisseau vers les aliens
        Entrée(s): 
            back_img : 
                Image de fond du jeu
                type = int
            invaders :
                Liste des numéros des aliens sur le canevas
                type = list
        Sortie(s): None

        """
        # Si il n'y a plus d'aliens, c'est la fin de la partie
        if invaders.get_invaders() == [] :
            messagebox.showinfo ("Bravo !", "Vous avez réussi à éliminer tous les aliens !")

        else :
            coord = self.canevas.coords (self.player_item)
            if len (coord) == 2 :
                # Création d'un missile
                shot = missile.Missile_S (coord [0] + 7, coord [1] - 80, self.window, self.canevas, self)
                shot.bullet_ship_i (back_img, invaders.get_invaders())

    def shoot_boss (self, back_img, boss) :
        """ 
        Fonction qui envoie un missile du vaisseau vers le boss
        Entrée(s): 
            back_img : 
                Image de fond du jeu
                type = int
            boss :
                Boss que le joueur doit vaincre 
                type = Class
        Sortie(s): None

        """
        coord = self.canevas.coords (self.player_item)
        if len (coord) == 2 :
            # Création d'un missile
            shot = missile.Missile_S (coord [0] + 7, coord [1] - 80, self.window, self.canevas, self, boss)
            shot.bullet_ship_b (back_img)            

    def get_score (self) :
        """ 
        Fonction qui récupère le score 
        Entrée(s): None
        Sortie(s): 
            score :
                Score du joueur 
                type = int

        """
        return self.score

    def add_score (self, score_to_add) :
        """ 
        Fonction qui ajoute le score du joueur  
        Entrée(s): 
            score_to_add :
                Points à ajouter au score du joueur
                type = int
        Sortie(s): None

        """
        self.score += score_to_add
        if self.var_score :
            self.var_score.set (self.score)

    def lost_life (self) :
        """ 
        Fonction qui gère la perte des vies à chaque fois que l'utilisateur en perd une
        Entrée(s): None
        Sortie(s): 
            0 : 
                Si c'est la dernière vie du joueur
                type = int
            1 :
                Si le joueur a perdu une vie
                type = int  

        """

        # Cas où le joueur n'a plus qu'une vie
        if self.life == 1 :
            self.life -= 1
            if self.var_life :
                self.var_life.set (self.life)
            return 1
        
        # Cas où le joueur a encore 2 ou 3 vies
        else :
            self.life -= 1
            if self.var_life :
                self.var_life.set (self.life)
            return 0