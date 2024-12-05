a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b**2 - 4 * a * c

if delta > 0:

    raiz1 = (-b + delta**0.5) / (2 * a)
    raiz2 = (-b - delta**0.5) / (2 * a)
    print(f"As raízes são: {raiz1} e {raiz2}")
elif delta == 0:
    raiz = -b / (2 * a)
    print(f"A raiz é: {raiz}")
else:
    print("A equação não possui raízes reais.")
    