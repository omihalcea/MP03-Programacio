p = False

while p == False:
    try:
        nota = float(input("Introdueix la teva nota: "))
        if 0 <= nota <= 10:
            if nota >= 9:
                print("Excel·lent")
                p = True
            elif nota >= 8:
                print("Notable")
                p = True
            elif nota >= 7:
                print("Bé")
                p = True
            elif nota >= 5:
                print("Suficient")
                p = True
            else:
                print("Insuficient")
                p = True
        else:
            print("\nHas d'introduir un numero dins del rang")

    except:
        print("\nHas de ficar un numero")