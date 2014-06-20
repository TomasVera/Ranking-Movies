# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movies.ui'
#
# Created: Thu Jun 12 12:33:10 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(465, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btn_up = QtGui.QPushButton(self.widget)
        self.btn_up.setObjectName("btn_up")
        self.horizontalLayout.addWidget(self.btn_up)
        self.btn_down = QtGui.QPushButton(self.widget)
        self.btn_down.setObjectName("btn_down")
        self.horizontalLayout.addWidget(self.btn_down)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 2)
        self.table_movies = QtGui.QTableView(self.centralwidget)
        self.table_movies.setMaximumSize(QtCore.QSize(850, 16777215))
        self.table_movies.setObjectName("table_movies")
        self.gridLayout.addWidget(self.table_movies, 1, 0, 1, 1)
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_imagen = QtGui.QLabel(self.widget_2)
        self.lbl_imagen.setObjectName("lbl_imagen")
        self.verticalLayout.addWidget(self.lbl_imagen)
        self.label_3 = QtGui.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lbl_reparto = QtGui.QLabel(self.widget_2)
        self.lbl_reparto.setWordWrap(True)
        self.lbl_reparto.setObjectName("lbl_reparto")
        self.verticalLayout.addWidget(self.lbl_reparto)
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.lbl_descripcion = QtGui.QLabel(self.widget_2)
        self.lbl_descripcion.setWordWrap(True)
        self.lbl_descripcion.setObjectName("lbl_descripcion")
        self.verticalLayout.addWidget(self.lbl_descripcion)
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ranking de peliculas", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ranking:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_up.setText(QtGui.QApplication.translate("MainWindow", "Subir", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_down.setText(QtGui.QApplication.translate("MainWindow", "Bajar", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_imagen.setText(QtGui.QApplication.translate("MainWindow", "imagen", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Reparto: ", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_reparto.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_descripcion.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

