a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

valor_mdc, _ = mdc(a, b)
mmc = abs(a * b) // valor_mdc

print(f"mdc({a}, {b}) = {valor_mdc}")
print(f"mmc({a}, {b}) = {mmc}")