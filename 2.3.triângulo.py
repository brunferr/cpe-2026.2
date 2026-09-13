import math
def valida_triangulo(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)
def area_heron(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
a=int(input("Digite o primeiro lado do triângulo: "))
b=int(input("Digite o segundo lado do triângulo: "))
c=int(input("Digite o terceiro lado do triângulo: "))
if valida_triangulo(a, b, c):
    area = area_heron(a, b, c)
    print(f"A área do triângulo com lados {a}, {b} e {c} é: {area}")
else:
    print("Os valores fornecidos não formam um triângulo válido.")
