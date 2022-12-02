numeros= input("Inserte 5 numeros separados por comas")

def suma_numeros():
    suma = 0
    lista_numeros = numeros.split(',')
    for i in range(len(lista_numeros)):
        lista_numeros[i] = int(lista_numeros[i])
        suma += lista_numeros[i]
    return suma

print(f'Los numeros a sumar son: {numeros} y el resultado es:', suma_numeros())

