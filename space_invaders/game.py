# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import Tk, Canvas, Button, Label, NW, W, E, IntVar, Frame
from PIL import Image, ImageTk
from space_invaders import invaders, ship, boss, islet
import subprocess

class Game :
    """
    Une classe qui permet de jouer au jeu "Space Invaders _ Ju^2 Version".
    Cette classe s'occupe de tous les éléments graphiques à afficher et de comment les afficher.

    Fonctions 
    ---------
        start_game :
            Fonction qui démarre le jeu lorsque l'on est sur l'écran d"accueil.
        get_window :
            Fonction qui affiche la fenêtre du menu d'accueil.
        new_game :
            Fonction qui permet de jouer une nouvelle partie.
        create_widgets :
            Fonction qui rassemble et ajoute les widgets sur la frame du jeu principal.
        create_figures :
            Fonction qui créer les objets (aliens, vaisseau, missiles, îlots) à afficher.
        hide_score_and_life :
            Fonction qui permet de cacher le score et le nombre de vies restantes.
        show_score_and_life :
            Fonction qui permet d'afficher le score et le nombre de vies restantes.
        quit :
            Fonction qui ferme la fenêtre et reviens sur le menu principal

    """
    def __init__ (self) :
        """
        Initialisateur. 
        Fonction qui initialise les objets de la classe pour les réutiliser dans les fonctions associées à celle ci.
        Entrée(s): None
        Sortie(s): None

        """
        # Création de la fenêtre et de son nom
        self.window = Tk()
        self.window.title ('Space Invaders Ju2 version')
        self.window.geometry (f"+{-8}+0")

        # Initialisation dimensions des canevas 
        self.width_canvas = 1530
        self.height_canvas = 700

        self.width_canvas_welc = 1530
        self.height_canvas_welc = 1000
    
        # Création de la frame "écran d'accueil"
        self.welcome_frame = Frame (self.window)
        self.Canevas_welc = Canvas (self.welcome_frame, width = self.width_canvas_welc, height = self.height_canvas_welc, bg = 'gray')

        # Ajout d'un bouton pour démarrer le jeu
        button_start_game = Button (self.welcome_frame, text = 'Start game', fg ='navy', command = self.start_game)
        button_start_game.grid (row = 2, padx = 3, pady = 3)

        # Affichage de l'image de fond de la frame d'accueil
        self.back_pic_welc = Image.open ("space_invaders/images/front_page.jpg")
        self.resized_welc = self.back_pic_welc.resize ((1530, 1000))
        self.background_welc = ImageTk.PhotoImage (self.resized_welc)
        self.Canevas_welc.create_image(0, 0, image = self.background_welc, anchor = NW)

        # Affichage du canevas associé à la frame d'accueil
        self.Canevas_welc.grid()

        # Affichage la frame d'accueil 
        self.welcome_frame.grid()

        # Récupération et ajustement de l'image de fond des frames
        self.back_pic = Image.open ("space_invaders/images/milky_way.jpg")
        self.resized = self.back_pic.resize ((1530, 700))
        self.background = ImageTk.PhotoImage (self.resized)

        ## ----- Premier niveau du jeu -----
        # Création de la frame du premier niveau
        self.frame_lvl1 = Frame (self.window)
        self.Canevas_lvl1 = Canvas (self.frame_lvl1, width = self.width_canvas, height = self.height_canvas, bg = 'gray')

        # Affichage de la frame du premier niveau
        self.frame_lvl1.grid()

        # Initialisation de la variable score du joueur pour le premier niveau
        self.score = IntVar()
        self.score.set (0)

        # Affichage du score pour le premier niveau
        self.label_score = Label (self.frame_lvl1, fg = 'navy', textvariable = self.score)
        self.label_score.grid (row = 2, sticky = W, pady = 3)
        self.score_text = Label (self.frame_lvl1, fg = 'navy', text = "Score : ")
        self.score_text.grid (row = 1, sticky = W, pady = 3)

        # Initialisation de la variable vie du joueur pour le premier niveau
        self.life_nb = IntVar()
        self.life_nb.set (3)
        
        # Affichage du nombre de vies restantes pour le premier niveau
        self.label_life = Label (self.frame_lvl1, fg = 'navy', textvariable = self.life_nb)
        self.label_life.grid (row = 4, sticky = W, padx = 3, pady = 3)
        self.life_text = Label (self.frame_lvl1, fg = 'navy', text = "Remaining lives : ")
        self.life_text.grid (row = 3, sticky = W, padx = 3, pady = 3)


        ## ----- Niveau boss du jeu -----
        # Création de la frame du niveau boss
        self.frame_lvlboss = Frame (self.window)
        self.Canevas_lvlboss = Canvas (self.frame_lvlboss, width = self.width_canvas, height = self.height_canvas, bg = 'gray')

        # Affichage de la frame du niveau boss
        self.frame_lvlboss.grid()

        # Affichage du score pour le niveau boss
        self.label_score = Label (self.frame_lvlboss, fg = 'navy', textvariable = self.score)
        self.label_score.grid (row = 2, sticky = W, pady = 3)
        self.score_text = Label (self.frame_lvlboss, fg = 'navy', text = "Score : ")
        self.score_text.grid (row = 1, sticky = W, pady = 3)
        
        # Affichage du nombre de vies restantes du joueur pour le niveau boss
        self.label_life = Label (self.frame_lvlboss, fg = 'navy', textvariable = self.life_nb)
        self.label_life.grid (row = 4, sticky = W, padx = 3, pady = 3)
        self.life_text = Label (self.frame_lvlboss, fg = 'navy', text = "Player remaining lives : ")
        self.life_text.grid (row = 3, sticky = W, padx = 3, pady = 3)

        # Initialisation de la variable vie du boss pour le premier niveau
        self.life_boss = IntVar()
        self.life_boss.set (10)

        # Affichage du nombre de vies restantes du boss pour le niveau boss
        self.label_life_boss = Label (self.frame_lvlboss, fg = 'navy', textvariable = self.life_boss)
        self.label_life_boss.grid (row = 4, sticky = E, padx = 3, pady = 3)
        self.life_boss_text = Label (self.frame_lvlboss, fg = 'navy', text = "Boss remaining lives : ")
        self.life_boss_text.grid (row = 3, sticky = E, padx = 3, pady = 3)

    def start_game (self):
        """ 
        Fonction qui démarre le jeu lorsque l'on est sur l'écran d'accueil 
        Entrée(s): None
        Sortie(s): None

        """
        # Suppression de la frame précédente (frame menu d'accueil)
        self.welcome_frame.grid_forget()

        # Affichage du score et des vies du joueur
        self.show_score_and_life()

        # Création et mise en route d'une partie
        self.new_game()

    def start_game_boss (self) :
        """ 
        Fonction qui démarre le jeu losqu'on appuie sur le bouton New Game depuis le niveau boss
        Entrée(s): None
        Sortie(s): None

        """
        # Suppression de la frame précédente (frame niveau boss)
        self.frame_lvlboss.grid_forget()

        # Suppression de la vie du boss
        self.hide_boss_life()

        # Affichage de la frame premier niveau
        self.frame_lvl1.grid()

        # Affichage du score et des vies du joueur
        self.show_score_and_life()

        # Création et mise en route d'une partie
        self.new_game()
   
    def get_window (self) :
        """
        Fonction qui affiche la fenêtre du menu d'accueil
        Entrée(s): None
        Sortie(s): 
            window : fenêtre du menu d'accueil
                     type = window

        """
        # Masquage du score et des vies qui sont inutiles ici
        self.hide_score_and_life()

        # Affichage de la fenêtre du menu d'accueil
        return self.window

    def new_game (self) :
        """
        Fonction qui permet de lancer une nouvelle partie
        Entrée(s): None
        Sortie(s): None

        """
        # Supression de tout ce qu'il y a sur le Canevas
        self.Canevas_lvl1.delete ('all') 

        # Réinitialisation des scores et du nombre de vies
        self.score.set (0)
        self.life_nb.set (3)

        # Remise à l'initiale des widgets et des figures sur le Canevas 
        img = self.create_widgets()
        self.create_figures_lvl1 (img)

    def boss_level (self) :
        """
        Fonction qui permet de lancer le niveau boss une fois que le premier niveau a été réussi
        Entrée(s) : None
        Sortie(s) : None

        """
        # Supression de tout ce qu'il y a sur le Canevas
        self.Canevas_lvl1.delete ('all') 
        self.Canevas_lvlboss.delete ('all')

        # Suppression de la frame précédente (frame premier niveau)
        self.frame_lvl1.grid_forget()

        # Affichage du score et des vies du joueur
        self.show_score_and_life()

        # Apparition de la frame du niveau boss
        self.frame_lvlboss.grid()
        
        # Réinitialisation du nombre de vies
        self.life_nb.set (3)

        # (Ré) initialisation du nombre de vies du boss 
        self.life_boss.set (10)

        # (Re) mise à l'initiale des widgets et des figures sur le Canevas 
        img = self.create_widgets ("lvlboss")
        self.create_figures_nvboss (img)

    def create_widgets (self, typ_lvl = "lvl1") :
        """
        Fonction qui rassemble et ajoute les widgets sur la frame du jeu principal
        Entrée(s): None
        Sortie(s): 
            background_img : Image de fond du jeu
                             type = int

        """
        if typ_lvl == "lvl1" :
            # Création d'un bouton pour détruire la fenêtre
            button_quit = Button (self.frame_lvl1, text = 'Quit', fg = 'navy', command = self.quit)
            button_quit.grid (row = 4, padx = 3, pady = 3)

            # Création d'un bouton pour relancer une nouvelle partie
            button_new_game = Button (self.frame_lvl1, text = 'New game', fg ='navy', command = self.new_game)
            button_new_game.grid (row = 2, padx = 3, pady = 3)

            # Création d'un bouton pour lancer le niveau boss
            button_new_game = Button (self.frame_lvl1, text = 'Start boss level', fg ='navy', command = self.boss_level)
            button_new_game.grid (row = 4, sticky = E, padx = 3, pady = 3)

            # Ajout d'une image de fond 
            background_img = self.Canevas_lvl1.create_image (0, 0, anchor = NW, image = self.background)
            self.Canevas_lvl1.grid()
            return background_img
        
        elif typ_lvl == "lvlboss" :
            # Création d'un bouton pour détruire la fenêtre
            button_quit = Button (self.frame_lvlboss, text = 'Quit', fg = 'navy', command = self.quit)
            button_quit.grid (row = 4, padx = 3, pady = 3)

            # Création d'un bouton pour relancer une nouvelle partie
            button_new_game = Button (self.frame_lvlboss, text = 'Restart boss level', fg ='navy', command = self.boss_level)
            button_new_game.grid (row = 2, padx = 3, pady = 3)

            # Création d'un bouton pour relancer une nouvelle partie depuis le début
            button_new_game = Button (self.frame_lvlboss, text = 'New game', fg ='navy', command = self.start_game_boss)
            button_new_game.grid (row = 2, sticky = E, padx = 3, pady = 3)
        
            # Ajout d'une image de fond 
            background_img = self.Canevas_lvlboss.create_image (0, 0, anchor = NW, image = self.background)
            self.Canevas_lvlboss.grid()
            return background_img

    def create_figures_lvl1 (self, back_img = 1) :
        """
        Fonction qui créer les objets (aliens, vaisseau, missiles, îlots) à afficher
        Entrée(s):
            back_img :  Background du jeu.
                        Si on ne veut pas afficher l'image de fond, il suffit de passer 0 en argument
                        type = int
        Sortie(s): None

        """
        # Création de 3 îlots protecteurs
        islet1 = islet.Islet (100, 480, 25, self.Canevas_lvl1)
        islet2 = islet.Islet (650, 480, 25, self.Canevas_lvl1)
        islet3 = islet.Islet (1200, 480, 25, self.Canevas_lvl1)
        islet1.multiply_islet()
        islet2.multiply_islet()
        islet3.multiply_islet()

        # Création du vaisseau/joueur
        Player = ship.Ship (765, 625, self.frame_lvl1, self.Canevas_lvl1, self.width_canvas, self.height_canvas, "space_invaders/images/vaisseau_zinzins.png")

        # Gestion des déplacements du joueur en utilisant des touches du clavier
        self.Canevas_lvl1.bind_all ("<KeyPress-Left>", lambda _ : Player.ship_move (-15)) 
        self.Canevas_lvl1.bind_all ("<KeyPress-Right>", lambda _ : Player.ship_move (15)) 

        # Création des aliens et gestion de leur mouvements
        aliens = invaders.Invaders (self.frame_lvl1, self.Canevas_lvl1, Player, "space_invaders/images/alien.png")
        aliens.add_invaders()
        aliens.move_invaders()

        # Création d'un missile tiré par le vaisseau
        self.Canevas_lvl1.bind_all ("<KeyPress-space>", lambda _ : Player.shoot_invaders (back_img, aliens)) 

        # Création des missiles tirés par les aliens
        aliens.shoot_ship (back_img)

        # Modification du score et de la vie
        Player.var_score = self.score
        Player.var_life = self.life_nb
    
    def create_figures_nvboss (self, back_img = 1) :
        """
        Fonction qui créer les objets (aliens, vaisseau, missiles, îlots) à afficher
        Entrée(s):
            back_img :  Background du jeu.
                        Si on ne veut pas afficher l'image de fond, il suffit de passer 0 en argument
                        type = int
        Sortie(s): None

        """
        # Création du vaisseau/joueur
        Player = ship.Ship (765, 625, self.frame_lvlboss, self.Canevas_lvlboss, self.width_canvas, self.height_canvas, "space_invaders/images/vaisseau_zinzins.png")

        # Gestion des déplacements du joueur en utilisant des touches du clavier
        self.Canevas_lvlboss.bind_all ("<KeyPress-Left>", lambda _ : Player.ship_move (-25)) 
        self.Canevas_lvlboss.bind_all ("<KeyPress-Right>", lambda _ : Player.ship_move (25)) 

        # Création du boss et gestion de ses mouvements
        big_boss = boss.Boss (self.width_canvas / 2 - 25, 100, self.frame_lvlboss, self.Canevas_lvlboss, Player, "space_invaders/images/boss.png")
        big_boss.boss_move()

        # Création d'un missile pour le vaisseau
        self.Canevas_lvlboss.bind_all ("<KeyPress-space>", lambda _ : Player.shoot_boss (back_img, big_boss)) 

        # Création des missiles pour le boss
        big_boss.boss_shot (back_img)

        # Modification du score et de la vie du joueur
        Player.var_score = self.score
        Player.var_life = self.life_nb

        # Modification de la vie du boss
        big_boss.var_life_boss = self.life_boss

    def hide_score_and_life (self):
        """
        Fonction qui permet de cacher le score et le nombre de vies restantes.
        "grid_remove" est une fonction qui rend des éléments invisibles dans l'interface.
        Entrée(s): None
        Sortie(s): None

        """
        # Masquage du score 
        self.label_score.grid_remove() 
        self.score_text.grid_remove()

        # Masquage du nombre de vie
        self.label_life.grid_remove()
        self.life_text.grid_remove()

    def hide_boss_life (self):
        """
        Fonction qui permet de cacher le nombre de vies restantes du boss.
        "grid_remove" est une fonction qui rend des éléments invisibles dans l'interface.
        Entrée(s): None
        Sortie(s): None

        """
        # Masquage du nombre de vie
        self.label_life_boss.grid_remove()
        self.life_boss_text.grid_remove()

    def show_score_and_life (self):
        """
        Fonction qui permet d'afficher le score et le nombre de vies restantes.
        "grid" permet d'afficher des éléments dans l'interface.
        Entrée(s): None
        Sortie(s): None

        """
        # Affichage du score
        self.label_score.grid()
        self.score_text.grid()

        # Affichage du nombre de vie
        self.label_life.grid()
        self.life_text.grid()

    def quit (self):
        """ 
        Fonction qui ferme la fenêtre et reviens sur le menu principal
        Entrée(s): None
        Sortie(s): None

        """
        self.window.destroy()
        subprocess.run (["python", "main.py"])


    



        

        


