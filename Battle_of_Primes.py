def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
x=int(input())
y=int(input())
k=x+y
for j in range(1,10):
    res=k+j
    if(prime(res)):
        print(j,end=' ')
        break