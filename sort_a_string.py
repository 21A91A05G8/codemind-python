a=input().split()
b=[]
c=[]
for i in a:
    for j in i:
        if j.isalpha():
            b.append(j)
        else:
            c.append(j)
b.sort()
k,l=0,0
for i in a:
    for j in range(len(i)):
        if i[j] in b:
            print(b[k],end='')
            k+=1
        else:
            print(c[l],end='')
            l+=1
    print(end=' ')