import csv
ruta = '/home/ana/Proyectos/archivos/proyecto/'
datos = ruta + 'cust_orders_prods.csv'


def leer(fichero):

    filas = []
    with open(fichero, 'r') as csv_file:
        csvreader = csv.DictReader(csv_file)
        filas = list(csvreader)
    return filas

def vendedores(filas):
    vendedores_cantidad = {}

    for i in filas:
        vendedores_cantidad = i[' quantity']
        print(vendedores_cantidad)


        # if vendedores_cantidad.get(i['customer_name']) != None:
        #     vendedores_cantidad[i['customer_name']] += i[' quantity']
        # else:
        #     vendedores_cantidad[i['customer_name']] = i[' quantity']
    
    print(vendedores_cantidad)

vendedores(leer(datos))





# def vendedores():
#     lista_vendedores = []
#     lista_vendedores_y_cantidad = []
#     total_datos = leer(datos)
#     for i in total_datos:
#         # aquí recorro los datos para rellenar una lista solo con los vendedores que me servirá más adelante.
#         if i[1] not in lista_vendedores:
#             lista_vendedores.append(i[1])
#     for i in total_datos:
#         # con este for quiero llenar la lista lista_vendedores_y_cantidad en la cual aparecera el nombre del vendedor
#         # y todas las ventas que tiene en cada producto
#         if i[1] not in lista_vendedores_y_cantidad:
#         # con este if y este else lo que hago es que meta solo una vez el nombre del vendedor pero si meta en la lista 
#         # todas las cifras de ventas de los vendedores. pq? pq si i[1] q es nombre d cada vendedor no esta en la lista
#         #le digo q meta nombre y cantidad, y si esta en la lista, q meta solo cantidad
#             lista_vendedores_y_cantidad.append(i[1])
#             lista_vendedores_y_cantidad.append(i[3])
#         else:
#             lista_vendedores_y_cantidad.append(i[3])
#     #a continuacion creo tres listas vacias, con bucles for recorro la lista dnd estan los vendedores y las cantidades.
#     # lo q consigo aqui es recorrer esa lista: si encuentro un nombre, lo añado a l_final. si no es un nombre, lo añado a
#     # l_cantidades, la cual es una lista q solo me sirve para ir metiendo las cantidades de cada vendedor. cuando
#     # recorriendo l_vendedores_y_cantidad encuentro otro nombre de vendedor, añado a l_final el sumatorio de todas las cifras
#     # que habia encontrado hasta entonces en l_cantidades y vacio esa lista para volver a empezar a llenarla hasta encontrar otro nombre.
#     l_cantidades = []
#     l_final = []
#     l_total = []
#     for e in lista_vendedores_y_cantidad:
#         if e in lista_vendedores:
#             if sum(l_cantidades) != 0:
#                 l_final.append(sum(l_cantidades))
#                 l_total.append(sum(l_cantidades))
#             l_final.append(e)
#             l_cantidades = []
#         else:
#             l_cantidades.append(int(e))
#     l_final.append(sum(l_cantidades))
#     l_total.append(sum(l_cantidades))
#     l_total = sum(l_total)
#     print(l_total)
#     #en l_total fui añadiendo todos los sumatorios de todas las cantidades de cada vendedor para tener el total de ventas. 
#     # podeis probarlo y os dara la suma correcta igual q si sumais todas las ventas en excel, que son 29420000
#     return l_final

# print(vendedores())