n=int(input())
l=list(map(int,input().split()))
max=0
c=0
for i in range(0,n):
    c=0
    for j in range(0,n):
        if(l[i]==l[j]):
            c+=1
    if(c>n//2):
        print(l[i],end=' ')
        break