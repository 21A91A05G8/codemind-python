n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    p=1
    for j in range(n):
        if(i!=j):
            p*=a[j]
    print(p,end=' ')        