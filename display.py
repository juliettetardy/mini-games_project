# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import Tk, Canvas, Button, Frame, Toplevel, Label, Entry, messagebox, NW, CENTER
from PIL import Image, ImageTk
import subprocess

from space_invaders import SpaceInvadersGame
from mastermind import MastermindGame
from jeu_du_pendu import HangmanGame

class Display :
    """
    Une classe qui crée une interface de mini-jeux sous Tkinter

    Fonctions :
        menu :
            ...
        space_invaders :
            ...
        hangman_game :
            ...
        mastermind :
            ...
        life_game :
            ...
        vhinfos  :
            Fonction qui regarde si les données entrées sont bien des nombres, sachant que les données sont
            la taille horizontalement et verticalement de la fenêtre
        on_button_click :
            Fonction appelée sur le clic du bouton et appelle la fonction vhinfos

    """
    def __init__(self):
        # Stocke les dimensions de la fenêtre Jeu de la Vie
        self.vertical_cells, self.horizontal_cells = None, None

        ## ----- Initialise la fenêtre -----
        # Création de la fenêtre et de son nom
        self.window = Tk()
        self.window.title ('Mini-games')
        self.window.geometry(f"+{-10}+0")

        # Initialisation dimensions des canvas 
        self.w_canvas = 1535
        self.h_canvas = 780

        ## ----- Frame d'accueil -----
        # Création de la frame "écran d'accueil"
        self.welcome_frame = Frame (self.window)
        self.Canevas_welc = Canvas (self.welcome_frame, width = self.w_canvas, height = self.h_canvas, bg = 'gray')

        # Ajout d'un bouton pour démarrer le jeu
        self.button_choose = Button (self.welcome_frame, 
                                    text = 'Choose your game', 
                                    fg ='black', 
                                    bg ='white', 
                                    font = ("Georgia", 16, "bold"), 
                                    bd = 10, 
                                    command = self.menu)
        self.Canevas_welc.create_window(self.w_canvas//2, self.h_canvas//2 + 20, window = self.button_choose)

        # Affichage de l'image de fond de la frame d'accueil
        self.back_pic_welc = Image.open ("images/front_page.png")
        self.resized_welc = self.back_pic_welc.resize ((1535, 780))
        self.background_welc = ImageTk.PhotoImage (self.resized_welc)
        self.Canevas_welc.create_image(0, 0, image = self.background_welc, anchor = NW)

        # Affichage du canevas associé à la frame d'accueil
        self.Canevas_welc.grid()

        # Affichage de la frame d'accueil 
        self.welcome_frame.grid()


        ## ----- Choix du jeu -----
        # Image de fond pour le choix du jeu
        self.back_pic_choice = Image.open ("images/side_page.png")
        self.resized_choice = self.back_pic_choice.resize ((1535, 780))
        self.background_choice = ImageTk.PhotoImage (self.resized_choice)

        # Création de la frame de choix du jeu
        self.frame_choice = Frame (self.window)
        self.Canevas_choice = Canvas (self.frame_choice, width = self.w_canvas, height = self.h_canvas, bg = 'gray')

        # Affichage de la frame de choix du jeu
        self.frame_choice.grid()

        # Vignettes image issues des jeux
        self.game_pic_1 = Image.open ("images/space_invaders.png")
        self.game_pic_1 = self.game_pic_1.resize ((int(512/2 + 50), int(384/2 + 50)))
        self.game_pic_1 = ImageTk.PhotoImage (self.game_pic_1)

        self.game_pic_2 = Image.open ("images/nuage.png")
        self.game_pic_2 = self.game_pic_2.resize ((int(512/2 + 50), int(384/2 + 50)))
        self.game_pic_2 = ImageTk.PhotoImage (self.game_pic_2)

        self.game_pic_3 = Image.open ("images/nuage.png")
        self.game_pic_3 = self.game_pic_3.resize ((int(512/2 + 50), int(384/2 + 50)))
        self.game_pic_3 = ImageTk.PhotoImage (self.game_pic_3)

        self.game_pic_4 = Image.open ("images/jeu_de_la_vie.png")
        self.game_pic_4 = self.game_pic_4.resize ((int(512/2 + 50), int(384/2 + 50)))
        self.game_pic_4 = ImageTk.PhotoImage (self.game_pic_4)

        self.window.mainloop()

    def menu(self) :
        """ Fonction qui permet de choisir son mini-jeu
            Entrée(s): None
            Sortie(s): None
        """
        # Suppression de la frame précédente (frame menu d'accueil)
        self.welcome_frame.grid_forget()
        
        pos_w = self.w_canvas/4
        pos_h = self.h_canvas/4

        # Ajout d'une image de fond 
        self.Canevas_choice.create_image (0, 0, anchor = NW, image = self.background_choice)

        # Création d'un bouton pour détruire la fenêtre
        button_quit = Button (self.frame_choice, 
                            text = 'Quit', 
                            fg = 'black', bg = 'white', bd = 10, 
                            font = ("Georgia", 12, "bold"),
                            command = self.window.destroy)
        self.Canevas_choice.create_window(self.w_canvas - 50, 50, window = button_quit) # permet de placer le bouton dans le canva

        # Création d'un bouton + image pour lancer le jeu Space invaders
        button = Button (self.frame_choice, 
                        text = 'Start Space Invaders', 
                        fg = 'black', bg = 'white', bd = 10, 
                        font = ("Georgia", 12, "bold"), 
                        command = self.space_invaders)
        self.Canevas_choice.create_window(int(pos_w), int(pos_h - 80), window = button)
        self.Canevas_choice.create_image (int(pos_w), int(pos_h - 80 + 175), anchor = CENTER, image = self.game_pic_1)

        # Création d'un bouton + image pour lancer le jeu du Pendu
        button = Button (self.frame_choice, 
                        text = 'Start Hangman game', 
                        fg = 'black', bg = 'white', bd = 10, 
                        font = ("Georgia", 12, "bold"), 
                        command = self.hangman_game)
        self.Canevas_choice.create_window(int(3*pos_w), int(pos_h - 80), window = button)
        self.Canevas_choice.create_image (int(3*pos_w), int(pos_h - 80 + 175), image = self.game_pic_2)

        # Création d'un bouton + image pour lancer le jeu Mastermind
        button = Button (self.frame_choice, 
                        text = 'Start Mastermind', 
                        fg = 'black', bg = 'white', bd = 10, 
                        font = ("Georgia", 12, "bold"),
                        command = self.mastermind)
        self.Canevas_choice.create_window(int(pos_w), int(3*pos_h - 120), window = button)
        self.Canevas_choice.create_image (int(pos_w), int(3*pos_h - 120 + 175), image = self.game_pic_3)

        # Création d'un bouton + image pour lancer le jeu de la Vie
        button = Button (self.frame_choice, 
                        text = 'Start Life game', 
                        fg = 'black', bg = 'white', bd = 10, 
                        font = ("Georgia", 12, "bold"),
                        command = self.life_game)
        self.Canevas_choice.create_window(int(3*pos_w), int(3*pos_h - 120), window = button)
        self.Canevas_choice.create_image (int(3*pos_w), int(3*pos_h - 120 + 175), image = self.game_pic_4)
        
        self.Canevas_choice.grid()

    def space_invaders(self) :
        """ Fonction qui permet de lancer le jeu Space Invaders
            Entrée(s): None
            Sortie(s): None
        """
        #self.window.destroy() # ne pas enlever sinon ne fonctionne plus !
        jeu = SpaceInvadersGame()

        # Récupération et bouclage de la frame du jeu
        fenetre = jeu.get_si_window()
        fenetre.mainloop()

    def hangman_game(self) :
        """ Fonction qui permet de lancer le jeu du Pendu
            Entrée(s): None
            Sortie(s): None
        """
        jeu = HangmanGame()
        #fenetre = jeu.
        #subprocess.run (["python", "jeu_du_pendu/game.py"])

    def mastermind(self) :
        """ Fonction qui permet de lancer le jeu Mastermind
            Entrée(s): None
            Sortie(s): None
        """
        subprocess.run (["python", "mastermind/game.py"])

    ### ----- Fonctions utiles pour life_game -----

    def life_game(self) :
        """ Fonction qui permet de lancer le jeu de la Vie
            Entrée(s): None
            Sortie(s): None
        """
        # Demande la taille de la fenêtre de jeu à génération aléatoire
        ask_window = Toplevel (self.window)
        ask_window.title ("Taille de la fenêtre")
        ask_window.geometry("350x210+585+270")  # Définir la taille de la nouvelle fenêtre

        vertical_label = Label (ask_window, text = "Entrez le nombre de cellules sur la verticale :")
        vertical_label.pack (padx = 10, pady = 5)
        vertical_label = Label (ask_window, text = "Ne pas dépasser 75 cellules verticales")
        vertical_label.pack()
        vertical_entry = Entry (ask_window)
        vertical_entry.pack (padx = 10, pady = 5)
        vertical_entry.focus_set() # permet de mettre le curseur de l'utilisateur sur la première cellule

        horizontal_label = Label (ask_window, text = "Entrez le nombre de cellules sur l'horizontale :")
        horizontal_label.pack (padx = 10, pady = 5)
        vertical_label = Label (ask_window, text = "Ne pas dépasser 200 cellules horizontales")
        vertical_label.pack()
        horizontal_entry = Entry (ask_window)
        horizontal_entry.pack (padx = 10, pady = 5)

        submit_button = Button (ask_window, text = "Soumettre", command = lambda : self.on_button_click (ask_window, vertical_entry, horizontal_entry))
        submit_button.pack (padx = 10, pady = 10)

        # Liaison de la touche Entrée à la fonction on_button_click
        ask_window.bind('<Return>', lambda event : self.on_button_click (ask_window, vertical_entry, horizontal_entry))

    def vhinfos (self, ask_window, vertical_entry, horizontal_entry) :
        """ Fonction qui regarde si les données entrées sont bien des nombres, sachant que les données sont
            la taille horizontalement et verticalement de la fenêtre
            Entrée(s): ask_window (fenêtre)
                    vertical_entry
                    horizontal_entry
            Sortie(s): vertical_cells (int)
                    horizontal_cells (int)
        """
        global vertical_cells, horizontal_cells

        vertical = vertical_entry.get()
        horizontal = horizontal_entry.get()
        if vertical.isdigit() and horizontal.isdigit() :
            vertical_cells = int(vertical)
            horizontal_cells = int(horizontal)
        else :
            messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")
            ask_window.destroy()
    
    def on_button_click (self, ask_window, vertical_entry, horizontal_entry) :
        """ Fonction appelée sur le clic du bouton et appelle la fonction vhinfos
            Entrée(s): ask_window (fenêtre)
                    vertical_entry
                    horizontal_entry
            Sortie(s): None
        """
        self.vhinfos (ask_window, vertical_entry, horizontal_entry)

        if isinstance(vertical_cells, int) == True and isinstance(horizontal_cells, int) == True :
            ask_window.destroy()
            subprocess.run (["python", "jeu_de_la_vie/jeu_de_la_vie_aleatoire.py", str(vertical_cells), str(horizontal_cells)])
