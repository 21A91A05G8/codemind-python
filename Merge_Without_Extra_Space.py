t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    v=[]
    for i in l:
        v.append(i)
    for i in m:
        v.append(i)
    print(*sorted(v))