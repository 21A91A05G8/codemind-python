def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
if prime(n):
    rev=0
    while(n):
        r=n%10
        n=n//10
        rev=rev*10+r
    if prime(rev):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")