n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[j]!=-1:
            if(a[i]==a[j] and i!=j):
                print(a[i])
                a[j]=-1
        