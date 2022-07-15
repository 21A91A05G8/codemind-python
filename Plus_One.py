n=int(input())
a=list(map(int,input().split()))
t=0
for i in range(0,n):
    t=t*10+a[i]
t+=1
s=str(t)
for i in s:
    print(i,end=' ')