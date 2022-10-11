n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(a[i]>a[j] and i!=j):
            c+=1
    print(c,end=' ')