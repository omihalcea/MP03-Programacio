import random
t1 = random.randint(1, 2)
t2 = int()
np = 3
rang = 2
puntuacio1 = int()
puntuacio2 = int()
preguntes = [["Quants anys tinc? \n[1] 1 \n[2] 2 \n[3] 3", 2], 
            ["T'agrada el Pene? \n[1] SI \n[2] Potser \n[3] No estic del tot segur", 3], 
            ["Ets menor \n[1] SI \n[2] NO", 2]]

nomp1 = input("""\n─────¡¡¡Benvinguts al Trivi Pursuit!!!─────

Este es un joc de preguntes per a 2 jugadors,
el primer que encerte 3 preguntes guanya.

Per a contestar has d'escriure el numero
qu hi ha al costat de cada resposta.

Per a continuar heu d'introduir els vostres noms

Nom del jugador 1: """)
nomp2 = input("Ara introduiu el nom del segon jugador: ")

if t1 == 1:
    print("\nComença el jugador 1")
    t2 = 2
else:
    print("\nComença el jugador 2")
    t2 = 1

while puntuacio1 < 3 or puntuacio2 < 3:
    while np > 0:
        pregunta = random.randint(0, rang)
        print("\n" + preguntes[pregunta][0] + "\n")
        res = int(input())
        preguntes.pop(pregunta)
        rang -= 1
        if t1 == 1 and res == preguntes[pregunta][1]:
            print("\nResposta correcta")
            puntuacio1 += 1

        elif t2 == 1 and res == preguntes[pregunta][1]:
            print("\nResposta correcta")
            puntuacio2 += 2

        elif t1 == 1 and res != preguntes[pregunta][1]:
            print("\nResposta incorrecta")
            t1 = 2
            t2 = 1
            
        elif t2 == 1 and res != preguntes[pregunta][1]:
            print("\nResposta incorrecta")
            t1 = 1
            t2 = 2
        np -= 1