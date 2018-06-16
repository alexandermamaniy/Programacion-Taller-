#!/usr/bin/python3
# -*- coding: utf-8 -*-
from lxml import etree
from project.model.vo.initialData import InitialData
from project.model.vo.movement import Movement

class Data():

    def __init__(self):
        self.__initialData = None
        self.__listOfMovements = []

    def setInitialData(self, initialData):
        self.__initialData = initialData

    def getInitialData(self):
        return self.__initialData

    def getListOfMovements(self):
        return self.__listOfMovements

    def addMovement(self, movement):

        self.__listOfMovements.append(movement)

    def __getObjetXML(self):

        objectX = etree.Element("auto")
        initialData = etree.Element("datos")

        initialData.set('posX', self.__initialData.posX)
        initialData.set('posY', self.__initialData.posY)
        initialData.set('m', self.__initialData.m)
        initialData.set('b', self.__initialData.b)
        initialData.set('orientation', self.__initialData.orientation)
        initialData.set('angle', self.__initialData.angle)
        initialData.set('lastPz', self.__initialData.lastPz)
        initialData.set('lastMv', self.__initialData.lastMv)
        initialData.set('rotation', self.__initialData.rotation)


        objectX.append(initialData)

        for mov in self.__listOfMovements:
            movement = etree.Element("movimiento")
            movement.set('time', mov.time)
            movement.set('movement', mov.movement)
            movement.set('pincer', mov.pincer)
            objectX.append(movement)


        return objectX

    def getXmlSerialized(self):
        objetoXML = self.__getObjetXML()
        doc = etree.ElementTree(objetoXML)
        serialization = etree.tostring(doc, pretty_print=True, xml_declaration=True, encoding="utf-8")

        return serialization

    @staticmethod
    def saveXML(objetXML, route):
        fileXML = open(route, "w")
        fileXML.write(objetXML.decode("utf-8"))
        fileXML.close()

    @staticmethod
    def readXML(route):
        data = Data()
        root = etree.parse(route).getroot()

        initialData = InitialData()
        firstDataXML = root[0]

        initialData.posX = firstDataXML.get('posX')
        initialData.posY = firstDataXML.get('posY')
        initialData.m = firstDataXML.get('m')
        initialData.b = firstDataXML.get('b')
        initialData.orientation = firstDataXML.get('orientation')
        initialData.angle = firstDataXML.get('angle')
        initialData.lastMv = firstDataXML.get('lastMv')
        initialData.lastPz = firstDataXML.get('lastPz')
        initialData.rotation = firstDataXML.get('rotation')

        data.setInitialData(initialData)

        for mov in root[1:]:
            movement = Movement()
            movement.time = mov.get('time')
            movement.movement = mov.get('movement')
            movement.pincer = mov.get('pincer')
            data.addMovement(movement)

        return data


