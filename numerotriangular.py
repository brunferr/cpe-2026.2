n=int(input("Digite um numero: "))
soma=0
k=0
while soma<n:
    k=k+1
    soma=soma+k
if soma==n:
    print(f"{n} é um número triangular")
else:
    print(f"{n} não é um número triangular")