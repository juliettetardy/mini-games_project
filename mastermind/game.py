# Importation des fichiers et/ou bibliothèque(s) nécessaire(s) au fonctionnement du jeu
from tkinter import Tk, Canvas, NW
from PIL import Image, ImageTk

window = Tk()
window.title ("Mastermind")

w = 1535
h = 780
window.geometry(f"{w}x{h}+{-10}+0")
Canevas = Canvas (window, width = w, height = h, bg = 'gray')
Canevas.grid()

# Récupération et ajustement de l'image de fond des frames
back_pic = Image.open ("images/dominos_pions_dés.jpg")
resized = back_pic.resize ((1535, 780))
background = ImageTk.PhotoImage (resized)
Canevas.create_image(0, 0, image = background, anchor = NW)

window.mainloop()