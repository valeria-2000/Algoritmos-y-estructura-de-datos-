import burbuja
import insercion
import time
import mezcla
import random
size_list= int (input("Ingrese tamaño de la lista : "))
lista = [random.randint(1,1000) for i in range(size_list)]

lista_desordenada = lista
lista_desordenada_2 = lista
lista_desordenada_3 = lista
inicio = time.time()
burbuja.ordenamiento_burbuja(lista)
final_burbuja = time.time()-inicio

inicio = time.time()
insercion.ordenamiento_por_insercion(lista_desordenada)
final_insercion = time.time()-inicio


inicio = time.time()
mezcla.ord_por_mezcla(lista_desordenada_2)
final_mezcla = time.time()-inicio

inicio = time.time()
lista_desordenada_3.sort()
final_python = time.time()-inicio

print(f"el tiempo fina de borbuja es {final_burbuja} y el de insercion {final_insercion} el tiempo final de mezcla {final_mezcla} y el final de python es {final_python}")