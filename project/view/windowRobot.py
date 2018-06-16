#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QTransform, QImage
import math, time, threading
from PyQt5 import QtCore

class Robot(QLabel):

    robot = None
    def __init__(self, window):
        super(QLabel,self).__init__(window)
        self.window = window
        self.posX = self.window.graphicV.x() + (self.window.graphicV.width() // 2)
        self.posY = self.window.graphicV.y() + (self.window.graphicV.height() // 2)
        self.angle = 0
        self.m = 0
        self.b = self.posY
        self.orientation = 'o'
        self.rotation = 0

        self.dicMov = {'front': 0,
                    'back': 0,
                    'left': 0,
                    'right': 0,
                    'open':0,
                    'close':0
                       }

        self.statesMovements = {'front':[False, self.__moveFront],
                        'back':[False, self.__moveBack],
                        'rotationPos':[False, self.__rotatePos],
                        'rotationNeg':[False, self.__rotateNeg],
                        'stop':[True, self.__stop]}

        self.statesPincers = {'open':[False, self.__openPincers],
                              'close':[True, self.__closePincers]}

        self.threadOfMovements = threading.Thread(target=self.moveRobot)
        self.threadOfMovements.setDaemon(True)
        self.threadOfMovements.start()
        self.lastMovement = None
        self.lastPincer = None

    def uploadImageRobot(self, routeImage, auto):
        self.image = QImage()
        self.routeImage = routeImage + auto
        self.image.load(self.routeImage + "/cerrar.png")
        pixmap = QPixmap(self.image)
        self.centerX = pixmap.rect().center().x()
        self.centerY = pixmap.rect().center().y()
        diag = (pixmap.width() ** 2 + pixmap.height() ** 2) ** 0.5
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setPixmap(pixmap)
        self.setGeometry(self.posX, self.posY, diag, diag)


    # methods responsible modifies the Images the robot
    def __updateEquationOfTheLine(self):
        angleR = self.angle * (math.pi / 180)
        self.m = math.tan(angleR)
        self.b = self.posY-(self.m*self.posX)
        self.__defineOrientation()

    def __moveImgXPositivo(self):
        self.posX += 3
        self.posY = self.posX * self.m + self.b
        self.move(self.posX, self.posY)

    def __moveImgXNegativo(self):
        self.posX -= 3
        self.posY = self.posX * self.m + self.b
        self.move(self.posX, self.posY)

    def __moveImgYPositivo(self):
        self.posY += 3
        self.posX = (self.posY - self.b) / self.m
        self.move(self.posX, self.posY)

    def __moveImgYNegativo(self):
        self.posY -= 3
        self.posX = (self.posY - self.b) / self.m
        self.move(self.posX, self.posY)

    def __isInTheLimit(self):
        centerX = self.posX + self.centerX
        centerY = self.posY + self.centerY
        return (centerX > self.window.graphicV.x() + 70 and centerY > self.window.graphicV.y() + 50 and centerX < self.window.graphicV.x() + self.window.graphicV.width() - 100 and centerY < self.window.graphicV.y() + self.window.graphicV.height() - 120)


    # methods responsible for defining the orientation of the robot

    def __moveFront(self):
        if (self.angle >= 0 and self.angle <= 45) or (self.angle >= 316 and self.angle <= 360):
            self.__moveImgXPositivo()
            if not self.__isInTheLimit():
                self.__moveImgXNegativo()
        elif (self.angle >= 46 and self.angle <= 135):
            self.__moveImgYPositivo()
            if not self.__isInTheLimit():
                self.__moveImgYNegativo()
        elif (self.angle >= 136 and self.angle <= 225):
            self.__moveImgXNegativo()
            if not self.__isInTheLimit():
                self.__moveImgXPositivo()
        elif (self.angle >= 226 and self.angle <= 315):
            self.__moveImgYNegativo()
            if not self.__isInTheLimit():
                self.__moveImgYPositivo()

    def __moveBack(self):
        if (self.angle >= 0 and self.angle <= 45) or (self.angle >= 316 and self.angle <= 360):
            self.__moveImgXNegativo()
            if not self.__isInTheLimit():
                self.__moveImgXPositivo()
        elif (self.angle >= 46 and self.angle <= 135):
            self.__moveImgYNegativo()
            if not self.__isInTheLimit():
                self.__moveImgYPositivo()
        elif (self.angle >= 136 and self.angle <= 225):
            self.__moveImgXPositivo()
            if not self.__isInTheLimit():
                self.__moveImgXNegativo()
        elif (self.angle >= 226 and self.angle <= 315):
            self.__moveImgYPositivo()
            if not self.__isInTheLimit():
                self.__moveImgYNegativo()

    def __rotatePos(self):

        pixmap = QPixmap(self.image)
        self.rotation += 5.1
        transform = QTransform().rotate(self.rotation)
        pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.setPixmap(pixmap)
        self.angle = math.fabs(self.rotation % 360)
        self.__updateEquationOfTheLine()

    def __rotateNeg(self):
        pixmap = QPixmap(self.image)
        self.rotation -= 5.1
        transform = QTransform().rotate(self.rotation)
        pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.setPixmap(pixmap)
        self.angle = math.fabs(self.rotation % 360)
        self.__updateEquationOfTheLine()

    def __openPincers(self):
        self.image = QImage()
        self.image.load(self.routeImage + "/abrir.png")
        pixmap = QPixmap(self.image)
        transform = QTransform().rotate(self.rotation)
        pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.setPixmap(pixmap)

    def __closePincers(self):
        self.image = QImage()
        self.image.load(self.routeImage + "/cerrar.png")
        pixmap = QPixmap(self.image)
        transform = QTransform().rotate(self.rotation)
        pixmap = pixmap.transformed(transform, QtCore.Qt.SmoothTransformation)
        self.setPixmap(pixmap)


    def __stop(self):
        pass


    # methods that will allow interactive with the graphic interface
    def moveFront(self):

        self.dicMov['front'] +=1

        for key in self.statesMovements.keys():
            if key == 'front':
                self.statesMovements[key][0] = True
            else:
                self.statesMovements[key][0] = False
        self.lastMovement = self.window.obtenerKeyEvent(self.moveFront)


    def moveBack(self):

        self.dicMov['back'] += 1

        for clave in self.statesMovements.keys():
            if clave == 'back':
                self.statesMovements[clave][0] = True
            else:
                self.statesMovements[clave][0] = False

        self.lastMovement = self.window.obtenerKeyEvent(self.moveBack)

    def rotatePos(self):

        self.dicMov['right'] += 1

        for clave in self.statesMovements.keys():
            if clave == 'rotationPos':
                self.statesMovements[clave][0] = True
            else:
                self.statesMovements[clave][0] = False

        self.lastMovement = self.window.obtenerKeyEvent(self.rotatePos)


    def rotateNeg(self):

        self.dicMov['left'] += 1


        for clave in self.statesMovements.keys():
            if clave == 'rotationNeg':
                self.statesMovements[clave][0] = True
            else:
                self.statesMovements[clave][0] = False

        self.lastMovement = self.window.obtenerKeyEvent(self.rotateNeg)


    def stop(self):

        for clave in self.statesMovements.keys():
            if clave == 'stop':
                self.statesMovements[clave][0] = True
            else:
                self.statesMovements[clave][0] = False
        self.lastMovement = self.window.obtenerKeyEvent(self.stop)


    def openPincer(self):

        self.dicMov['open'] += 1

        for clave in self.statesPincers.keys():
            if clave == 'open':
                self.statesPincers[clave][0] = True
            else:
                self.statesPincers[clave][0] = False
        self.lastPincer = self.window.obtenerKeyEvent(self.openPincer)


    def closePincer(self):

        self.dicMov['close'] += 1
        for clave in self.statesPincers.keys():
            if clave == 'close':
                self.statesPincers[clave][0] = True
            else:
                self.statesPincers[clave][0] = False
        self.lastPincer = self.window.obtenerKeyEvent(self.closePincer)


    def moveRobot(self):
        while True:
            time.sleep(.05)
            for value in self.statesMovements.values():
                if value[0]:
                    value[1]()

            for value in self.statesPincers.values():
                if value[0]:
                    value[1]()

    def __defineOrientation(self):
        if self.angle == 0:
            self.orientation = 'o'
        elif self.angle == 90:
            self.orientation = 's'
        elif self.angle == 180:
            self.orientation = 'e'
        elif self.angle == 270:
            self.orientation = 'n'
        elif self.angle >0 and self.angle<90:
            self.orientation = 'so'
        elif self.angle >90 and self.angle<180:
            self.orientation = 'se'
        elif self.angle >180 and self.angle<270:
            self.orientation = 'ne'
        elif self.angle >180 and self.angle<360:
            self.orientation = 'no'

    def information(self):
        print("posX = {}, posY = {}, m = {}, b = {}, angle = {}, orientacio = {}, ultimoMV = {}, lastPincer = {}, rotation = {}".format(self.posX, self.posY, self.m, self.b, self.angle, self.orientation, self.lastMovement, self.lastPincer, self.rotation))

    def getInstance(clase):
        if Robot.robot == None:
            Robot.robot = Robot(clase)
        return Robot.robot
