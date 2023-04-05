edad = int(input("Cual es su edad: "))
tipo_de_carnet = input("Que carnet tienes(E estudiante/ P pensionista/ F familia/ N nada): ")


if (25 <= edad <= 35 and tipo_de_carnet == "E") or \
        edad <= 10 or\
        (edad >= 65 and tipo_de_carnet == "P") or\
        (tipo_de_carnet == "F"):
    print("Si cumples los requisitos para tener 25% de descuento")

else:
    print("No se te aplica el descuento")