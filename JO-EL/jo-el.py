n = int(input())
deus = int()
nota = int()

while n != int():
    n = int(input())
    if n == 10:
        deus += 1
        nota += 1
    elif 0 <= n <= 10:
        nota += 1

print("TOTAL NOTES: " + str(nota) + " NOTES10: " + str(deus))