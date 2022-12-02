def promedio():

    lista_valores = []

    while True:
        valores = int(input("Ingrese un valor: "))
        if valores == 0:
            break
        lista_valores.append(valores)
    
    resultado = sum(lista_valores)/len(lista_valores)
    print(resultado)
    
    return resultado


promedio()


