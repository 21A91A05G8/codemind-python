n=int(input())
l=list(map(int,input().split()))
sum=0
for i in set(l):
    sum=sum+i
print(sum)    
    