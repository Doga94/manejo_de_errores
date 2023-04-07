def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError('Error: No se puede dividir por cero!')
    else:
        return a / b
    
dividir(5, 0)