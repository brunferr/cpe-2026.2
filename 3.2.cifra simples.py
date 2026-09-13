palavra=input("Digite uma palavra: ")
substituicao={
    'a':'i','A':'I',
    'e':'o','E':'O',
    'i':'u','I':'U',
}
resultado=""
for letra in palavra:
    resultado+=substituicao.get(letra,letra)
print(f"Palavra original: {palavra}")
print(f"Palavra cifrada: {resultado}")    