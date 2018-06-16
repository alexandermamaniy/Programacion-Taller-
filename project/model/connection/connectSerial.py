#!/usr/bin/python3
# -*- coding: utf-8 -*-

import serial, threading

class ConnectSerial():
    connection = None


    def __init__(self, port):
        self.__connection = serial.Serial(port, 9600)


    def getDato(self):
        dataSerial = self.__connection.readline().decode("utf-8").strip()
        return dataSerial

    def __sendData(self, message):
        data = bytes(message, "utf-8")
        self.__connection.write(data)

    def setDato(self, message):
        threadOfSendOfData = threading.Thread(target=self.__sendData, args=(message,))
        threadOfSendOfData.setDaemon(True)
        threadOfSendOfData.start()



    @staticmethod
    def getInstance( port ):
        if ConnectSerial.connection == None:
            ConnectSerial.connection = ConnectSerial(port)
        return ConnectSerial.connection
