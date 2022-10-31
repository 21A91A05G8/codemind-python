n=int(input())
l=list(map(int,input().split()))
t=int(input())
c=0
for i in range(n):
    if(l[i]==t):
        c=1
        print(i,end=" ")
        break
for i in range(n-1,-1,-1):
    if(l[i]==t):
        c=1
        print(i,end=" ")
        break
if(c==0):
    print('-1 -1')
        