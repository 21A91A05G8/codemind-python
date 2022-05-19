a=int(input())
b=int(input())
for n in range(a,b+1):
    rev=0
    temp=n
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if(rev==n):
        print(n,end=' ')
        