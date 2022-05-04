import math
n=int(input())
temp=n
c=1
sq=n*n
temp=n
while(n>0):
    c=c*10
    n=n//10
if(sq%c==temp):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number");