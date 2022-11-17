import random
import platform
from os import system
import socket
import time

#Puntucions
puntuacio1 = int()
puntuacio2 = int()
puntuacio3 = int()
puntuacio4 = int()
equip = socket.gethostname()
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

#Un petita funcion per a netejar pantalla. No t'enfades 
def clear():
    sistema = platform.system()
    if sistema == "Linux":
        system("clear")
    elif sistema == "Windows":
        system("cls")

clear()
pb = False

print("""           
                   ¡¡¡AVÍS!!!!

          PER A UNA MILLOR EXPERIENCIA
        HAS DE JUGAR EN PANTALLA COMPLETA
""")
time.speep(3)
print("""            
            Prem ENTER per a continuar
""")
input()

clear()

while pb == False:
    try:
        numjugadors = int(input("""\n─────¡¡¡Benvinguts al Trivia Pursuit!!!─────

Este es un joc de preguntes de 2 a 4 jugadors,
el primer que encerte 3 preguntes guanya.

Per a contestar has d'escriure el numero
que hi ha al costat de cada resposta.

Per a continuar heu d'introduir quants jugadors sereu.

Introdueix el numero de jugadors (2-4): """))
        pb = True
    except:
            print("\nHAS D'INTRODUIR UN VALOR VÀLID")
            input()
            clear()

los = numjugadors-1
nombre = 1
numr = [1, 2, 3]

while numjugadors > 0:
    nomp = input("Introduiu el nom del jugador " + str(nombre) + ": ")
    jugadors.append(nomp)
    nombre += 1
    numjugadors -=1
    pb = True

turno = random.randint(0, los)

while puntuacio1 < 3 and puntuacio2 < 3 and puntuacio3 < 3 and puntuacio4 < 3 and len(preguntes) > 0:
    try:
        clear()
        random.shuffle(preguntes)
        random.shuffle(preguntes[0][1])
        print("\nEs el torn de", str(jugadors[turno]))
        print("\n" + preguntes[0][0] + "\n")
        for i in range(1, 4):
            print("[" + str(i) + "]",preguntes[0][1][i-1][0])  
        res = int(input())
        if preguntes[0][1][res-1][1] == True:
            if len(preguntes) > 0:
                print("\nRESPOSTA CORRECTA")
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
        else:
            if len(preguntes) > 0:
                print("\nRESPOSTA INCORRECTA\n")
                del preguntes[0]
                if turno + 1 > los:
                    turno = 0
                else:
                    turno += 1
            input("\nPrem enter per continuar")
    except:
        if len(preguntes) > 0:
            print("HAS D'INTRODUIR UNA RESPOSTA VÀLIDA")
            del preguntes[0]
            if turno + 1 > los:
                turno = 0
            else:
                turno += 1
        input("\nPrem enter per continuar")
        clear()

if puntuacio1 == 3 or puntuacio2 == 3 or puntuacio3 == 3 or puntuacio4 == 3:
    clear()
    print("El guanyador es", jugadors[turno] + ", felicitats!!!")
    print("""
_______oBBBBB8o      oBBBBBBB
_____o8BBBBBBBBBBB  BBBBBBBBB8       o88o,
___o8BBBBBB**8BBBB  BBBBBBBBBB     oBBBBBBBo,
__oBBBBBBB*   ***   BBBBBBBBBB     BBBBBBBBBBo,
_8BBBBBBBBBBooooo   *BBBBBBB8      *BB* 8BBBBBBo,
_8BBBBBBBBBBBBBBBB8ooBBBBBBB8           8BBBBBBB8,
__*BBBBBBBBBBBBBBBBBBBBBBBBBB8 o88BB88BBBBBBBBBBBB,
____*BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB8,
______**8BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB*,
___________*BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB8*,
____________*BBBBBBBBBBBBBBBBBBBBBBBB8888**,
_____________BBBBBBBBBBBBBBBBBBBBBBB*,
_____________*BBBBBBBBBBBBBBBBBBBBB*,
______________*BBBBBBBBBBBBBBBBBB8,
_______________*BBBBBBBBBBBBBBBB*,
________________8BBBBBBBBBBBBBBB8,
_________________8BBBBBBBBBBBBBBBo,
__________________BBBBBBBBBBBBBBB8,
__________________BBBBBBBBBBBBBBBB,
__________________8BBBBBBBBBBBBBBB8,
__________________*BBBBBBBBBBBBBBBB,
__________________8BBBBBBBBBBBBBBBB8,
_________________oBBBBBBBBBBBBBBBBBB,
________________oBBBBBBBBBBBBBBBBBBB,
________________BBBBBBBBBBBBBBBBBBBB,
_______________8BBBBBBBBBBBBBBBBBBB8,
______________oBBBBBBBBB88BBBBBBBBB8,
______________8BBBBBBBBB*8BBBBBBBBB*,
______________BBBBBBBBB* BBBBBBBBB8,
______________BBBBBBBB8 oBBBBBBBBB*,
______________8BBBBBBB  oBBBBBBBB*,
______________BBBBBBB*  8BBBBBBB*,
_____________8BBBBBB*   BBBBBBB*,
____________8BBBBBB8   oBBBBBB8,
___________8BBBBBB8    8BBBBBB*,
__________oBBBBBB8    BBBBBBB8,
__________BBBBBBB8   BBBBBBBB*,
_________oBBBBBBB8   BBBBBBBB,
_________8BBBBBB8    BBBBBBB*,
_________BBBBBB*     8BBBBB*,
________oBBBB8       BBBBB*,
________oBBB8        BBBB*,
______8BBBB*         *BBBBBBBB8o,
______BBBBB*            *88BBBo

    """)
else:
    clear()
    print("""                               S'HAN ACABAT LES PREGUNTES""")
    time.sleep(1.2)
    print("""                               NO HA GUANYAT NINGÚ""")
    time.sleep(1.2)
    print("""                               EL JOC S'HA ACABAT""")
    time.sleep(1.2)
    print("""                               FINS LA PRÒXIMA,""", equip.upper())
    time.sleep(1.2)
    print("""
                  ██████████                                    ██████████              
                ██████████    ░░                                  ██████████            
░░              ██████████  ████████                    ████████  ██████████            
░░              ████████  ██        ████            ████        ▓▓  ████████          ░░
              ██████████░░▒▒            ████    ████            ▒▒░░██████████          
              ██████████    ██████████      ████      ██████████    ██████████          
              ██████████  ██████▒▒▒▒████            ████▒▒▒▒██████  ██████████          
            ████████████  ████▒▒████▒▒██            ██▒▒████▒▒████  ████████████        
            ██████████▒▒▒▒  ████▒▒▒▒████  ██    ██  ████▒▒▒▒████  ▒▒▒▒██████████        
            ██████████    ▒▒  ████████    ██    ██    ████████  ▒▒    ██████████        
            ████████▒▒▒▒    ▒▒            ██    ██            ▒▒    ▒▒▒▒████████        
            ████████    ▒▒  ▒▒            ██    ██            ▒▒  ▒▒    ████████        
              ██████▒▒▒▒  ▒▒  ▒▒          ██    ██          ▒▒  ▒▒  ▒▒▒▒████████        
            ████████▒▒▒▒  ▒▒  ▒▒          ██    ██          ▒▒  ▒▒  ▒▒▒▒████████        
              ████████  ▒▒    ▒▒        ██        ██        ▒▒    ▒▒  ████████          
              ████████████  ▒▒          ██        ██          ▒▒  ████████████          
              ██████████████    ▒▒▒▒  ██            ██  ▒▒▒▒    ██████████████          
              ██████████████      ▒▒▒▒▒▒████████████▒▒▒▒▒▒      ██████████████          
                ██████████████      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒      ██████████████            
                ██████████████      ██                ██      ██████████████            
                  ██  ████  ██      ██                ██      ██  ████  ██              
                              ██    ██                ██    ██                          
░░    ░░░░        ░░  ░░░░░░  ██    ██                ██    ██  ░░  ░░        ░░  ░░░░░░
                            ░░  ██  ██                ██  ██                            
                                  ████                ████                              
                                      ██            ██                                  
                                        ████████████                                    
                                                                                        
    """)
