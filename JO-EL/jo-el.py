i = input().split(";")

for x in i:
    if len(x) >= 10:
        i[i.index(x)] = "ERROR"
print(";".join(i))