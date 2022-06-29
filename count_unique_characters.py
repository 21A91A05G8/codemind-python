n=input()
n=n.lower()
n=list(n)
k=n.copy()
k=set(k)
k=list(k)
c=0
for i in range(len(k)):
    if(n.count(k[i])==1 and k[i]!=" "):
        c+=1
print(c)        