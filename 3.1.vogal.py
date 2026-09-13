palavra=input("Digite uma palavra de 5 caracteres: ")
vogais_achadas=[]
for letra in palavra:
    if letra.lower() in "aeiou":
        vogais_achadas.append(letra)
print(f"Quantidade de vogais: {len(vogais_achadas)}")
print(f"Vogais encontradas: {vogais_achadas}")        
    