numeros = [int(input("Digite um número: ")) for _ in range(10)]
soma = sum(numeros)
media = soma / len(numeros)
print(f"Soma: {soma}, Média: {media}")