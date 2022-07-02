n=int(input())
a=list(map(int,input().split()))
b=list()
for i in a:
    i=i**2
    b.append(i)
print(*sorted(b))    