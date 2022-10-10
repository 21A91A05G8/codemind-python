s=input().split()
b='aeiou'
d=[]
c=0
for i in s:
    c=0
    for j in i:
        if j in b:
            c+=1
    d.append(c)
print(d.count(min(d))) 
        