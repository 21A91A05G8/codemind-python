n=int(input())
x=list(map(int,input().split()))
s=0
for i in x:
   s+=i*(2**(n-1))
   n-=1
print(s) 