s1=input().lower()
s2=input().lower()
k=[]
c=0
for i in s1:
    if i  in s2:
        k.append(i)
for i in s2:
    if i  in s1:
        k.append(i)
for i in sorted(set(k)):
    if i!=' ':
        c+=1
print(c)    
        ##print(i,end='')
        