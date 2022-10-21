p = False

while p == False:
    try:
        anyP = int(input("Dis-me el any actual: "))
        anyD = int(input("Dis-me un altre any: "))

        if anyD == anyP:
            print("\nSon el mateix any, imbecil")
        elif anyD > anyP:
            print("\nLa diferencia entre els anys es " + str((anyD - anyP)))
            p = True
        elif anyD < anyP:
            print("\nLa diferencia entre els anys es " + str((anyP - anyD)))
            p = True
    except:
        print("\nHas d'introduir un número\n")