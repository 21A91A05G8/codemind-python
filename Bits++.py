n=int(input())
c=0
for i in range(n):
    s=input()
    if "++" in s:
        c+=1
    else:
        c-=1
print(c)        