n=int(input())
l=list(map(int,input().split()))
k=int(input())
b=[]
c=0
for i in l:
    if(l.count(i)==k):
        b.append(i)
    if(b.count(i)==1):
        print(i,end=' ')
if(b==[]):
    print('-1')