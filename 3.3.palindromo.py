texto = input("Digite um texto: ")

texto_limpo = texto.replace(" ", "").lower()

if texto_limpo == texto_limpo[::-1]:
    print(f'"{texto}" é um palíndromo!')
else:
    print(f'"{texto}" não é um palíndromo.')