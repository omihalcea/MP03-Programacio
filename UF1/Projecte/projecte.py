import random
nombre = 1
t1 = random.randint(1, 2)
t2 = int()
np = 3
rang = 2
puntuacio1 = int()
puntuacio2 = int()
puntuacio3 = int()
puntuacio4 = int()
jugadors = []
preguntes = [
    ["Quants anys tinc? \n[1] 1 \n[2] 2 \n[3] 3", 2], 
    ["T'agrada el Pene? \n[1] SI \n[2] Potser \n[3] No estic del tot segur", 3], 
    ["Ets menor \n[1] SI \n[2] NO" "\n[3] NO SE", 2]
    ]

numjugadors = int(input("""\n─────¡¡¡Benvinguts al Trivia Pursuit!!!─────

Este es un joc de preguntes per a 2 jugadors,
el primer que encerte 3 preguntes guanya.

Per a contestar has d'escriure el numero
qu hi ha al costat de cada resposta.

Per a continuar heu d'introduir els vostres noms

Introdueix el numero de jugadors (2-4): """))

los = numjugadors

while numjugadors > 0:
    nomp = input("Introduiu el nom del jugador " + str(nombre) + ": ")
    jugadors.append(nomp)
    nombre += 1
    numjugadors -=1

while puntuacio1 < 3 and puntuacio2 < 3 and puntuacio3 < 3 and puntuacio4 < 3 and len(preguntes) != 0:
    turno = random.randint(0, los-1)
    print("\nEs el torn de", str(jugadors[turno]))
    while np > 0:
        random.shuffle(preguntes)
        print("\n" + preguntes[0][0] + "\n")
        res = int(input())
        rang -= 1
        if res == preguntes[0][1]:
            print("\nResposta correcta")
            del preguntes[0]
            if turno == 1:
                puntuacio1 += 1
            elif turno == 2:
                puntuacio2 += 1
            elif turno == 3:
                puntuacio3 += 1
            elif turno == 4:
                puntuacio4 += 1
        else:
            print("\nRESPOSTA INCORRECTA\n")
            del preguntes[0]
            turno += 1
            if turno + 1 > los:
                turno = 0
            print("\nEs el torn de", str(jugadors[turno]))
        np -= 1