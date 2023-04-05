import random

print("Escapando de la prisión espacial\n"
      "--------------------------------\n"
      "\n"
      "Tú y tu compañero de celda acaban de escapar de la prision espacial, logrando evadir el primer punto de control\n"
      "lamentablemente se encuentran al primer guardia que captura a tu amigo, ahora deberas tomar una serie de \n"
      "decisiones para no acabar como el, ya que tu lograste pasar desapersibido.\n"
      "Es tu oportunidad de escapar, ¿por donde te diriges?.\n"
      "A la izquierda tienes una puerta entreabierta, a la derecha una escotilla en el piso.")

opcion= input("[OPCION (A) - puerta enrteabierta] o [OPCION (B) - escotilla en el suelo]: ")



if opcion == "A":
      print("Entras a la puerta entreabierta y otro guardia te descubre, ¿que haces?")
      opcion= input("[OPCION (A) - Te haces el dormido o OPCION (B) intentas correr a la siguiente puerta ]")

      if opcion == "A":
            print("El guardia te atrapa con facilidad y te vuelven a encerrar\n GAME OVER")
            exit()
      elif opcion == "B":
            print("logras encontrar la salida descuidada y con una nave de emergencia con destino a la tierra.\n"
                  "Cres que estas a salvo pero notas una bomba en la parte trasera del vehiculo, ¿ganaste?\n"
                  "vuelve a intentar con otras opciones para comprobarlo")
            exit()


if opcion == "B":
    print( "Al pasar por esa escotilla te encuentras con una rata gigante que te regala un baston, a cambio de una cuenta,\n "
                   "¿lo aceptas?")
opcion = input("[OPCION (A) si - OPCION (B) no]: ")
baston_en_inventario = False
numero_random_rata = random.randint(1, 100)
if opcion == "A":
    print("Realiza la siguiente multiplicacion\n"
    "cuanto es 13 * {})".format(numero_random_rata))
    opcion = int(input("¿cual es el resultado?"))
    if opcion == 13* numero_random_rata:
        print("La rata te ha comido, no le gusta le gente más lista que ella")
        exit()

    else:
        print("Felicidades, la rata te hace entrega del baston legendario y puedes avanzar a la siguiente puerta")
        baston_en_inventario = True
if opcion == "B":
    print("no aceptas el baston y misteriosamente la rata te deja seguir tu camino")

print("al llegar a la nueva puerta suenan las alarmas y hay una ranura por donde entra el baston")


opcion = input("[OPCION (A) - tengo el baston] o [OPCION (B) no tome el baston]")

if opcion == "A":
    print("Puedes pasar por la puerta, a la sala de controles y puedes volver a casa\n"
          "has ganado")
if opcion == "B":
    print("No tienes el baston en tu inventarion, no puedes pasar\n GAME OVER")
    exit()