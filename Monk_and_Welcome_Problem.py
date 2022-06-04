n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(len(a)):
    for i in range(len(b)):
        sum=a[i]+b[i]
        print(sum,end=' ') 
    break    