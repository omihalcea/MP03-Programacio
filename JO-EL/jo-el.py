i=int(input())
while i-1>0:
    n=list(map(int, input().split()))
    l=[]
    while (n[0]-1)>0:
        fil=l.append(list(map(int, input().split())))
        n[0]-=1
    posicio=list(map(int, input().split()))
    uns=int()
    if l[posicio[0]][posicio[1]]==1:
        print("BOOM")
    else:
        for u in l:
            uns+=u.count(1)
        print(uns)
    i-=1