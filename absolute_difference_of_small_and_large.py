s=input().split()
for i in s:
    a=ord(min(i))
    b=ord(max(i))
    print(b-a,end=' ')