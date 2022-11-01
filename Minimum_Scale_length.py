n=int(input())
a=list(map(int,input().split()))
c=0
max=0
for i in range (1,100):
    c=0
    for j in a:
        if j%i==0:
            c+=1
    if c==n:
        max=i;
print(max)        