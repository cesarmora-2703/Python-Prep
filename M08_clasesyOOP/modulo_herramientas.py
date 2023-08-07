class Herramientas_lista_mod:

    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros


    def verifica_primo(self):
        for num in self.lista_numeros:
            if(self.__verifica_primo(num)):
                print(f'El elemento {num} es primo.')
            else:
                print(f'El elemento {num} no es primo.')

    def __verifica_primo(self, num):
        if num < 2:
            return False
        for i in range(2,num):
            if num%i == 0:
                return False
        return True

    def valor_modal(self):
        times = 0
        which_one = 0
        checked_items = []
        for item in self.lista_numeros:
            if item in checked_items:
                continue
            timesItem = self.lista_numeros.count(item)
            if timesItem > times:
                times = timesItem
                which_one = item
            checked_items.append(item)
    
        return print(f'El valor modal es {which_one} y se repite {times} veces.')


    def __convert_to_Centigrade(self, valor, entrada):
        '''
        Centigrades to kelvin or Farenheit
        '''
        if entrada == 'K':
            return  valor - 273.15
        elif entrada == 'F':
            return (5*(valor-32))/9 

 
    def __convert_to_Farenheit(self, valor, entrada):
        '''
        Farenheit to kelvin or Centigrades
        '''
        if entrada == 'K':
            return (9/5)*(self.__convert_to_Centigrade(valor, 'K')) + 32
        elif entrada == 'C':
            return (9/5)*valor + 32
        
    def __convert_to_Kelvin(self, valor, entrada):
        '''
        Centigrades to kelvin or Farenheit
        '''
        if entrada == 'F':
            return self.__convert_to_Centigrade(valor, 'F') + 273.15
        elif entrada == 'C':
            return valor + 273.15
        
    
    def conversion_grados(self, origen, destino):
        for temp in self.lista_numeros:
            tempC = self.__conversion_grados(temp, origen, destino)
            print(f'{temp} grados º{origen.upper()} son {tempC} grados º{destino.upper()}')

    def __conversion_grados(self, valor, entrada, salida ):
        '''
        Converts temperature from C, K or F to other scales
        '''
        entrada = entrada.upper()
        salida = salida.upper()
        
        if entrada == 'C':
            if salida == 'F':
                return self.__convert_to_Farenheit(valor, entrada)
            elif salida == 'K':
                return self.__convert_to_Kelvin(valor, entrada)
            elif salida == 'C':
                return valor

        if entrada == 'F':
            if salida == 'C':
                return self.__convert_to_Centigrade(valor, entrada)
            elif salida == 'K':
                return self.__convert_to_Kelvin(valor, entrada)
            elif salida == 'F':
                return valor

        if entrada == 'K':
            if salida == 'C':
                return self.__convert_to_Centigrade(valor, entrada)
            elif salida == 'F':
                return self.__convert_to_Farenheit(valor, entrada)
            elif salida == 'K':
                return  valor


    def factorial(self):
        for num in self.lista_numeros:
            print(f'El factorial de {num} es {self.__factorial(num)}')

    def __factorial(self, number):
        '''
        Calcula el factorial de un numero entero positivo
        '''
        if type(number) != int:
            return 'El numero debe ser un entero'
        if number < 0:
            return 'El mumero debe ser un entero positivo'
        if number >1:
            number = number * self.__factorial(number - 1)
        
        return number
    
    if __name__ == '__main__':
        pass