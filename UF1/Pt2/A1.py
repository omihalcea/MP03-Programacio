cadena = input("Disme 4 numeros: ")

print("Els caracters son tots numeros? " + str(cadena.isnumeric()) + "\n")

resultat = int(cadena[0]) + int(cadena[1]) + int(cadena[2]) + int(cadena[3])
print("La suma dels caracters es " + str(resultat))