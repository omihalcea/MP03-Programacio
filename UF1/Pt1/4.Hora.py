hora = int(input("Disme l'hora: "))
minuts = int(input("Disme els minuts: "))

h = hora * 60
totalM = h + minuts
segons = totalM * 60

print("\nEls segons son " + str(segons))