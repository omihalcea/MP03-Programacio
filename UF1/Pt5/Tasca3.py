import random
numero1 = random.randint(1, 6)
numero2 = random.randint(1, 6)
p = False
puto = False
while p == False:
    p1 = input("\nEscriu 'tirar' per a tindre el numero del jugador 1: ")

    if p1 == "tirar":
        print("El teu número es: " + str(numero1))
        while puto == False: 
            p2 = input("\nEscriu 'tirar' per a tindre el numero del jugador 2: ")
            if p2 == "tirar":
                puto = True
                print("El teu número es: " + str(numero2))
                print("\nEl número del jugador 1 es: " + str(numero1) + "\nI el número del jugador 2 es: " + str(numero2))

                if numero1 > numero2:
                    print("\nGuanya el jugador 1")

                elif numero1 < numero2:
                    print("\nGuanya el jugador 2")

                elif numero1 == numero2:
                    print("\nHa sigut un empat")
                p = True
            else:
                print("\nEl jugador 2 no ha escrit 'tirar'")

    else: 
        print("\nEl jugador 1 no ha escrit 'tirar'")