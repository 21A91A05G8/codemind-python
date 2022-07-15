n,m=map(int,input().split())
a=list(map(int,input().split()))
s=0
c=0
for i in range(0,n):
    for j in range(i,n):
        s+=a[j]
        if(s==m):
            c+=1
        if(s>m):
            break
    s=0
print(c)    