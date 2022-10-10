p1 = int(input())
p2 = int(input())

if p1 == 1 and p2 == 3 or p1 == 2 and p2 == 1 or p1 == 3 and p2 == 2:
    print("Jugador1")
elif p2 == 1 and p1 == 3 or p2 == 2 and p1 == 1 or p2 == 3 and p1 == 2:
    print("Jugador2")
elif p1 == p2:
    print("EMPAT")
elif p1 != 1:
    print("ERROR")