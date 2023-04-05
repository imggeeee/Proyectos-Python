a = []
input_de_usuario = None

print("Programa de Lista de compras")

while True:
    input_de_usuario = input("Que deseas comprar? ([Q] para salir): ")
    if input_de_usuario == "Q":
        break
    elif input_de_usuario in a:
        print("{} ya esta en la lista".format(input_de_usuario))
    else:
        if input("¿Seguro que quieres añadir {} a la lista de la compra? [S/N]: ".format(input_de_usuario)) == "S":
            a.append(input_de_usuario)

print("La lista de la compra es: {}".format(a))