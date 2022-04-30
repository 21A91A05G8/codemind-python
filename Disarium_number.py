import math
n=int(input())
sum=0
c=0
temp=n;
while(temp):
    temp=temp//10
    c+=1
temp=n
while(temp):
    r=temp%10
    sum=sum+pow(r,c)
    temp=temp//10
    c-=1
if(sum==n):
    print("True")
else:
    print("False")
    