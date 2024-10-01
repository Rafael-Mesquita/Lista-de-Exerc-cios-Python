string = input("Digite uma string: ")
vogais = "aeiouAEIOU"
contagem_vogais = sum(1 for char in string if char in vogais)
contagem_espacos = string.count(' ')
print(f"Número de vogais: {contagem_vogais}, Número de espaços: {contagem_espacos}")