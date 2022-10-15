a=input().split()
s=a[len(a)-1]
k=min(s)
if k and k.lower() in s:
    print(k.lower())
else:
    print(k)