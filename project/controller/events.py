#!/usr/bin/python3
# coding: utf-8

from project.view.windowRobot import Robot
from project.controller.actions import recordMovements, monitorMovements
from project.view.windowOpenFileXML import DialogOpenXML
from project.model.connection.connectSerial import ConnectSerial
from project.view.windowOfGraphicStad import graphicBar,graphicCake

class Event():
    def __init__(self):
        pass

    def loadKeysPressed(self):
        robot = Robot.getInstance(self)
        self.keys = {'W': robot.moveFront,
                     'S': robot.moveBack,
                     'D': robot.rotatePos,
                     'A': robot.rotateNeg,
                     'X': robot.stop,
                     'R': robot.openPincer,
                     'T': robot.closePincer}

    def loadButtonClicked(self):
        self.grabar.clicked.connect(self.__record)
        self.openD.clicked.connect(self.__openDialog)
        self.monitoreo.clicked.connect(self.__setMonitor)
        self.barra.clicked.connect(self.__graphicTypeBar)
        self.pastel.clicked.connect(self.__graphicTyprCake)

    def __setMonitor(self):
        monitorMovements(self)

    def __openDialog(self):
        self._dialogoO = DialogOpenXML(self)
        self._dialogoO.exec_()


    def __record(self):
        self.grabando = False if self.grabando else True
        if self.grabando:
            recordMovements(self)

    def __graphicTypeBar(self):
        graphicBar(Robot.getInstance(self).dicMov)

    def __graphicTyprCake(self):
        graphicCake(Robot.getInstance(self).dicMov)

    def keyPressEvent(self, e):
        port = self.port
        conexion = ConnectSerial.getInstance(port)
        for tecla in self.keys.keys():
            if e.key() == ord(tecla):
                self.keys[tecla]()
                conexion.setDato(chr(e.key()))


    def obtenerKeyEvent(self, funcion):
        for c,f in self.keys.items():
            if f == funcion:
                return c


