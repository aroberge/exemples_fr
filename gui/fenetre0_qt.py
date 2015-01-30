# -*- coding: utf-8 -*-
'''Simple fenêtre'''

import PyQt4.QtGui as gui

app = gui.QApplication([])

fenetre = gui.QWidget()
fenetre.show()

app.exec_()
