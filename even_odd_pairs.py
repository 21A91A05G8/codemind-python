n=int(input())
l=list(map(int,input().split( )))
c=[]
d=[]
for i in range(n):
    if(l[i]%2==0):
        c.append(l[i])
    else:
        d.append(l[i])
i=0
j=0
while(i<len(c) or j<len(d)):
    if(i<len(c)):
        print(c[i],end=" ")
        i+=1
    if(j<len(d)):
        print(d[j],end=" ")
        j+=1
if(n%2!=0):
    print("0")