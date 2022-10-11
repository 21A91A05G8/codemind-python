n=int(input())
a=list(map(int,input().split()))
b=sorted((set(a)))
if(n>=3):
    print(b[-3])
else:
    print(max(b))