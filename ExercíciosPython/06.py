import cmath

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

raiz1 = (-b + cmath.sqrt(delta)) / (2*a)
raiz2 = (-b - cmath.sqrt(delta)) / (2*a)

print(f"As raízes da equação são: {raiz1} e {raiz2}")