""" class CasaBarrio:
    def __init__(self, numero_casa, fachada):
        self.numero_casa = numero_casa
        self.fachada = fachada

    def imprimirCasa(self):
        return print(f'La casa {self.numero_casa} es de {self.fachada}')
    
    def imprimirCasa2(self):
        return 'La casa ' + str(self.numero_casa) + ' es de ' + self.fachada
    
casa1 = CasaBarrio(2130, 'dos pisos ladrillo a la vista,')
casa2 = CasaBarrio(2587, 'un piso fachada de yeso ')

casa1.imprimirCasa()
casa2.imprimirCasa()

print(casa1.imprimirCasa2())

def factorial (number):
    '''
    Calcula el factorial de un numero entero positivo
    '''
    if number >1 :
        number = number * factorial(number -1)
    return number

print(factorial(5))
help(factorial)
 """

x1 = [10, 20, 30]
def funcion(entrada):
    entrada.append(40)

x = x1.copy()
funcion(x)
print(x1)
print(x)


def funcion(entrada):
    entrada = 0
    print(id(entrada))
x = 1
print(id(x))
funcion(x)


def funcion(entrada):
    entrada.append(40)
    print(id(entrada))
x = [10, 20, 30]
print(id(x))
funcion(x)

lambda_producto = lambda x, y: x * y
print(lambda_producto(3, 4))