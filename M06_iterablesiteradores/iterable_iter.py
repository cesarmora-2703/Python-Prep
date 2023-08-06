lista = [5, 4, 9, 2]
i = 0
while i < len(lista):
    elemento = lista[i]
    print(elemento)
    i += 1
    
lista = ['*', 5, 4, 9, 2, 8, 90]

for elemento in lista:
    print(elemento)
    
cadena = "Henry"
for c in cadena:
    print(c)
    
cadena = "soy Henry"
for c in enumerate(cadena):
    print(c)
    
from collections.abc import Iterable
cadena = "Henry"
numero = 9
dict = {'a':1, 'b':2, 'c':3}
print(isinstance(9, Iterable))
print(isinstance(cadena, Iterable))
print(isinstance(dict, Iterable))

mi_dict = {'a':1, 'b':2, 'c':3}
for i in mi_dict:
    print(i)
    
print(mi_dict.keys())
print(mi_dict.values())

libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)

print(marcapaginas)
for x in marcapaginas:
    print(x)


lista_1 = [1, 2, 3, 4]
lista_2 = ['a', 'b', 'c', 'd']
combinacion = zip(lista_1, lista_2)
print(combinacion)
for c in combinacion:
    print(c)
    
numeros = [1, 2, 3, 4, 5, 6]
pares_por_dos = [x * 2 for x in numeros if x % 2 == 0]
print(pares_por_dos)

frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
print(erres)
print(len(erres))

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

# Classi code
for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list comprenhensions
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# without condition
newlist2 = [x for x in range(10)]
print(newlist2)

# with condition
newlist3 = [x for x in range(10) if x%2==0]
print(newlist3)

# change banana for orange
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# all grapes
newlist = ['grape' for x in fruits]
print(newlist)

libro = ['página1', 'página2', 'página3', 'página4']
marcapaginas = iter(libro)
print(next(marcapaginas))

fibo1 = [0,1]
print(fibo1)

fibo = [ fibo1.append(fibo1[j-1] + fibo1[j-2]) for j in range(2,30)  ]

print(fibo1)

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
cadena1 = list(enumerate(cadena))

n = [print(cadena1.index(c)) for c in cadena1 if 'n' in c]
