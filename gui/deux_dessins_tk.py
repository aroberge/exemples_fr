'''Adapted from Swinner, p: 88'''

import tkinter as tk

def dessiner_cercle(x, y, r, couleur='black'):
    '''tracé d'un cercle de centre (x, y) et de rayon r'''
    canevas.create_oval(x-r, y-r, x+r, y+r, outline=couleur)

def figure_1():
    '''dessiner une cible'''

    canevas.delete(tk.ALL)  # efface dessin existant
    canevas.create_line(100, 0, 100, 200, fill='blue')
    canevas.create_line(0, 100, 200, 100, fill='blue')

    rayon = 15

    while rayon < 100:
        dessiner_cercle(100, 100, rayon)
        rayon += 15

def figure_2():
    '''dessiner une caricature de visage'''
    canevas.delete(tk.ALL)
    cercles = [[100, 100, 80, 'red'],  # visage
          [70, 70, 15, 'blue'],   # yeux
          [130, 70, 15, 'blue'],
          [70, 70, 5, 'black'],
          [130, 70, 5, 'black'],
          [44, 115, 20, 'red'],   # joues
          [156, 115, 20, 'red'],
          [100, 95, 15, 'purple'],  # nez
          [100, 145, 30, 'purple']]  # bouche

    for cercle in cercles:
        dessiner_cercle(*cercle)  # cerc[0], cerc[1], cerc[2], cerc[3])

fenetre = tk.Tk()
canevas = tk.Canvas(fenetre, width=200, height=200, bg='ivory')
canevas.pack()

bouton1 = tk.Button(fenetre, text="cible", command=figure_1)
bouton1.pack(side=tk.LEFT, padx=3, pady=3)
bouton2 = tk.Button(fenetre, text="visage", command=figure_2)
bouton2.pack(side=tk.RIGHT, padx=3, pady=3)

fenetre.mainloop()
