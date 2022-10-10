n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if i not in a:
        a.append(i)
for i in range(len(a)):
    print(a[i],l.count(a[i]),end=' ')
