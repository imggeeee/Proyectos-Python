
opcion = input("¿Que marca prefieres?\n"
               "A - Ios\n"
               "B - Android\n")
if opcion == "A":
    dinero_ios = input("¿Tienes dinero?[S/N]")
    if dinero_ios == "S":
        print("Comprate el Iphone Ultra Pro Max")
    else:
        print("Comprate un iphone de segunda mano")
if opcion == "B":
    dineor_android = input("¿Tienes dinero?[S/N]")
    if dineor_android == "S":
        camara = input("¿Te importa la camara del celular?[S/N]")
        if camara == "S":
            print("Comprate el Google Pixel Supercamara")
        else:
            print("Comprate un Android calidad-precio")
    else:
        print("Comprate un android chino $100")
else:
    print("Las opciones son A y/o B")