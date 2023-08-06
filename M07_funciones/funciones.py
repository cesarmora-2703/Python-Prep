class CasaBarrio:
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