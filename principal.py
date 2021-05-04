from fabricas import *

# fabricas = ''
# opt = input("1. Json \n2. XML \n")
# if opt == 1:
#     fabricas = FabricaJson()
# if opt == 2:
#     fabricas = FabricaXml()
# fabricas = FabricaJson()
fabricas = FabricaXml()

opcion = input("1. Descripcion del PC \n2. Imprimir Partes \n3. Parte del PC \n")
if opcion == 1:
    brand = input("Digite marca de computador para comprar \n")
    pc = fabricas.crearPC()
    pc.readPC(marca=brand)

if opcion == 2:
    brand = input("Digite marca de computador para comprar \n")
    parts = fabricas.crearPartes()
    parts.readPartes(part=brand)

else:
    parte = input("Digite parte del PC \n")
    parts = fabricas.crearPartes()
    parts.readPartes(part=parte)
