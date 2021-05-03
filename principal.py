from fabricas import *

opcion = input("Digite marca de computador para comprar \n")

fabricas = FabricaJson()
# fabricas = FabricaXml()

pc = fabricas.crearPC()
pc.readPC(marca=opcion)

parts = fabricas.crearPartes()
parts.readPartes(partes=opcion)