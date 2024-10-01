def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    for a, b in zip(lista1, lista2):
        lista_intercalada.append(a)
        lista_intercalada.append(b)
    return lista_intercalada

lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
resultado = intercalar_listas(lista1, lista2)
print("Lista intercalada:", resultado)