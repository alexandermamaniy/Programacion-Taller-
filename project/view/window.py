#!/usr/bin/python3
# -*- coding: utf-8 -*-

import threading

import pygame
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from project.view.windowRobot import Robot
from project.controller.events import Event
from project.view.windowSaveFileXML import DialogSaveXML


class Window(QMainWindow, Event):

    def __init__(self, port):
        super(QMainWindow, self).__init__()

        pygame.init()
        routeImages = "../../resources/imagenes/"
        tittleWindow = "Project Robot"
        routeOfFileUI = "../../resources/archivosUi/proyecto.ui"
        widthGraphicR = pygame.display.Info().current_w
        heightGraphicR = pygame.display.Info().current_h
        uic.loadUi( routeOfFileUI ,self)
        self.port = port
        self.setWindowTitle(tittleWindow)
        self.setGeometry(0, 0, widthGraphicR, heightGraphicR)
        self.graphicV.setGeometry(100,100,widthGraphicR-450,heightGraphicR-200)
        robot =  Robot.getInstance(self)
        robot.uploadImageRobot(routeImages, 'auto1')
        robot.show()

        #self.imprimir = threading.Thread(target=self.informacion, args=(robot,))
        #self.imprimir.setDaemon(True)

        self.grabando = False
        self.loadKeysPressed()
        self.loadButtonClicked()
        self.monitoreando = False

        self.dialogoS = DialogSaveXML(self)



    def closeEvent(self,event):
        resultado = QMessageBox.question(self,"salir...","seguro que quieres salir ?", QMessageBox.Yes | QMessageBox.No )
        if resultado == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
