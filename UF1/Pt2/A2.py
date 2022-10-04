frase = input("Escriu una frase: \n")

split = len(frase.split())

#Compta el numero de caracters
caracters = str(len(frase))

#Compta el numero de paraules
paraules = str(split)

#Transforma les minuscules en majuscules
majuscules = str(frase.upper())

#Transforma les majuscules en minuscules
minuscules = str(frase.lower())

print("""
\nHi han """ + caracters + " caracters en total" + 
"\nHi han " + paraules + " paraules en total" + 
"\nLa frase en majuscules es: " + majuscules + 
"\nLa frase en miuscules es: " + minuscules)

caracter = input("\nDisme un caracter de la frase que has escrit: ")

#Retorna la primer coincidencia basat amb la variable caracter
fcaracter = minuscules.find(caracter) + 1

#Retorna l'última coincidencia basat amb la variable caracter
lcaracter = minuscules.rfind(caracter) + 1

#Retorna el numero de coincidencies basat amb la variable caracter
ncaracters = minuscules.count(caracter)

#Compta totes les vocals de la frase
vocals = minuscules.count("a") + minuscules.count("e") + minuscules.count("i") + minuscules.count("o") + minuscules.count("u")

print("""
\nLa primer posició a la que es troba es: """ + str(fcaracter) + 
"\nL'última posició on s'ha trobat es: " + str(lcaracter) + 
"\nEl número de vegades que s'ha trobat es: " + str(ncaracters) +
"\nEl número de vocals que s'han trobat es: " + str(vocals))