'''Adapted from Swinner, p: 88; class based version'''

import tkinter as tk

class DeuxDessins(tk.Tk):

    def __init__(self):
        super().__init__()
        self.creation()
        self.positionnement()


    def creation(self):
        '''création des différents widgets '''
        self.canevas = tk.Canvas(self, width=200, height=200, bg='ivory')
        self.bouton1 = tk.Button(self, text="cible", command=self.figure_1)
        self.bouton2 = tk.Button(self, text="visage", command=self.figure_2)


    def positionnement(self):
        '''positionnement des widgets'''
        self.canevas.pack()
        self.bouton1.pack(side=tk.LEFT, padx=3, pady=3)
        self.bouton2.pack(side=tk.RIGHT, padx=3, pady=3)


    def dessiner_cercle(self, x, y, r, couleur='black'):
        '''tracé d'un cercle de centre (x, y) et de rayon r'''
        self.canevas.create_oval(x-r, y-r, x+r, y+r, outline=couleur)


    def effacer_tout(self):
        '''efface tout ce qui se trouve sur le canevas'''
        self.canevas.delete(tk.ALL)


    def figure_1(self):
        '''dessiner une cible'''
        self.effacer_tout()
        self.canevas.create_line(100, 0, 100, 200, fill='blue')
        self.canevas.create_line(0, 100, 200, 100, fill='blue')
        rayon = 15
        while rayon < 100:
            self.dessiner_cercle(100, 100, rayon)
            rayon += 15


    def figure_2(self):
        '''dessiner une caricature de visage'''
        self.effacer_tout()
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
            self.dessiner_cercle(*cercle)


if __name__ == '__main__':
    fenetre = DeuxDessins()
    fenetre.mainloop()
