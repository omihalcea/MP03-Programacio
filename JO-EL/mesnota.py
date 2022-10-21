diccionari = {"Pepe":[], "Manolo":[], "Xeng":[]}

n = input("Disme un nom: ")
x = int(input("Introdueix un pes: "))
try: 
    diccionari[n].append(x)
    print("Pesos de Pepe",diccionari["Pepe"])
except:
    diccionari[n]=[x]
    print("S'ha creat l'usuari " + n + " i se li ha afegit el pes",x)