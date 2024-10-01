n = int(input("Digite o número de termos da sequência de Fibonacci: "))
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(f"A sequência de Fibonacci com {n} termos é: {fibonacci[:n]}")