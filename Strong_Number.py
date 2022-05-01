n=int(input())
sum=0
fact=1
temp=n
while(n!=0):
    d=n%10
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    fact=1
    n=n//10
n=temp
if(sum==n):
    print("The number %d is a strong number" %n)
else:
    print("The number %d is not a strong number" %n)