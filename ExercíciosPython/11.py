string = input("Digite uma string: ")
if string == string[::-1]:
    print(f"{string} é um palíndromo.")
else:
    print(f"{string} não é um palíndromo.")