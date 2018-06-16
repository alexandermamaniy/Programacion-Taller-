import time
from PyQt5.QtWidgets import QDialog,QTreeWidgetItem
from PyQt5 import uic
import os
from project.model.dao.data import Data


class DialogSaveXML(QDialog):


    def __init__(self, window):

        QDialog.__init__(self)
        routeOfTheFileUI = "../../resources/archivosUi/saveXML.ui"

        uic.loadUi(routeOfTheFileUI, self)
        self.window = window
        self.historial = os.getcwd().split(os.sep)
        self.directorio.itemDoubleClicked.connect(self.openElement)
        self.back.clicked.connect(self.backHistory)
        self.changeDir()
        self.getDir()
        self.open.clicked.connect(self.saveFileXML)
        self.cancel.clicked.connect(self.cancelFileXML)

    def setObjeto(self, objectXML):
        self.objectXML = objectXML
        #self.changeDir()
        self.getDir()

    def cancelFileXML(self):
        self.close()

    def saveFileXML(self):
        # item = self.directorio.currentItem()
        routeOfFileXML = "{}{}{}".format(self.stackOfDirectories[-1], os.path.sep, self.ruta.text())
        Data.saveXML(self.objectXML, routeOfFileXML)
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

        # Eliminamos todas la filas de la busqueda anterior

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

                    # datas of the fields del directorio
                    row = [name, date, tipo, size]

                    # add a row to we directorio
                    self.directorio.insertTopLevelItem(0, QTreeWidgetItem(self.directorio, row))


    def openElement(self):

        # get the item selected
        item = self.directorio.currentItem()

        # create the route accesing to filed name of the element( directory, file )
        elementSelected = "{}{}{}".format(self.stackOfDirectories[-1], os.path.sep, item.text(0))

        if os.path.isdir(elementSelected):

            self.historial = elementSelected.split(os.sep)
            self.changeDir()
            self.getDir()
        else:
            pass




