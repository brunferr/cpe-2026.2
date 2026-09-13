import math

a = float(input("Digite o lado a: "))
b = float(input("Digite o lado b: "))
c = float(input("Digite o lado c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    s = (a + b + c) / 2  
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Triângulo válido! Área = {area:.2f}")
else:
    print("Os lados informados não formam um triângulo válido.")