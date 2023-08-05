tupla_dias= ('lunes', 'martes', 'miércoles','jueves','viernes','sábado', 'domingo')
print(tupla_dias[1])

x=11
y=22
z='Henry'
mi_tupla= x,y,z
print(mi_tupla)
mi_lista = list(mi_tupla)
print(mi_lista)
new_tuple = tuple(mi_lista)
print(new_tuple)

primer_diccionario = dict()
primer_diccionario['primero'] = 'uno'
print(primer_diccionario)

mi_diccionario = {  'Colores Primarios': ['Rojo','Azul','Amarillo'], 
                    'Colores secundarios': ['Naranja','Violeta','Verde'], 
                    'Clave3': 10,
                    'Clave4': False}

print(mi_diccionario.keys())
print(mi_diccionario.values())
print(mi_diccionario['Colores Primarios'])
