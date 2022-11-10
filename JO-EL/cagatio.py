i=int(input())
while i>0:
    a=["À","Á","È","É","Ì","Í","Ò","Ó","Ù","Ú"]
    aa=["A","A","E","E","I","I","O","O","U","U"]
    s=[]
    f=input()
    ff=f.split(", ")
    fff=f.split(" i ")
    ff.append(fff[-1])
    for l in ff:
        s.append(l[0])
    for x in s:
        if x == a:
    print("".join(s).upper())
    i-=1
