from random import randint
import os


VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_Squirtle = VIDA_INICIAL_SQUIRTLE

while vida_Squirtle > 0 and vida_pikachu > 0:

    #Turno de Pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Ataca con Bola voltio")
        vida_Squirtle -= 10
    else:
        print("Ataca con Onda trueno")
        vida_Squirtle -= 11

    if vida_Squirtle < 0:
        vida_Squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0


    barra_vida_pika = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
    print("Pikachu:    [{}{}] ({}/{})".format("*" * barra_vida_pika, " " * (10 - barra_vida_pika),
                                              vida_pikachu, VIDA_INICIAL_PIKACHU))

    barra_vida_squirtle = int(vida_Squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:    [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle),
                                               vida_Squirtle, VIDA_INICIAL_SQUIRTLE))

    input("Enter para continuar... \n")
    os.system("clear")

    print("Turno de Squirtle")
    ataque_squirtle = None
    while ataque_squirtle not in ["A","B","P"]:
        ataque_squirtle = input("Que ataque deseas realizar?[P]lacaje, [B]urbuja, Pistola [A]gua : ")
    if ataque_squirtle == "P":
        print("Ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Ataca con Pistola Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Ataca con Burbuja")
        vida_pikachu -= 9

    if vida_Squirtle < 0:
        vida_Squirtle = 0

    if vida_pikachu < 0:
        vida_pikachu = 0

barra_vida_pika = int(vida_pikachu * 10 / VIDA_INICIAL_PIKACHU)
print("Pikachu:    [{}{}] ({}/{})".format("*" * barra_vida_pika, " " * (10 - barra_vida_pika),
                                          vida_pikachu, VIDA_INICIAL_PIKACHU))

barra_vida_squirtle = int(vida_Squirtle * 10 / VIDA_INICIAL_SQUIRTLE)
print("Squirtle:    [{}{}] ({}/{})".format("*" * barra_vida_squirtle, " " * (10 - barra_vida_squirtle),
                                           vida_Squirtle, VIDA_INICIAL_SQUIRTLE))



if vida_pikachu > vida_Squirtle:
    print("Pikachu es el ganador!")
else:
    print("Squirtle es el ganador!")