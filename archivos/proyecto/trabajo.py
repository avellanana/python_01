import csv

rutabase = (r'C:\Users\Ana\Documents\FP\Programacion\Proyectoequipo')
datos = rutabase + '\cust_orders_prods.csv'

def leer(datos):

    filas = []
    with open(datos, 'r') as csv_file:
        csvreader = csv.reader(csv_file)
        for f in csvreader:
            filas.append(f)
    return filas

print(leer(datos))

# def leerdicc(datos):

#     with open(datos,'r') as csv_file:
#         csvreader = csv.DictReader(csv_file)
#         for fila in csvreader:
#             print(dict(fila))

# leerdicc(datos)

# def productos(datos):

#     lista_general = []
#     with open(datos,'r') as csv_file:
#         csvreader = csv.reader(csv_file)
#         for f in csvreader:
#             for j in f:
#                 lista_general.append(j)
#     print(lista_general)
        
#     listavendedores = lista_general[6::6]
#     listaclientes = lista_general[7::6]
#     listafechas = lista_general[8::6]
#     listacantidades = lista_general[9::6]
#     listaprecios = lista_general[10::6]
#     listaproductos = lista_general[11::6]

#     productos_dif = list(set(listaproductos))
#     print(productos_dif)

# productos(datos)

# def suma_productos(productos):
#     filas = []
#     with open(datos, 'r') as csv_file:
#         csvreader = csv.reader(csv_file)
#         for f in csvreader:
#             filas.append(f)
    
#     for i in productos:
#         if i == filas[i[0]]:
#             print(filas)

# suma_productos(productos(datos))


# def vendedor():
#     lista = leer(datos)
#     dicc = {}
#     for i in lista:
#         dicc[i[1]] = 'hola'
            
#     print(dicc)



    

# print(vendedor())
