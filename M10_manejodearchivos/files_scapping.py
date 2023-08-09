import os

ingredientes = ["Cebolla","Tomate", "Aceite"]

archivo = open('datos.txt','w')

for elemento in ingredientes:
    archivo.write(elemento+'\n')

archivo.close()

archivo = open('datos.txt','r')


for linea in archivo:
    print(linea)


archivo.close()