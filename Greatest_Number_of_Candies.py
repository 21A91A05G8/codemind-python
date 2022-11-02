n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range(n):
    if(l[i]+k>=max(l)):
        print('True',end=' ')
    else:
        print('False',end=' ')