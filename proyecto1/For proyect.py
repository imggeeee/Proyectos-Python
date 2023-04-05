espacios = 0
puntos = 0
comas = 0

texto_de_usuario = input("Escribe algo pibi: ")
for letra in texto_de_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ",":
        comas += 1
    elif letra == ".":
        puntos += 1

print("Hay {} espacios, {} comas y {} puntos".format(espacios, comas, puntos))