n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(1,a):
        if l[i]<l[i-1]:
            c+=1
    if c==0:
        print(c)
    else:
        print(max(l)-min(l))