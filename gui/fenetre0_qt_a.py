'''
Simple fenêtre imitant tk pour la boucle
'''

import PyQt4.QtGui as gui

class MyApp(gui.QApplication):
    def __init__(self):
        super().__init__([])

    def mainloop(self):
        self.exec_()


app = MyApp()

fenetre = gui.QWidget()
fenetre.show()

app.mainloop()
