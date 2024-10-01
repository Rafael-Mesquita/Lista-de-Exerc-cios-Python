def ultimo_elemento(lista):
    if lista:
        return lista[-1]
    return None

lista = [1, 2, 3, 4, 5]
print("Último elemento:", ultimo_elemento(lista))