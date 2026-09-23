a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

valor_mdc, _ = mdc (a, b)

if valor_mdc == 1:
    print(f"{a} e {b} são primos entre si")
else:
    print(f"{a} e {b} não são primos entre si (mdc = {valor_mdc})")