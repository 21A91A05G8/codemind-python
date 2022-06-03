n=int(input())
a=list(map(int,input().split()))
s1=0
s2=0
for i in range(len(a)):
    if i%2==0:
        s1=s1+a[i]
    else:
        s2=s2+a[i]
diff=s1-s2
if(diff==0):
    print("YES")
else:
    print("NO")