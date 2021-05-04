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
                if p['partes']['memoria'] == args['part']:
                    print(p['partes']['memoria'], p['computador']['marca'])
                    break
                if p['partes']['procesador'] == args['part']:
                    print(p['partes']['procesador'], p['computador']['marca'])
                    break
                if p['partes']['board'] == args['part']:
                    print(p['partes']['board'], p['computador']['marca'])
                    break
                if p['partes']['placaRefrigeradora'] == args['part']:
                    print(p['partes']['placaRefrigeradora'], p['computador']['marca'])
                    break
                if p['partes']['quemadorCD'] == args['part']:
                    print(p['partes']['quemadorCD'], p['computador']['marca'])
                    break
                if p['partes']['tarjetaGrafica'] == args['part']:
                    print(p['partes']['tarjetaGrafica'], p['computador']['marca'])
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
                if str(elem['computador']["marca"]) == args["part"]:
                    print(elem['partes']['memoria'], elem['partes']['procesador'], elem['partes']['board'], elem['partes']['placaRefrigeradora'], elem['partes']['quemadorCD'], elem['partes']['tarjetaGrafica'])
                if str(elem['partes']['memoria']) == args['part']:
                    print(elem['partes']['memoria'], elem['computador']['marca'])
                    break
                if str(elem['partes']['procesador']) == args['part']:
                    print(elem['partes']['procesador'], elem['computador']['marca'])
                    break
                if str(elem['partes']['board']) == args['part']:
                    print(elem['partes']['board'], elem['computador']['marca'])
                    break
                if str(elem['partes']['placaRefrigeradora']) == args['part']:
                    print(elem['partes']['placaRefrigeradora'], elem['computador']['marca'])
                    break
                if str(elem['partes']['quemadorCD']) == args['part']:
                    print(elem['partes']['quemadorCD'], elem['computador']['marca'])
                    break
                if str(elem['partes']['tarjetaGrafica']) == args['part']:
                    print(elem['partes']['tarjetaGrafica'], elem['computador']['marca'])
                    break

