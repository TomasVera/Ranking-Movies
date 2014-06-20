#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from ui_movies import Ui_MainWindow
import controlador


class Movies(QtGui. QMainWindow):

    table_columns = (
        (u"Título", 200),
        (u"Año", 100),
        (u"Director", 150),
        (u"País", 100),
        (u"Ranking", 75))

    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_movies()
        self.show()

        self.ui.btn_up.clicked.connect(self.action_up)
        self.ui.btn_down.clicked.connect(self.action_down)

    def load_movies(self):
        movies = controlador.get_movies()
        rows = len(movies)
        model = QtGui.QStandardItemModel(
            rows, len(self.table_columns))
        self.ui.table_movies.setModel(model)
        self.ui.table_movies.horizontalHeader().setResizeMode(
            0, self.ui.table_movies.horizontalHeader().Stretch)

        for col, h in enumerate(self.table_columns):
            model.setHeaderData(col, QtCore. Qt.Horizontal, h[0])
            self.ui.table_movies.setColumnWidth(col, h[1])

        for i, data in enumerate(movies):
            row = [data[1], data[3], data[4], data[5], data[8]]
            for j, field in enumerate(row):
                index = model.index(i, j, QtCore. QModelIndex())
                model.setData(index, field)
            #parametro oculto
            model.item(i).mov = data

    def action_up(self):
        self.update_rank("Up")

    def action_down(self):
        self.update_rank("Down")

    def update_rank(self, action):
        model = self.ui.table_movies.model()
        index = self.ui.table_movies.currentIndex()
        if index.row() == -1:
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una Pelicula")
        else:
            rank = model.index(index.row(), 4, QtCore.QModelIndex()).data()
            movie = controlador.get_rank(rank)
            old_rank = int(movie[0]['ranking'])
            if(action == "Up"):
                new_rank = old_rank - 1
            elif(action == "Down"):
                new_rank = old_rank + 1
            if(new_rank == 0):
                self.errorMessageDialog = QtGui.QErrorMessage(self)
                self.errorMessageDialog.showMessage("No se puede subir el ranking a esta película")
            elif(new_rank > 7):
                self.errorMessageDialog = QtGui.QErrorMessage(self)
                self.errorMessageDialog.showMessage("No se puede bajar más el ranking a esta película")
            else:
                movie1 = controlador.get_rank(new_rank)
                controlador.update(movie[0]['title'], new_rank)
                if(movie1):
                    controlador.update(movie1[0]['title'], old_rank)
                self.load_movies()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Movies()
    sys.exit(app.exec_())