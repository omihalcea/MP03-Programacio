dni = input("Disme el teu DNI: ")
numero = int(dni[:8])
lletra = dni[8:]
lletres = str("TRWAGMYFPDXBNJZSQVHLCKE")
residu = numero % 23
lletraT = lletres[residu]
print(str(lletraT) == str(lletra))