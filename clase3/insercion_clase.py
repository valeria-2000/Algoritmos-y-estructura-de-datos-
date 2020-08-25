def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice
        print(posicion_actual,valor_actual)
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            print (lista[posicion_actual - 1] , valor_actual)
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
        print(lista)
        print('#'*25)
    return lista
lista =[1,7,8,3,2,4,9,23,0]
print(ordenamiento_por_insercion(lista))