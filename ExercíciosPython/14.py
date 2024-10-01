def maior_menor(lista):
    return max(lista), min(lista)

lista = [int(input("Digite um número: ")) for _ in range(5)]
maior, menor = maior_menor(lista)
print(f"Maior: {maior}, Menor: {menor}")