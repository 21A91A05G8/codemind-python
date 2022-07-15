n=int(input())
a=list(map(int,input().split()))
c=0
count=0
for i in a:
    if(i==1):
        c+=1
    if(i==0):
        if(c>count):
            count=c
        c=0
if(c>count):
    count=c
print(count)    