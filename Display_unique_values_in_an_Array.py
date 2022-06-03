n=int(input())
a=list(map(int,input().split()))
c=0
c1=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(a[i]==a[j] and i!=j):
            c+=1
    if(c==0):
        print(a[i],end=' ')
        c1+=1
if(c1==0):
    print("-1")
            