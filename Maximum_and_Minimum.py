n=int(input())
l=list(map(int,input().split()))
s=[]
c=0
k=[]
for i in l:
    if l.count(i)==i:
        s.append(i)
for i in s:
    c=0
    k.append(i)
    c+=1
if c>0:
    print(min(k),max(k),end=' ')    
else:
    print("-1")
    