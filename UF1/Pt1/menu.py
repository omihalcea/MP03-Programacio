from Mitjana import *
from IMC import *
from Hora import *
from Temperatura import *
from os import system
p = False

while p == False:
    try:
        o = int(input("""
Que vols fer?

[1] Calcular mitjana
[2] Calcular IMC
[3] Conversor de temperatura
[4] Convertir la hora a segons

"""))
        if o == 1:
            mitjana()
            p = True
        elif o == 2:
            imc()
            p = True
        elif o == 3:
            temperatura()
            p = True
        elif o == 4:
            hora()
            p = True
        else:
            system("clear")
            print("\nHas d'introduir un d'estos 4 numeros")
    except:
        system("clear")
        print("\nHas d'introduir un d'estos 4 numeros")