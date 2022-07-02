a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
for i in range(0,3):
    if(a[i]>b[i]):
        c+=1
    elif(b[i]>a[i]):
        d+=1
print(c,d)        