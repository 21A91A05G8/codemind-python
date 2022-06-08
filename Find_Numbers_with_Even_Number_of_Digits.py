n=int(input())
a=list(map(int,input().split()))
c=0
m=0
for i in range(len(a)):
    c=0
    while(a[i]!=0):
        d=a[i]%10
        a[i]=a[i]//10
        c+=1
    if(c%2==0):
        m+=1
print(m)        