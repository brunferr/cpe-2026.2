n=int(input("Digite um número: "))
if n<0:
    print("Numero invalido ")
else:
    fatorial=1
    i=1
    while i<=n:
        fatorial=fatorial*i
        i=i+1
    print(f"O fatorial de {n} é {fatorial}")