# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk

class MastermindGame :
    """
    """

    def __init__(self):
        """
        """
        # Création de la fenêtre et de son nom
        self.window = Tk()
        self.window.title ("Mastermind")

        # Dimensions du canevas
        self.width = 1535
        self.height = 780
        self.window.geometry(f"{self.width}x{self.height}+{-10}+0")

        # Création du canevas    
        self.Canevas = Canvas (self.window, width = self.width, height = self.height, bg = 'gray')
        self.Canevas.grid()

        # Récupération et ajustement de l'image de fond des frames
        self.back_pic = Image.open ("images/dominos_pions_dés.jpg")
        self.resized = self.back_pic.resize ((1535, 780))
        self.background = ImageTk.PhotoImage (self.resized)
        self.Canevas.create_image(0, 0, image = self.background, anchor = NW)

        self.window.mainloop()