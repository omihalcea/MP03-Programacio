i=int(input())
while i>0:
    n=list(map(int, input().split()))
    l=[]
    while (n[0]-1)>0:
        fil=l.append(list(map(int, input().split())))
        n[0]-=1
    p=list(map(int, input().split()))
    px=p[0]
    py=p[1]
    uns=int()
    if l[p[0]][p[1]]==1:
        print("BOOM")
    else:
        for u in range(l[px-1],l[py+1]):
            for x in range(l[py-1],l[py+1]):
                uns+=u.count(1)
        print(uns)
    i-=1