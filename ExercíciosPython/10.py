numeros = []
for _ in range(10):
    numeros.append(int(input("Digite um número: ")))

soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)

print(f"Soma: {soma}, Maior: {maior}, Menor: {menor}")