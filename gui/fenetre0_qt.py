'''
Simple fenêtre
'''

import PyQt4.QtGui as gui

app = gui.QApplication([])

fenetre = gui.QWidget()  # autres choix possibles
fenetre.show()

app.exec_()
