#!/usr/bin/python3
# -*- coding: utf-8 -*-

class InitialData():
    def __init__(self):
        self.__posX = None
        self.__posY = None
        self.__m = None
        self.__b = None
        self.__orientation = None
        self.__angle = None
        self.__lastPz = None
        self.__lastMv = None
        self.__rotation = None

    # getters of attribs
    def __getposX(self):
        return self.__posX

    def __getposY(self):
        return self.__posY

    def __getm(self):
        return self.__m

    def __getb(self):
        return self.__b

    def __getorientation(self):
        return self.__orientation

    def __getangle(self):
        return self.__angle

    def __getlastPz(self):
        return self.__lastPz

    def __getlastMv(self):
        return self.__lastMv

    def __getrotation(self):
        return self.__rotation


    # setters of attribs

    def __setposX(self, posX):
        self.__posX = posX

    def __setposY(self, posY):
        self.__posY = posY

    def __setm(self, m):
        self.__m = m

    def __setb(self, b):
        self.__b = b

    def __setorientation(self, orientation):
        self.__orientation = orientation

    def __setangle(self, angle):
        self.__angle = angle

    def __setlastPz(self, lastPz):
        self.__lastPz = lastPz

    def __setlastMv(self, lastMv):
        self.__lastMv = lastMv

    def __setrotation(self, rotation):
        self.__rotation = rotation


    # properties of attrib
    posX = property(fget=__getposX, fset=__setposX)
    posY = property(fget=__getposY, fset=__setposY)
    m = property(fget=__getm, fset=__setm)
    b = property(fget=__getb, fset=__setb)
    orientation = property(fget=__getorientation, fset=__setorientation)
    angle = property(fget=__getangle, fset=__setangle)
    lastPz = property(fget=__getlastPz, fset=__setlastPz)
    lastMv = property(fget=__getlastMv, fset=__setlastMv)
    rotation = property(fget=__getrotation, fset=__setrotation)



