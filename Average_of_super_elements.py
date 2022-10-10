n=int(input())
l=list(map(int,input().split()))
c=0
s=0
for i in set(l):
    if l.count(i)==i:
        c+=1
        s=s+i
if c==0:
    print("-1")
else:
    su=s/c
    print("%.2f"%su)