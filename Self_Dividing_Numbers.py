def count(num):
    c=0
    while num:
        d=num%10
        num//=10
        c+=1
    return c
def fun(num):
    p=0
    h=num
    while num:
        d=num%10
        num//=10
        if d>0:
            if h%d==0:
                p+=1
    return p
n=int(input())
m=int(input())
for i in range(n,m+1):
    c=count(i)
    k=fun(i)
    if(k==c):
        print(i,end=' ')