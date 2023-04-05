
titulo = "Bienvenido al test sobre Messi"

print("\n" + titulo + "\n" + "-" * len(titulo) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Cuantos años tiene Messi?\n"
                "A - 35 años\n"
                "B - 34 años\n"
                "C - 38 años\n")

if opcion == "A":
    puntuacion += 10

elif opcion == "B":
    puntuacion += 5

elif opcion == "C":
    puntuacion += 0
else:
    print("Las opciones son A,B y C")
    exit()

opcion = input("Pregunta 2: ¿Cuantos hijos tiene Messi?\n"
                "A - 3 hijos\n"
                "B - 2 hijos\n"
                "C - No tiene hijos\n")
if opcion == "A":
    puntuacion += 10

elif opcion == "B":
    puntuacion += 5

elif opcion == "C":
    puntuacion += 0
else:
    print("Las opciones son A,B y C")
    exit()

opcion = input("Pregunta 3: ¿Como se llama la Esposa de Messi?\n"
                "A - Antonella Rocuzo\n"
                "B - Antonela Rocuszo\n"
                "C - Antonela Roccuzzo\n")
if opcion == "A":
    puntuacion += 0

elif opcion == "B":
    puntuacion += 5

elif opcion == "C":
    puntuacion += 10
else:
    print("Las opciones son A,B y C")
    exit()

if puntuacion >= 25:
    print("Resultado: Felicidades, eres fan de Messi")
elif puntuacion >= 15:
    print("Resultado: Te falta conocer a Messi")
else:
    print("Resultado: Felicidades, no eres fan de Messi")
    
