n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if(l[i]!=0 and l[i]!=1):
        print('False')
        break
else:
    print('True')
