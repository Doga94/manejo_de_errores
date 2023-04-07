#Ejemplo general

while True:
    try:
        numerador = float(input("Ingrese el numerador: "))
        denominador = float(input("Ingrese el denominador: "))
        resultado = numerador / denominador
        print("El resultado es:", resultado)
    except ZeroDivisionError:
        print("El denominador no puede ser cero.")
    except ValueError:
        print("Ingrese solo numeros")
    else:
        print("Toda OK")
        break