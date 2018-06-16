#!/usr/bin/python3
# coding: utf-8

import threading, pygame

from project.view.windowRobot import Robot
from project.model.dao.data import Data
from project.model.vo.movement import Movement
from project.model.vo.initialData import InitialData
from project.model.connection.connectSerial import ConnectSerial


def __recordMovements(window):
    pygame.init()
    robot = Robot.getInstance(window)
    clock = pygame.time.Clock()
    lastMovement = "inicio"

    data = Data()
    initialData = InitialData()
    initialData.posX = str(robot.posX)
    initialData.posY = str(robot.posY)
    initialData.m = str(robot.m)
    initialData.b = str(robot.b)
    initialData.orientation = str(robot.orientation)
    initialData.angle = str(robot.angle)
    initialData.lastPz = str(robot.lastPincer)
    initialData.lastMv = str(robot.lastMovement)
    initialData.rotation = str(robot.rotation)

    data.setInitialData(initialData)



    while window.grabando:
        if lastMovement == 'inicio':
            clock.tick()

            if robot.lastMovement == None:
                robot.lastMovement = window.obtenerKeyEvent(Robot.getInstance(window).stop)
            if robot.lastPincer == None:
                robot.lastPincer = window.obtenerKeyEvent(Robot.getInstance(window).closePincer)

            lastMovement = robot.lastMovement
            lastPincer = robot.lastPincer
        else:
            if robot.lastMovement != lastMovement or robot.lastPincer != lastPincer:
                clock.tick()
                timeMovement = clock.get_time()
                movement = Movement()
                movement.time= str(timeMovement)
                movement.movement = lastMovement
                movement.pincer = lastPincer

                data.addMovement(movement)
                print("se gravo  movimiento : {}, pinzas : {},  con tiempo  {}".format(lastMovement, lastPincer, timeMovement))
                lastMovement, lastPincer = robot.lastMovement, robot.lastPincer
    else:
        clock.tick()
        timeMovement = clock.get_time()
        movement = Movement()
        movement.time = str(timeMovement)
        movement.movement = lastMovement
        movement.pincer = lastPincer

        data.addMovement(movement)
        print("se gravo  movimiento : {}, pinzas : {},  con tiempo  {}".format(lastMovement, lastPincer, timeMovement))

    doc = data.getXmlSerialized()
    # chequear esto
    window.dialogoS.setObjeto(doc)
    window.dialogoS.exec()

    print("se termino de grabar")
    pygame.quit()

def recordMovements(window):
    threadOfMovements = threading.Thread(target=__recordMovements, args=(window,))
    threadOfMovements.setDaemon(True)
    threadOfMovements.start()


def __playMovements(window, route):
    port = window.port
    conex = ConnectSerial.getInstance(port)

    pygame.init()
    robot = Robot.getInstance(window)
    print(route)
    objectXML = Data.readXML(route)
    robot.posX = float(objectXML.getInitialData().posX)
    robot.posY = float(objectXML.getInitialData().posY)
    robot.m = float(objectXML.getInitialData().m)
    robot.b = float(objectXML.getInitialData().b)
    robot.orientation = objectXML.getInitialData().orientation
    robot.angle = float(objectXML.getInitialData().angle)
    robot.lastMovement = objectXML.getInitialData().lastMv
    robot.lastPincer = objectXML.getInitialData().lastPz
    robot.rotation = float(objectXML.getInitialData().rotation)

    robot.move(robot.posX, robot.posY)



    for mov in objectXML.getListOfMovements():
        realTime = pygame.time.get_ticks()

        end = realTime + int(mov.time)
        window.keys[mov.movement]()
        window.keys[mov.pincer]()

        # aqui vamos a enviar al Robot los signals

        conex.setDato(mov.movement)
        conex.setDato(mov.pincer)

        while True:
            if pygame.time.get_ticks() >= end:
                break
    print("esto es todo")
    pygame.quit()

# evento
def playMovements(clase, ruta):
    threadPlayMovements = threading.Thread(target=__playMovements, args=(clase, ruta))
    threadPlayMovements.setDaemon(True)
    threadPlayMovements.start()


def __monitorMovements(window):
    port  = window.port
    conex = ConnectSerial.getInstance(port)

    dataObject = Data()
    initialData = InitialData()
    initialData.posX = '558'
    initialData.posY = '384'
    initialData.m = '0'
    initialData.b = '384'
    initialData.orientation = "o"
    initialData.angle = '0'
    initialData.lastMv = "X"
    initialData.lastPz = "T"
    initialData.rotation = '0'

    dataObject.setInitialData(initialData)
    codeSend = 77
    conex.setDato(chr(codeSend))
    mov = "X"
    pinc = "T"
    while True:
        datoConecction = conex.getDato()
        dataSerial, timeSerial = datoConecction.split('_')
        if dataSerial == "termino":
            break
        else:
            movement = Movement()

            if dataSerial == 'T' or dataSerial == 'R':
                pinc = dataSerial
            else:
                mov = dataSerial

            movement.time = timeSerial
            movement.movement = mov
            movement.pincer = pinc

            dataObject.addMovement(movement)

    doc = dataObject.getXmlSerialized()

    window.dialogoS.setObjeto(doc)
    window.dialogoS.exec()

    print("terinmo de monitorear")


def monitorMovements(window):
    threadOfMonitor = threading.Thread(target=__monitorMovements, args=(window,))
    threadOfMonitor.setDaemon(True)
    threadOfMonitor.start()

