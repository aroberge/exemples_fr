'''Swinnen damier - exercice 8.9'''

import tkinter as tk
import random

side = 20


def dessiner_pion(i, j):
    '''tracé d'un cercle de centre (x, y) et de rayon r'''
    dia = side - 2
    x = i * side + 1
    y = j * side + 1
    canevas.create_oval(x, y, x+dia, y+dia, fill='red', outline="blue")


def dessine_case_bleue(x, y):
    '''dessine une case bleue pour le damier'''
    canevas.create_rectangle(x, y, x+side, y+side, fill="blue",
                outline="blue")


def dessine_damier():
    '''dessiner un damier'''

    canevas.delete(tk.ALL)
    for i in range(9):
        for j in range(10):
            if (i + j) % 2 == 0:
                x = i*side
            else:
                x = (i+1)*side
            y = j*side
            dessine_case_bleue(x, y)


def ajoute_pions():
    '''dessine un certain nombre de pions'''
    nb_pions = random.randint(1, 10)
    dessine_damier()
    for _ in range(nb_pions):
        j = random.randint(0, 9)
        i = random.randint(0, 4)
        i *= 2
        if j % 2 == 1:
            i += 1

        dessiner_pion(i, j)


fenetre = tk.Tk()
canevas = tk.Canvas(fenetre, width=10*side, height=10*side, bg='white')
canevas.pack()

bouton1 = tk.Button(fenetre, text="damier", command=dessine_damier)
bouton1.pack(side=tk.LEFT, padx=3, pady=3)
bouton2 = tk.Button(fenetre, text="pions", command=ajoute_pions)
bouton2.pack(side=tk.RIGHT, padx=3, pady=3)

fenetre.mainloop()
