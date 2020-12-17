import math


def area(radio): 
    #Refactorizado
    
    if not type(radio) in [int, float] :
        raise TypeError('El radio debe ser un número entero o decimal mayor que cero')

    if  radio <0:
        raise ValueError('El radio no puede ser negativo')
    
    return math.pi * radio * radio

