import csv

rutabase = ('/home/ana/Proyectos/archivos/proyecto/')
datos = rutabase + '/cust_orders_prods.csv'

def leer(datos):

    with open(datos, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        for fila in csvreader:
            print(dict(fila))

leer(datos)

# def lista(datos):
#     lista_general = []
#     with open(datos, 'r') as csv_file:
#         csvreader = csv.reader(csv_file)
#         for f in csvreader:
#             for j in f:
#                 lista_general.append(j)

#     listavendedores = lista_general[6::6]
#     listaclientes = lista_general[7::6]
#     listafechas = lista_general[8::6]
#     listacantidades = lista_general[9::6]
#     listaprecios = lista_general[10::6]
#     listaproductos = lista_general[11::6]

#     productos_dif = list(set(listaproductos))
#     print(productos_dif)

# print(leer(datos))