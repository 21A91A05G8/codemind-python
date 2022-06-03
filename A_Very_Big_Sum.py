n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    sum=sum+a[i]
print(sum)    