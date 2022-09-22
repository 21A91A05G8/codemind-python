n=input()
n=n.split()
d='aeiou'
c=0
for i in n:
    k=i
    c=0
    for i in k:
        if i in d:
            c+=1
    print(c,end=' ')        
        