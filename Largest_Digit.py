n=int(input())
largest=0
while(n>0):
    r=n%10
    if(largest<r):
        largest=r
    n=n//10
print(largest)