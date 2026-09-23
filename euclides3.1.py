def mdc(a, b):
    ciclos = 0
    while b != 0:
        a, b = b, a % b
        ciclos += 1
    return a, ciclos

resultado1, ciclos1 = mdc(76, 34)
print(f"mdc(76, 34) = {resultado1}, com {ciclos1} ciclos")

resultado2, ciclos2 = mdc(224, 7)
print(f"mdc(224, 7) = {resultado2}, com {ciclos2} ciclos")