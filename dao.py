import json
import xmltodict
from abc import ABC, abstractmethod

class DAOJson:

    @abstractmethod
    def readPC(self, **args):
        with open('./file/data.json') as json_data:
            json_parsed = json.loads(json_data.read())
            for p in json_parsed:
                if p['computador']['marca'] == args['marca']:
                    print(p['computador']['descripcion'])

    @abstractmethod
    def readPartes(self, **args):
        with open('./file/data.json') as json_data:
            json_parsed = json.loads(json_data.read())
            for p in json_parsed:
                if p['computador']['marca'] == args['part']:
                    print(p['partes']['memoria'], p['partes']['procesador'], p['partes']['board'], p['partes']['placaRefrigeradora'], p['partes']['quemadorCD'], p['partes']['tarjetaGrafica'])
                if p['partes']['memoria'] == args['part'] or p['partes']['procesador'] == args['part'] or p['partes']['board'] == args['part'] or p['partes']['placaRefrigeradora'] == args['part'] or p['partes']['quemadorCD'] == args['part'] or p['partes']['tarjetaGrafica'] == args['part'] :
                    print(p['partes']['memoria'], p['partes']['procesador'], p['partes']['board'], p['partes']['placaRefrigeradora'], p['partes']['quemadorCD'], p['partes']['tarjetaGrafica'])
                    break

class DAOXml:

    @abstractmethod
    def readPC(self, **args):
        with open('./file/data.xml') as xml_data:
            xml_parsed = xmltodict.parse(xml_data.read())
            for elem in xml_parsed['root']['row']:
                if str(elem['computador']["marca"]) == args["marca"]:
                    print(elem['computador']['descripcion'])

    @abstractmethod
    def readPartes(self, **args):
        with open('./file/data.xml') as xml_data:
            xml_parsed = xmltodict.parse(xml_data.read())
            for elem in xml_parsed['root']['row']:
                if str(elem['computador']["marca"]) == args["partes"]:
                    print(elem['partes']['memoria'], elem['partes']['procesador'], elem['partes']['board'] )

