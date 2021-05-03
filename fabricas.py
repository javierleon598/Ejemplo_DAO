from abc import ABC, abstractmethod
from dao import *

class FabricaAbstracta(ABC):

    @abstractmethod
    def crearPC(self, **args):
        pass
    @abstractmethod
    def crearPartes(self, **args):
        pass

class FabricaJson(FabricaAbstracta):

    def crearPC(self, **args):
        return DAOJson()
    def crearPartes(self, **args):
        return DAOJson()

class FabricaXml(FabricaAbstracta):

    def crearPC(self, **args):
        return DAOXml()
    def crearPartes(self, **args):
        return DAOXml()
