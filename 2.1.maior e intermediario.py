a=int(input("Digite o primeiro numero: "))
b=int(input("Digite o segundo numero: "))
c=int(input("Digite o terceiro numero: "))
if a>b and a>c and b>c:
    print(f"O maior numero e: {a} e o intermediario e: {b}")
elif a>b and a>c and c>b:
    print(f"O maior numero e: {a} e o intermediario e: {c}")
elif b>a and b>c and a>c:
    print(f"O maior numero e: {b} e o intermediario e: {a}")    
elif b>a and b>c and c>a:
    print(f"O maior numero e: {b} e o intermediario e: {c}")
elif c>a and c>b and a>b:
    print(f"O maior numero e: {c} e o intermediario e: {a}")
elif c>a and c>b and b>a:
    print(f"O maior numero e: {c} e o intermediario e: {b}")