import time
from PyQt5.QtWidgets import QDialog,QTreeWidgetItem
from PyQt5 import uic
import os
from project.controller.actions import playMovements


class DialogOpenXML(QDialog):
    """
    window que nos permite crear un dialgo, donde estamos probando como funciona los QListWidget
    """
    def __init__(self, window):

        QDialog.__init__(self)

        routeOfTheFileUI = "../../resources/filesUI/openXML.ui"
        uic.loadUi(routeOfTheFileUI, self)
        self.window = window

        self.historial = os.getcwd().split(os.sep)
        self.directorio.itemDoubleClicked.connect(self.openElement)
        self.back.clicked.connect(self.backHistory)
        self.changeDir()
        self.getDir()
        self.open.clicked.connect(self.openFileXML)
        self.cancel.clicked.connect(self.cancelFileXML)

    def cancelFileXML(self):
        self.close()

    def openFileXML(self):
        item = self.directorio.currentItem()
        routeOfFileXML = "{}{}{}".format(self.stackOfDirectories[-1], os.path.sep, item.text(0))

        playMovements(self.window, routeOfFileXML)
        self.close()

    def changeDir(self):

        self.stackOfDirectories = [os.sep.join(self.historial[:i]) for i in range(2, len(self.historial) + 1)]
        self.history.clear()
        for i in self.stackOfDirectories[::-1]:
            self.history.addItem(i)



    def backHistory(self):
        self.historial = self.historial[:-1]
        self.changeDir()
        self.getDir()


    def keyPressEvent(self, e):

        keyReturn = 16777219
        keyEnter = 16777220

        if e.key() == keyReturn:
            self.backHistory()

        if e.key() == keyEnter:
            self.openElement()

    def getDir(self):

        self.directorio.clear()

        dir = self.stackOfDirectories[-1]

        if os.path.isdir(dir):
            for element in os.scandir(dir):

                if os.path.isdir(element.path) or element.name.endswith(".xml"):

                    name = str(element.name)

                    size = str(element.stat().st_size)

                    # ultima fecha de modificacion
                    date = str(time.ctime(element.stat().st_mtime))

                    if os.path.isdir(element.path):
                        tipo = "carpeta de archivos"
                    elif os.path.isfile(element.path):
                        tipo = "archivo"
                    elif os.path.islink(element.path):
                        tipo = "Link"

                    row = [name, date, tipo, size]

                    self.directorio.insertTopLevelItem(0, QTreeWidgetItem(self.directorio, row))



    def openElement(self):

        # obtenemos el item selecionado
        item = self.directorio.currentItem()

        # creamos la ruta accediendo al nombre del elemento(carpeta archivo)
        elementSelected = "{}{}{}".format(self.stackOfDirectories[-1], os.path.sep, item.text(0))

        if os.path.isdir(elementSelected):

            self.historial = elementSelected.split(os.sep)
            self.changeDir()
            self.getDir()
        else:
            self.openFileXML()



