s1=input().lower().split()
s2=input().lower().split()
#a=list(s1.split(" "))
#b=list(s2.split(" "))
c=[]
for i in s2:
    if i in s1 and i not in c:
        c.append(i)
print(" ".join(c))        