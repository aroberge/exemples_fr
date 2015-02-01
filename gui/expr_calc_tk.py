'''Adapté d'un exemple de Swinnen'''

import tkinter as tk
from math import *

def evaluer(event):
    chaine.configure(text="Résultat = " + str(eval(entree.get())))

fenetre = tk.Tk()
entree = tk.Entry(fenetre)
entree.bind("<Return>", evaluer)
chaine = tk.Label(fenetre)
entree.pack()
chaine.pack()

fenetre.mainloop()
