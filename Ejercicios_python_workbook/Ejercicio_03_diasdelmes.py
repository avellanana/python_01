def mes_nombre(mes):
    
    meses30 = ["abril","junio","septiembre","noviembre",]
    meses31 = ["enero","marzo","mayo","julio","agosto","octubre","diciembre"]

    for i in meses30:
        if i == mes:
            salida = print("El mes tiene 30 días")
    
    for i in meses31:
        if i == mes:
            salida = print("El mes tiene 31 días")
    
    if mes == "febrero":
        salida = print("El mes tiene 28 o 29 días")

    return salida
 
mes_nombre("diciembre")


