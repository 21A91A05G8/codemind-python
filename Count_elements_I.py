a,b=map(int,input().split())
m=list(map(int,input().split()))
n=list(map(int,input().split()))
d=[]
c=0
for i in m:
    if i in n and i not in d:
        d.append(i)
        c+=1
print(c)