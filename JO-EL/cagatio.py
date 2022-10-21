e = int(input())
caga = str("caga")
tio = str("tio")
l = ["caga"]
while e != 0:
    n = int(input())
    while n >= 2:
        l.append(caga)
        n -= 1
    print("Caga " + str(l) + "tio")
    e -= 1