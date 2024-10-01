numero = int(input("Digite um número menor que 100: "))
if 0 <= numero < 100:
    soma = sum(int(digito) for digito in str(numero))
    print(f"A soma dos dígitos de {numero} é: {soma}")
else:
    print("Número inválido! Deve ser menor que 100.")