#!/usr/bin/python
import sys
import os


class Constants:


    def __init__(self):
        self.__OK = 0
        self.__FAIL = 1
        self.__ERROR = -1
        self.__NODATA = 100
        self.__GLOBALCONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)),"config","globalConfig.properties")
        self.__ORIGIN_PATH = '/home/daniel/Desktop/Projects/postgresqlTasksManager/Origin'
        self.__DESTINY_PATH = '/home/daniel/Desktop/Projects/postgresqlTasksManager/Destiny'
        self.__ITER = 1000
        self.__DB_URL = 'postgresql://admin:admin@localhost:5432/pruebas'

    @property
    def OK(self):

        return self.__OK

    @property
    def ERROR(self):

        return self.__ERROR

    @property
    def NODATA(self):

        return self.__SINDATOS

    @property
    def FAIL(self):

        return self.__FALLO

    @property
    def GLOBALCONFIG(self):

        return self.__GLOBALCONFIG

    @property
    def ORIGIN_PATH(self):

        return self.__ORIGIN_PATH

    @property
    def DESTINY_PATH(self):

        return self.__DESTINY_PATH

    @property
    def ITER(self):

        return self.__ITER
    
    @property
    def DB_URL(self):

        return self.__DB_URL


        
        
        