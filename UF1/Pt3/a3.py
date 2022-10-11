#Primer punt
n = input("Escriu 4 numeros: ")

try:
    l = [int(n[0:1]), int(n[1:2]), int(n[2:3]), int(n[3:4])]
except:
    print("No")
else:
    print("La suma dels nombre es: " + str(sum(l)) + "\n")

#Segon punt
    l.append(int(input("Disme un altre numero: ")))

#Tercer punt
    l.pop(4)

#Quart punt
    s = sorted(l)

#Cinque punt
    M = max(s)
    m = min(s)
    print("El numero mes gran es " + str(M) + "i el mes petit es " + str(m) + "\n")

#Sise punt
    mitjana = int(sum(s)/len(s))
    print("La mitjana aritmetica es: " + str(mitjana))