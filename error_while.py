#Con While
c=0
suma=0

while c < 3:
    try:
        n = int(input(f'Ingese un numero entero {c+1}: '))
        suma += n
        c += 1
    except:
        print("Error: Ingrese solo números enteros")
    else:
        print("Todo funciono")

print('La sumetotal es: ', suma)
