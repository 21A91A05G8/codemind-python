n=input()
v="AEIOUaeiou"
l=[]
c=0
for i in n:
    if i in v and i not in l:
        l.append(i)
print(*l)        