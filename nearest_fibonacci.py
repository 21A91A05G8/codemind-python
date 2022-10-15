n=int(input())
a=0
b=1
for i in range(2,n):
    c=a+b
    a=b
    b=c
    if c<n:
        x=c
    if c>n:
        y=c
        break
if abs(x-n)<abs(y-n):
    print(x)
elif abs(x-n)==abs(y-n):
    print(x,y)
else:
    print(y)