n=int(input())
for i in range(n):
    x=int(input())
    c=0
    l=list(map(int,input().split()))
    for i in l:
        if i%2!=0:
            c+=1
    print(int(c/2))