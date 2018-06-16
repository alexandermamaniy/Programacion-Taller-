#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Movement():
    def __init__(self):
        self.__time = None
        self.__movement = None
        self.__pincer = None

    # setters of atrribs
    def __settime(self, timeM):
        self.__time = timeM

    def __setmovement(self, movement):
        self.__movement = movement

    def __setpincer(self, pincer):
        self.__pincer = pincer

    # getters of at
    def __gettime(self):
        return self.__time

    def __getmovement(self):
        return self.__movement

    def __getpincer(self):
        return self.__pincer

    # properties of attrib
    time = property(fget=__gettime, fset=__settime)
    movement = property(fget=__getmovement, fset=__setmovement)
    pincer = property(fget=__getpincer, fset=__setpincer)