import random
from os import system
import time
nombre = 1
puntuacio1 = int()
puntuacio2 = int()
puntuacio3 = int()
puntuacio4 = int()
puntuacions = [puntuacio1, puntuacio2, puntuacio3, puntuacio4]
jugadors = []
preguntes = [
    ["Qui va ser el primer president d'Estats Units?",[["Abraham Lincon", False], ["George Washinton", True], ["Donald Trump", False]]], 
    ["Quin any va arribar l'home a la lluna?",[["1969", True], ["1970", False], ["1965", False]]], 
    ["En quin any es va disoldre l'unio sovietica?",[["1987", False], ["1991", True], ["1976", False]]],
    ["Quina es la capital de Grecia?",[["Mikonos", False], ["Creta", False], ["Atenes", True]]],
    ["En quins oceans fa contacte Japó?",[["Pacific i Índic", False], ["Atlantic i Nordic", False], ["Pacific", True]]],
    ["Quina d'aquestes tribus no es nativa Americana?",[["Cheroquis", False], ["Nunga", True], ["Apaches", False]]],
    ["Com es diu la linea imaginaria vertical que divideix el planeta per la meitat?",[["El meridia de Greenwitch", True], ["Ecuador", False], ["Tròpic de Càncer", False]]],
    ["Quin dels següents programes no es un SGBD?",[["Microsoft Word", True], ["Oracle", False], ["MySQL", False]]],
    ["Qui va pintar el Guernica?",[["Salvador Dalí", False], ["Jackson Pollock", False], ["Pablo Picasso", True]]],
    ["Tinc una raqueta i un pilota de tenis. Tot junt m'ha costat 1.10€ i se que la raqueta m'ha costat 1€ mes que la pilota. Quan costa la pilota?",[["0.10€", False], ["0.5€", False], ["0.05€", True]]],
    ]

numjugadors = int(input("""\n─────¡¡¡Benvinguts al Trivia Pursuit!!!─────

Este es un joc de preguntes de 2 a 4 jugadors,
el primer que encerte 3 preguntes guanya.

Per a contestar has d'escriure el numero
que hi ha al costat de cada resposta.

Per a continuar heu d'introduir quants jugadors sereu.

Introdueix el numero de jugadors (2-4): """))

los = numjugadors-1
numr = [1, 2, 3]
while numjugadors > 0:
    nomp = input("Introduiu el nom del jugador " + str(nombre) + ": ")
    jugadors.append(nomp)
    nombre += 1
    numjugadors -=1

turno = random.randint(0, los)

while puntuacio1 < 3 and puntuacio2 < 3 and puntuacio3 < 3 and puntuacio4 < 3 and len(preguntes) > 0:
    random.shuffle(preguntes)
    random.shuffle(preguntes[0][1])
    print("\nEs el torn de", str(jugadors[turno]))
    print("\n" + preguntes[0][0] + "\n")
    for i in range(1, 4):
        print("[" + str(i) + "]",preguntes[0][1][i-1][0])  
    res = int(input())
    if preguntes[0][1][res-1][1] == True:
        if len(preguntes) > 0:
            print("\nResposta correcta")
            del preguntes[0]
            if turno+1 == 1:
                puntuacio1 += 1
            elif turno+1 == 2:
                puntuacio2 += 1
            elif turno+1 == 3:
                puntuacio3 += 1
            elif turno+1 == 4:
                puntuacio4 += 1
            input("\nPrem enter per continuar")
            system("clear")
    else:
        if len(preguntes) > 0:
            print("\nRESPOSTA INCORRECTA\n")
            del preguntes[0]
            if turno + 1 > los:
                turno = 0
            else:
                turno += 1
        input("\nPrem enter per continuar")
        system("clear")

if puntuacio1 == 3 or puntuacio2 == 3 or puntuacio3 == 3 or puntuacio4 == 3:
    print("El guanyador es", jugadors[turno] + ", felicitats!!!")
else:
    print("S'han acabat les preguntes i no ha guanyat ningú.")