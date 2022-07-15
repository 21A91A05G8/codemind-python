t=int(input())
for i in range(t):
    m=int(input())
    l=list(map(int,input().split()))
    for j in range(1,m+1):
        if(l.count(j)==0):
            print(j)