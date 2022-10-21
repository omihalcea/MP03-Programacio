import prova
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
            num1 = input("Disme un número: ")
            num2 = input("Un altre: ")
            mig = int(num1) + int(num2)
            mitjana = mig // 2
            print(mitjana)
            p = True
        elif o == 2:
            pes = int(input("Quant peses? "))
            altura = float(input("Quant medeixes? "))
            estatura = altura ** 2
            imc = pes // estatura
            print("\nEl teu IMC es " + str(imc))
            p = True
        elif o == 3:
            celsius = float(input("Disme la temperatura en ºC: "))
            fahrenheit = (celsius * 1.8) + 32
            print("\nLa temperatura en Farhenheit es " + str(fahrenheit))
            p = True
        elif o == 4:
            hora = int(input("Disme l'hora: "))
            minuts = int(input("Disme els minuts: "))
            h = hora * 60
            totalM = h + minuts
            segons = totalM * 60
            print("\nEls segons son " + str(segons))
            p = True
        else:
            system("clear")
            print("\nHas d'introduir un d'estos 4 numeros")
    except:
        system("clear")
        print("\nHas d'introduir un d'estos 4 numeros")