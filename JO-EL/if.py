num = 36
p = False
while p == False:
    try:
        candidat = int(input("Intodueix un numero entre 0 i 100: "))
        if candidat > 100 or candidat < 0:
            print("Has de ficar un numero dins del rang")
        elif candidat > num:
            print("T'has passat")
        elif candidat < num:
            print("T'has quedat curt")
        else:
            print("L'has encertat")
            p = True
    except:
        print("Has d'escriure un numero")