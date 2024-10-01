numero = int(input("Digite um número: "))
divisores = [i for i in range(1, numero + 1) if numero % i == 0]
print(f"Os divisores de {numero} são: {divisores}")